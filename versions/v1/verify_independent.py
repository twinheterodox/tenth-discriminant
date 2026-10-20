"""Independent, exact verification using periodic bitsets and Euler's criterion.

Unlike the C++ program, this scans the wheel residues directly, and eliminates
whole arithmetic progressions using Python arbitrary-precision integer bitsets.
Only the Python standard library is needed.
"""
from fractions import Fraction
from math import gcd, isqrt, prod
from time import perf_counter


def primes_up_to(n):
    return [p for p in range(3, n + 1, 2)
            if all(p % d for d in range(2, isqrt(p) + 1))]


def reduced_forms(q):
    """Primitive, reduced positive forms of discriminant -q, exactly."""
    forms = []
    for a in range(1, isqrt(q // 3) + 1):
        for b in range(-a, a + 1):
            numerator = b * b + q
            if numerator % (4 * a):
                continue
            c = numerator // (4 * a)
            if c < a or gcd(gcd(a, b), c) != 1:
                continue
            if (abs(b) == a or a == c) and b < 0:
                continue
            forms.append((a, b, c))
    return forms


def main():
    start = perf_counter()
    limit, largest_prime = 10**10, 109
    lower = 4 * largest_prime + 1
    primes = primes_up_to(largest_prime)
    wheel = [p for p in primes if p <= 17]
    rest = [p for p in primes if p > 17]
    modulus = 8 * prod(wheel)
    # Euler's criterion, independent of C++'s enumeration of squares.
    good = {p: [pow((-r) % p, (p - 1) // 2, p) == p - 1
                for r in range(p)] for p in primes}
    residues = [r for r in range(3, modulus, 8)
                if all(good[p][r % p] for p in wheel)]
    large_survivors = []
    total = 0
    for r in residues:
        k_min = max(0, (lower - r + modulus - 1) // modulus)
        k_max = (limit - 1 - r) // modulus
        if k_min > k_max:
            continue
        n = k_max + 1
        total += n - k_min
        live = ((1 << n) - 1) ^ ((1 << k_min) - 1)
        for p in rest:
            period = sum(1 << k for k in range(p)
                         if good[p][(r + k * modulus) % p])
            copies = (n + p - 1) // p
            repeated = period * (((1 << (p * copies)) - 1) // ((1 << p) - 1))
            live &= repeated
            if not live:
                break
        while live:
            bit = live & -live
            k = bit.bit_length() - 1
            large_survivors.append(r + k * modulus)
            live ^= bit
    small = [q for q in range(11, lower, 8)
             if all(good[p][q % p] for p in primes if 4 * p < q)]
    print("method independent_periodic_bitsets")
    print("limit_exclusive", limit)
    print("large_begin", lower)
    print("wheel_modulus", modulus)
    print("wheel_residues", len(residues))
    print("large_candidates_checked", total)
    print("large_survivors", sorted(large_survivors))
    print("small_survivors", small)
    assert not large_survivors
    assert small == [11, 19, 43, 67, 163]
    for q in [3, 4, 7, 8] + small:
        forms = reduced_forms(q)
        print("reduced_forms", q, forms)
        assert len(forms) == 1
    # Exact rational checks used in the analytic argument.
    theta_lower = Fraction(35, 33) * Fraction(2497, 2500) - Fraction(1, 10000)
    assert theta_lower > 1
    assert 8**12 > 10**5 * 3**12  # log(10^5) < 12, since e > 8/3.
    assert Fraction(10 * 24, 100000) < Fraction(3, 1000)
    print("theta_lower_bound", theta_lower, ">", 1)
    print("zero_distance_times_logq_upper_bound", Fraction(10 * 24, 100000))
    print("banks_lower_bound", Fraction(3, 1000))
    print("elapsed_seconds", perf_counter() - start)


if __name__ == "__main__":
    main()
