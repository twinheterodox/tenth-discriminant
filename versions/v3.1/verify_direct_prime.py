#!/usr/bin/env python3
"""Exact numerical certificate for proof.tex; optional finite geometry checks.

All decisions use integers or Fraction. This does not verify Banks's
determinant/interpolation results, the classical prime estimates, or the
general analytic deductions. The sanity checks test finite examples only.
"""

import argparse
from collections import Counter
from fractions import Fraction as F
from math import gcd, isqrt


PRIMES = (2, 3, 5, 7)
P = 210
Q0 = 1_000_000


class Checks:
    def __init__(self):
        self.count = 0

    def __call__(self, label, condition):
        if not condition:
            raise AssertionError(label)
        self.count += 1
        print("PASS:", label)


def exp_bounds(x, terms=160):
    """Enclose exp(x) by its Taylor sum and a geometric upper tail."""
    if x < 0 or terms < 0 or x >= terms + 2:
        raise ValueError("Require 0 <= x < terms + 2 and terms >= 0")
    term = total = F(1)
    for k in range(1, terms + 1):
        term *= x / k
        total += term
    next_term = term * x / (terms + 1)
    return total, total + next_term / (1 - x / (terms + 2))


def sieve_constants():
    rho = positive = signed = F(1)
    for p in PRIMES:
        rho *= 1 - F(1, p*p)
        positive *= 1 + F(1, p)
        signed *= 1 - F(1, p)
    return rho, positive, signed


