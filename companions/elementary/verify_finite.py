"""Exhaustive integer check below the analytically proved cutoff 32768.

For class number one and q > 8, q = 3 (mod 8) and -q is a nonzero
nonsquare modulo each odd prime p < q/4. Nonfundamental candidate
integers are deliberately included. Only primes at most 31 are needed.
The standard reduced-form enumeration also checks the nine survivors.
"""

from math import gcd, isqrt


def primes_up_to(limit):
    return [p for p in range(3, limit + 1, 2)
            if all(p % d for d in range(2, isqrt(p) + 1))]


def squarefree(n):
    return n > 0 and all(n % (d*d) for d in range(2, isqrt(n) + 1))


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
    forms = []
    for a in range(1, isqrt(q // 3) + 1):
        for b in range(-a, a + 1):
            if (b*b + q) % (4*a):
                continue
            c = (b*b + q) // (4*a)
            if c < a or gcd(gcd(a, b), c) != 1:
                continue
            if b < 0 and (abs(b) == a or a == c):
                continue
            forms.append((a, b, c))
    return forms


def main():
    limit = 32768
    primes = primes_up_to(31)
    squares = {p: {a*a % p for a in range(p)} for p in primes}
    # A second characterization checks every entry of these small tables.
    for p in primes:
        for r in range(p):
            assert (r not in squares[p]) == (
                r != 0 and pow(r, (p-1)//2, p) == p-1)

    survivors, rejections = [], {p: 0 for p in primes}
    checked = 0
    for q in range(11, limit, 8):
        checked += 1
        for p in primes:
            if 4*p < q and (-q) % p in squares[p]:
                rejections[p] += 1
                break
        else:
            survivors.append(q)

    assert checked == 4095
    assert checked == sum(rejections.values()) + len(survivors)
    assert survivors == [11, 19, 43, 67, 163]
    small = [q for q in range(1, 9) if fundamental_discriminant(-q)]
    assert small == [3, 4, 7, 8]
    final = small + survivors
    print("limit_exclusive", limit)
    print("candidate_integers_checked", checked)
    print("largest_prime", max(primes))
    for p, count in rejections.items():
        if count:
            print("first_rejecting_prime", p, "count", count)
    print("final_absolute_discriminants", final)
    for q in final:
        assert fundamental_discriminant(-q)
        forms = reduced_forms(q)
        assert len(forms) == 1
        print("reduced_forms", q, forms)
    print("PASS: exhaustive finite exclusion and nine class-number checks.")
    print("The analytic cutoff is a separate input proved in proof.tex.")


if __name__ == "__main__":
    if not __debug__:
        raise RuntimeError("Run without Python -O or -OO.")
    main()
