"""Exact algebra and finite arithmetic accompanying proof.tex.

This is not a proof assistant. The analytic modular facts, infinite descent,
and historical eligibility argument require mathematical and source review.
"""

from fractions import Fraction
from math import factorial, gcd, isqrt

import sympy as s


def multiplier(a, b, c, d):
    return d * b + c * a + 2 * d**2 - 2 * d * c - 2 * d * a


# Exact conversion of Weber's cubed multiplier to the convention in the paper.
# All terms depend only on the matrix entries modulo 16.
matrix_count = 0
for a in range(16):
    for b in range(16):
        for c in range(16):
            for d in range(16):
                if (a * d - b * c) % 16 != 1:
                    continue
                if (a % 2, b % 2, c % 2, d % 2) not in (
                    (1, 0, 0, 1), (0, 1, 1, 0)
                ):
                    continue
                r = d - c
                assert r % 2
                exponent = r**2 - 1 - 9 * r * (d + c + b - a)
                assert (exponent + multiplier(a, b, c, d)) % 16 == 0
                matrix_count += 1
assert matrix_count == 1024

# The root-selection congruence is universal: q and B are reduced modulo 16.
for q in (3, 11):
    for j in range(8):
        B = -2 * j
        a = B * pow(q, -1, 16)
        assert (a - 3 * B) % 16 == 0
        L = multiplier(a, 1 + B * a, -1, -B)
        assert (L + 12 * j) % 16 == 0
        assert (L % 16 == 0) == (j in (0, 4))

# Spot-check the exact transformation matrix identities for a range of primes.
# Their proof for every odd prime is the displayed matrix calculation.
z = s.symbols('z')
for p in list(s.primerange(3, 100)):
    for nu in range(p):
        nup = ((16 * nu + 2) * pow(16, -1, p)) % p
        ell = (16 * nu + 2 - 16 * nup) // p
        assert ell % 2 == 0 and (ell - 2 * p) % 16 == 0
        assert 16 * nu + 2 == 16 * nup + ell * p
        if nu:
            nup = (-pow(256 * nu, -1, p)) % p
            b = (-1 - 256 * nu * nup) // p
            assert 16 * nu * (-16 * nup) - b * p == 1
            assert multiplier(16 * nu, b, p, -16 * nup) % 16 == 0
            assert s.cancel(
                (16 * nu * ((z + 16 * nup) / p) + b)
                / (p * ((z + 16 * nup) / p) - 16 * nup)
                - (16 * nu * z - 1) / (p * z)
            ) == 0

X, Y, a, b, c = s.symbols('X Y a b c')
e, f, k = 2 * b - a**2, b**2 - 2 * a * c, -c**2
cubic = X**3 + a * X**2 + b * X + c
assert s.expand(s.resultant(cubic, Y - X**2, X)
                - (Y**3 + e * Y**2 + f * Y + k)) == 0
assert s.expand(s.resultant(cubic, Y - X**4, X)
                - (Y**3 + (2*f-e**2)*Y**2 + (f**2-2*e*k)*Y-k**2)) == 0

x, y = s.symbols('x y')
relation = (2*b-a**2)**2 - 2*(b**2-4*a)
assert s.expand(relation.subs({a: -2*x, b: 2*y+4*x**2})
                - 8*(y**2-2*x*(x**3+1))) == 0
solutions = [(0, 0), (-1, 0), (1, -2), (1, 2), (2, -6), (2, 6)]
coefficients = {(-2*x, 2*y+4*x**2) for x, y in solutions}
assert coefficients == {(0, 0), (2, 4), (-2, 0), (-2, 8), (-4, 4), (-4, 28)}
for aa, bb in coefficients:
    assert relation.subs({a: aa, b: bb}) == 0
    assert abs(aa) <= 4 and 0 <= bb <= 28

# The identities within Euler's descent. Completeness is proved in the paper,
# not inferred from a bounded search.
m, n, up, vp = s.symbols('m n up vp', nonzero=True)
u = m**2 - 3*n**2
v = -n*(2*m+3*n)
w = u + (m/n)*v
assert s.expand(w**2 - (u**2-3*u*v+3*v**2)) == 0
mm = -n*(up**2+3*vp**2)/(2*up*vp)
assert s.cancel((-n*(2*m+3*n)).subs(m, mm)
                - n**2*(up**2-3*up*vp+3*vp**2)/(up*vp)) == 0
assert s.cancel((m**2-3*n**2-(m+up*n/vp)**2).subs(m, mm)) == 0

lower_exp = sum(Fraction(7, 2)**n / factorial(n) for n in range(12))
assert lower_exp == Fraction(386627544403, 11678515200)
assert lower_exp > 33

witnesses = {171: (3, 0), 179: (3, 1), 187: (11, 0), 195: (3, 0)}
assert set(witnesses) == {q for q in range(164, 196) if q % 8 == 3}
for q, (p, r) in witnesses.items():
    assert s.isprime(p) and 4*p < q and (q+r*r) % p == 0

primes = [p for p in s.primerange(9, 164) if p % 8 == 3]
assert primes == [11, 19, 43, 59, 67, 83, 107, 131, 139, 163]
for q in (59, 83, 107, 131):
    assert 12 < q and (-q) % 3 == 1
assert 20 < 139 and (-139) % 5 == 1


def reduced_forms(q):
    out = []
    for A in range(1, isqrt(q // 3) + 1):
        for B in range(-A, A+1):
            if (B*B+q) % (4*A):
                continue
            C = (B*B+q) // (4*A)
            if C < A or gcd(A, gcd(B, C)) != 1:
                continue
            if (abs(B) == A or A == C) and B < 0:
                continue
            out.append((A, B, C))
    return out


expected = {
    3: (1, 1, 1), 4: (1, 0, 1), 7: (1, 1, 2), 8: (1, 0, 2),
    11: (1, 1, 3), 19: (1, 1, 5), 43: (1, 1, 11),
    67: (1, 1, 17), 163: (1, 1, 41),
}
for q, form in expected.items():
    assert reduced_forms(q) == [form]

print(f'PASS: Weber multiplier conversion ({matrix_count} residue matrices).')
print('PASS: complete root-selection residue calculation; modular matrix identities.')
print('PASS: cubic resultants, coefficient substitution, Euler descent identities.')
print('PASS: exact exponential bound, finite exclusions, and nine reduced-form lists.')
print('These checks do not certify the analytic modular inputs, the infinite descent,')
print('or the historical cutoff. No independent audit or formal verification is claimed.')