def arithmetic_certificate():
    check = Checks()
    rho, positive, signed = sieve_constants()
    check("primitive density = 768/1225", rho == F(768, 1225))
    check("sum |mu(d)|/d = 96/35", positive == F(96, 35))
    check("sum mu(d)/d = 8/35", signed == F(8, 35))
    check("boundary coefficients = 88/35 and 192/35",
          positive - signed == F(88, 35) and 2*positive == F(192, 35))
    check("pi*rho/4 < 0.493, using pi < 22/7",
          F(22, 7)*rho/4 < F(493, 1000))
    check("B_R < 2.52 for R >= 1000",
          positive - signed + 2*positive/1000 < F(63, 25))

    log_low, log_high = F(2763, 200), F(1727, 125)
    _, upper = exp_bounds(log_low)
    check("log(1,000,000) > 13.815", upper < Q0)
    lower, _ = exp_bounds(log_high)
    check("log(1,000,000) < 13.816", lower > Q0)
    lower, _ = exp_bounds(F(52, 25))
    check("log(8) < 2.08", lower > 8)
    _, upper = exp_bounds(F(1))
    check("log(4) > 1", upper < 4)
    _, upper = exp_bounds(F(2))
    check("log(q/4) > 2 and q > exp(2) for q >= q0", upper < Q0//4)
    check("sqrt(q0) = 1000", 1000**2 == Q0)

    H = 10**9
    N0 = Q0**13
    check("log(H)/log(q) <= 3/2 for q >= q0", H**2 == Q0**3)
    check("1/log(H) < 0.049", 1/(F(3, 2)*log_low) < F(49, 1000))
    check("q0 >= 9 and 319 <= H < N(q0)", Q0 >= 9 and 319 <= H < N0)
    check("H^(2/3) = 10^6", (10**6)**3 == H**2)
    check("Banks size hypothesis, using M >= N", 10**6*N0 > 2*97**2)
    check("M > H, M >= q/4, and M >= q0, using N(q) >= q", N0 > H and N0 >= Q0)

    r, c = F(73, 10000), F(19, 500)
    check("S23/S1 < 0.0073", F(768*97**2, H) < r)
    check("N^4 M/S1 < 0.038", F(4*97**2, 10**6) < c)
    check("26c/M < 10^-6 using M >= q0", 26*c/Q0 < F(1, 10**6))
    check("positive determinant coefficient", F(1, 4) - 3*r/4 > 0)

    z = F(52, 3)
    lhs = (F(1, 4) - 3*r/4)*z
    rhs = (
        F(493, 1000)*z*z*log_high/1000
        + (1+r)/2 + F(3, 2)
        + ((1+r)*F(52, 25) + F(49, 1000) + 2*c)/log_low
        + F(126, 25_000) + F(4, Q0) + F(1, 10**6)
    )
    check("left side = 127153/30000", lhs == F(127153, 30000))
    check("left side > 4.238", lhs > F(2119, 500))
    check("right side < 4.216", rhs < F(527, 125))
    check("contradiction gap > 0.022", lhs - rhs > F(11, 500))
    print(f"\nAll {check.count} exact arithmetic checks passed.")
    print("Exact rational gap:", lhs - rhs)
    print("Conditional cutoff: q < 1,000,000 (50-fold improvement over v2).")
    return check.count


def a_interval(q, x, b):
    """Exact horizontal section of the standard quadratic integer lattice."""
    twice_real = 1 if q % 4 == 3 else 0
    m_max = isqrt(4*x - q*b*b)
    return -((m_max + twice_real*b)//2), (m_max - twice_real*b)//2


def count_rows(q, x):
    total = 0
    for b in range(1, isqrt(4*x//q) + 1):
        low, high = a_interval(q, x, b)
        total += high - low + 1
    return total


def enumerate_pairs(q, x):
    twice_real = 1 if q % 4 == 3 else 0
    for b in range(1, isqrt(4*x//q) + 1):
        low, high = a_interval(q, x, b)
        for a in range(low, high + 1):
            numerator = (2*a + twice_real*b)**2 + q*b*b
            assert numerator % 4 == 0
            yield a, b, numerator//4


def mobius_divisors():
    ds = [(1, 1)]
    for p in PRIMES:
        ds += [(d*p, -mu) for d, mu in ds]
    return ds


def root_bounds(n, scale=10**6):
    k = isqrt(n*scale*scale)
    return F(k, scale), F(k+1, scale)


def primes_up_to(limit):
    flags = bytearray(b"\x01")*(limit+1)
    flags[:2] = b"\x00\x00"
    for p in range(2, isqrt(limit)+1):
        if flags[p]:
            flags[p*p:limit+1:p] = b"\x00"*((limit-p*p)//p+1)
    return [p for p, flag in enumerate(flags) if flag]


def quadratic_symbol_at_prime(q, p):
    if q % p == 0:
        return 0
    if p == 2:
        return 1 if (-q) % 8 in (1, 7) else -1
    residue = pow((-q) % p, (p-1)//2, p)
    return 1 if residue == 1 else -1


def sanity_checks():
    check = Checks()
    rho, positive, signed = sieve_constants()
    divisors = mobius_divisors()
    cases = [(q, x) for q in (7, 8, 43, 163, 1_000_003)
             for x in (q//4, q, 10*q)]
    for q, x in cases:
        pairs = list(enumerate_pairs(q, x))
        raw = len(pairs)
        primitive = sum(gcd(gcd(a, b), P) == 1 for a, b, _ in pairs)
        inclusion = sum(mu*count_rows(q, x//(d*d)) for d, mu in divisors)
        r_low, r_high = root_bounds(q)
        _, x_high = root_bounds(x)
        lower = 3*x/r_high - 2*x_high - 2*x_high/r_low
        upper = F(22, 7)*x/r_low + 2*x_high/r_low
        primitive_upper = (
            F(22, 7)*rho*x/r_low
            + (positive-signed+2*positive/r_low)*x_high
        )
        check(f"lattice and inclusion-exclusion, q={q}, X={x}",
              raw == count_rows(q, x) and primitive == inclusion
              and lower <= raw <= upper and primitive <= primitive_upper)

    primes = primes_up_to(2000)
    for q in (7, 8, 11, 19, 43, 67, 163):
        norm_counts = Counter(n for _, _, n in enumerate_pairs(q, 2000))
        expected = {-1: 0, 0: 1, 1: 2}
        check(f"prime-norm multiplicities for all primes <= 2000, q={q}",
              all(norm_counts[p] == expected[quadratic_symbol_at_prime(q, p)]
                  for p in primes))
    print(f"\nAll {check.count} finite sanity cases passed.")
    print("These finite examples are not a proof of the general counting lemmas.")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--sanity", action="store_true", help="also run finite lattice checks")
    args = parser.parse_args()
    arithmetic_certificate()
    if args.sanity:
        print("\nFinite lattice and prime-norm sanity checks:")
        sanity_checks()
    print("\nBanks's external results and the general analytic proof require mathematical review.")


if __name__ == "__main__":
    main()
