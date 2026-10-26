#!/usr/bin/env python3
"""Exact checks for the uniform-interval bound (quadratic-intervals-v0.1.0).

These are finite algebraic checks and rational certificates, not a formal
verification or an independent mathematical audit. Standard library only.
Run from any directory; output is deterministic.
"""

from fractions import Fraction as F
from math import comb, factorial, isqrt


def primes_to(n):
    sieve = bytearray(b"\x01") * (n + 1)
    sieve[:2] = b"\x00\x00"
    for p in range(2, isqrt(n) + 1):
        if sieve[p]:
            sieve[p * p : n + 1 : p] = b"\x00" * ((n - p * p) // p + 1)
    return [p for p in range(2, n + 1) if sieve[p]]


def vp(n, p):
    assert n
    n = abs(n)
    e = 0
    while n % p == 0:
        e += 1
        n //= p
    return e


def add(a, b):
    return a[0] + b[0], a[1] + b[1]


def sub(a, b):
    return a[0] - b[0], a[1] - b[1]


def mul(a, b, delta):
    return a[0] * b[0] + delta * a[1] * b[1], a[0] * b[1] + a[1] * b[0]


def scale(a, c):
    return a[0] * c, a[1] * c


def norm(a, delta):
    return a[0] ** 2 - delta * a[1] ** 2


def divexact(a, b, delta):
    denominator = norm(b, delta)
    numerator = mul(a, (b[0], -b[1]), delta)
    assert denominator and all(x % denominator == 0 for x in numerator)
    return tuple(x // denominator for x in numerator)


def reduce(a, p):
    return a[0] % p, a[1] % p


def invmod(a, delta, p):
    invnorm = pow(norm(a, delta) % p, -1, p)
    return reduce((a[0] * invnorm, -a[1] * invnorm), p)


def pivot_columns(matrix, delta, p):
    """Independent Gaussian elimination over F_p[sqrt(delta)]."""
    rows = [[reduce(a, p) for a in row] for row in matrix]
    rank = 0
    pivots = []
    for col in range(len(rows[0])):
        pivot = next((j for j in range(rank, len(rows)) if rows[j][col] != (0, 0)), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        inverse = invmod(rows[rank][col], delta, p)
        rows[rank] = [reduce(mul(x, inverse, delta), p) for x in rows[rank]]
        for j in range(rank + 1, len(rows)):
            factor = rows[j][col]
            if factor != (0, 0):
                rows[j] = [reduce(sub(x, mul(factor, y, delta)), p)
                           for x, y in zip(rows[j], rows[rank])]
        pivots.append(col)
        rank += 1
        if rank == len(rows):
            break
    return pivots


def bareiss(matrix, delta):
    """Fraction-free determinant in Z[sqrt(delta)], with exact divisions."""
    rows = [row.copy() for row in matrix]
    previous, sign = (1, 0), 1
    for k in range(len(rows) - 1):
        pivot = next((j for j in range(k, len(rows)) if rows[j][k] != (0, 0)), None)
        assert pivot is not None, "The selected minor should be nonzero."
        if pivot != k:
            rows[k], rows[pivot] = rows[pivot], rows[k]
            sign *= -1
        pivot_value = rows[k][k]
        for i in range(k + 1, len(rows)):
            for j in range(k + 1, len(rows)):
                numerator = sub(mul(pivot_value, rows[i][j], delta),
                                mul(rows[i][k], rows[k][j], delta))
                rows[i][j] = divexact(numerator, previous, delta)
            rows[i][k] = (0, 0)
        previous = pivot_value
    return scale(rows[-1][-1], sign)


def ceil_fourth_ratio(num, den=1):
    hi = 1
    while hi ** 4 * den < num:
        hi *= 2
    lo = 0
    while hi - lo > 1:
        mid = (lo + hi) // 2
        if mid ** 4 * den >= num:
            hi = mid
        else:
            lo = mid
    return hi


def grid(delta, n):
    q = abs(delta)
    nx = ceil_fourth_ratio(n * n * q)
    ny = ceil_fourth_ratio(n * n, q)
    points = [(a, b) for b in range(ny) for a in range(nx)]
    assert len(points) >= n
    # Alternate the ordering to ensure some examples use both coordinates.
    points.sort(key=lambda a: (a[0] * a[0] + q * a[1] * a[1], a[1], a[0]))
    return points[:n]


def jet_matrix(delta, R, S, n):
    J = (R * S + n - 1) // n
    points = grid(delta, n)
    columns = [(i, k) for i in range(n) for k in range(J)]
    powers = []
    for z in points:
        zp, wp = [(1, 0)], [(1, 0)]
        for _ in range(max(R, S)):
            zp.append(mul(zp[-1], z, delta))
            wp.append(mul(wp[-1], (z[0], -z[1]), delta))
        powers.append((zp, wp))
    matrix = []
    for r in range(R):
        for s in range(S):
            matrix.append([
                (0, 0) if k > r else scale(mul(powers[i][0][r-k], powers[i][1][s], delta), comb(r, k))
                for i, k in columns
            ])
    return points, columns, matrix


def check_minors():
    cases = [
        (-3, 5, 2, 3), (-3, 11, 3, 6), (-3, 11, 4, 8),
        (-4, 7, 2, 4), (-4, 11, 4, 9),
        (-7, 5, 2, 3), (-7, 13, 3, 7),
        (-8, 5, 2, 3), (-8, 7, 3, 5), (-8, 7, 4, 6),
        (-11, 7, 2, 4), (-11, 13, 3, 7), (-11, 7, 4, 6),
        (-15, 7, 3, 6),
        (5, 7, 2, 4), (5, 13, 4, 8),
        (8, 5, 2, 3), (8, 11, 4, 8),
        (12, 5, 2, 4), (12, 7, 3, 5),
        (13, 5, 2, 4), (13, 7, 3, 5), (13, 7, 4, 6),
        (17, 7, 2, 5), (17, 11, 3, 7),
    ]
    # Verify, rather than assume, that every manually chosen auxiliary prime is inert.
    assert all(pow(c[0] % c[1], (c[1]-1)//2, c[1]) == c[1]-1 for c in cases)
    inert_checks = split_checks = nonzero_split_checks = 0
    factorial_cost_cases = missing_cost_failures = 0
    for delta, R, S, n in cases:
        assert S < n <= R and n*n >= abs(delta)
        points, columns, matrix = jet_matrix(delta, R, S, n)
        assert len(set(reduce(z, R) for z in points)) == n
        pivots = pivot_columns(matrix, delta, R)
        assert len(pivots) == R*S
        square = [[row[j] for j in pivots] for row in matrix]
        determinant = bareiss(square, delta)
        dnorm = abs(norm(determinant, delta))
        assert dnorm and dnorm % R
        orders = [columns[j][1] for j in pivots]
        U = F(R*S*(R-1), 2)
        b = F(S-1, R-1)
        v = F(sum(orders), U)
        for p in primes_to(R + 10):
            if p == 2 or delta % p == 0:
                continue
            symbol = pow(delta % p, (p-1)//2, p)
            if symbol == p-1:
                E = sum(min(r//p, S-1-s) for r in range(R) for s in range(S))
                cost = sum(vp(factorial(k), p) for k in orders)
                bound = 2*E-2*cost
                assert vp(dnorm, p) >= bound, (delta, R, S, n, p, bound)
                relaxed = F(1,p)-F(2,R-1)-F(1,2*S*p)-F(2*R-1,6*S*p*p)-v/F(p-1)
                assert F(vp(dnorm,p), 2*U) >= relaxed
                factorial_cost_cases += bool(cost)
                missing_cost_failures += vp(dnorm, p) < 2*E
                inert_checks += 1
            else:
                bound = 2*R*sum(s//p for s in range(S))
                assert vp(dnorm, p) >= bound, (delta,R,S,n,p,bound)
                assert F(vp(dnorm,p), 2*U) >= b/F(p)-F(2,R-1)
                nonzero_split_checks += bool(bound)
                split_checks += 1
    print(f"Exact quadratic-ring minors and full finite-field ranks: {len(cases)}")
    print(f"Inert-prime valuation checks: {inert_checks}; nonzero column-factorial costs: {factorial_cost_cases}")
    print(f"Split-prime valuation checks: {split_checks}; positive row-factorial lower bounds: {nonzero_split_checks}")
    print(f"Cases where omitting the column-factorial cost gives a false divisibility claim: {missing_cost_failures}")
    print(f"Largest tested minor: {max(R*S for _, R, S, _ in cases)} by {max(R*S for _, R, S, _ in cases)}")
    assert nonzero_split_checks and factorial_cost_cases


def check_row_sums():
    count = 0
    for R in range(2, 81):
        for S in range(2, R+1):
            U = F(R*S*(R-1), 2)
            for p in primes_to(R+7):
                E = sum((S-h)*max(R-p*h, 0) for h in range(1,S))
                lower = U/F(p)-R*S-F(R*(R-1)*(2*R-1),12*p*p)-F(R*(R-1),4*p)
                assert E >= lower
                count += 1
    # Check the summation identity independently by its original double sum.
    identities = 0
    for R in range(2, 26):
        for S in range(2, R+1):
            for p in primes_to(R+3):
                E1 = sum(min(r//p,S-1-s) for r in range(R) for s in range(S))
                E2 = sum((S-h)*max(R-p*h,0) for h in range(1,S))
                assert E1 == E2
                identities += 1
    print(f"Exact finite row-sum lower bounds: {count}; independently expanded identities: {identities}")


def check_constants():
    # exp(7/10)>2 proves log(2)<7/10, using a positive Taylor polynomial.
    a = F(7,10)
    assert sum(a**j/F(factorial(j)) for j in range(4)) > 2
    c = F(7,5)
    assert 1+F(33,8)*a < 4
    floor_cost = 2*c*F(64,63)
    square_cost = 2*c/3
    small_cost = (a+6)/4
    column_cost = 6*c/F(32*31)
    assert floor_cost+square_cost+small_cost+column_cost < 6
    assert a+1+6 < 8
    C32 = F(5,2)*a+6+F(8*32,32-4)+(8*a+6)/28
    assert C32 < F(35,2)
    assert C32+F(1,2) < 18
    assert 42+F(12,5) < 45
    assert F(53,2)-F(132,5) == F(1,10) > 0
    print("Rational arithmetic-error bound:", floor_cost+square_cost+small_cost+column_cost, "< 6")
    print("Rational final-constant bound:", C32+F(1,2), "< 18")
    # The general conductor contribution is <1/2 because
    # K(K-4)-(K-32)(K+2)=26K+64>0. Check the identity algebraically at 3 points.
    for K in [32,33,1000000]:
        assert K*(K-4)-(K-32)*(K+2) == 26*K+64 > 0
    print("All scalar certificates pass; monotonic extensions are proved in the note.")


if __name__ == '__main__':
    print("AUTHOR CHECKS ONLY: no independent audit or formal verification.")
    check_constants()
    check_row_sums()
    check_minors()
    print("PASS")
