"""Exhaustive integer verification of the remaining range q < 2,000.

The proof shows that class number one with q > 8 requires q = 3 (mod 8)
and that -q is a nonzero nonsquare modulo every odd prime p < q/4.
Scan every candidate integer directly, using only primes at most 109.
Nonfundamental integers are deliberately included in the exclusion scan.
Then enumerate primitive reduced forms for each surviving discriminant.
Only the Python standard library is used; no earlier-version file is read.
"""

from math import gcd, isqrt


def primes_up_to(limit):
    return [p for p in range(3, limit + 1, 2)
            if all(p % d != 0 for d in range(2, isqrt(p) + 1))]


def squarefree(n):
    return n > 0 and all(n % (d * d) != 0
                         for d in range(2, isqrt(n) + 1))


def fundamental_discriminant(D):
    if D >= 0:
        return False
    if D % 4 == 1:
        return squarefree(-D)
    if D % 4 == 0:
        d = D // 4
        return d % 4 in (2, 3) and squarefree(-d)
    return False


def reduced_forms(q):
    """One representative per class: |b| <= a <= c, with boundary ties fixed."""
    result = []
    for a in range(1, isqrt(q // 3) + 1):
        for b in range(-a, a + 1):
            if (b * b + q) % (4 * a):
                continue
            c = (b * b + q) // (4 * a)
            if c < a or gcd(gcd(a, b), c) != 1:
                continue
            if b < 0 and (abs(b) == a or a == c):
                continue
            result.append((a, b, c))
    return result


def main():
    limit = 2_000
    primes = primes_up_to(109)
    squares = {p: {a * a % p for a in range(p)} for p in primes}
    # Check the residue tables against Euler's criterion, including zero.
    for p in primes:
        for r in range(p):
            assert (r not in squares[p]) == (
                r != 0 and pow(r, (p - 1) // 2, p) == p - 1
            )

    survivors = []
    first_rejections = {p: 0 for p in primes}
    checked = 0
    for q in range(11, limit, 8):
        checked += 1
        for p in primes:
            if 4 * p >= q:
                continue
            if (-q) % p in squares[p]:
                first_rejections[p] += 1
                break
        else:
            survivors.append(q)

    assert checked == len(range(11, limit, 8)) == 249
    assert sum(first_rejections.values()) + len(survivors) == checked
    assert survivors == [11, 19, 43, 67, 163]
    small = [q for q in range(1, 9) if fundamental_discriminant(-q)]
    assert small == [3, 4, 7, 8]
    final = small + survivors

    print("limit_exclusive", limit)
    print("method exhaustive_direct_residue_scan")
    print("largest_prime", max(primes))
    print("candidate_integers_checked", checked)
    for p, count in first_rejections.items():
        if count:
            print("first_rejecting_prime", p, "count", count)
    print("survivors_above_8", survivors)
    print("final_absolute_discriminants", final)
    for q in final:
        assert fundamental_discriminant(-q)
        forms = reduced_forms(q)
        assert len(forms) == 1
        print("reduced_forms", q, forms)
    print("PASS: exhaustive finite exclusion and nine class-number checks.")
    print("The analytic cutoff and general mathematical argument are separate inputs.")


if __name__ == "__main__":
    main()
