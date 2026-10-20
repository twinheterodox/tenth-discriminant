#!/usr/bin/env python3
"""Exact arithmetic certificate for the refinement in proof.tex (v0.2.0).

This checks finite numerical inequalities, not the analytic proof or
Banks's external lemmas. All decisions use integers or Fraction.
"""

from fractions import Fraction as F


def exp_bounds(x, terms=240):
    """Enclose exp(x) using a Taylor sum and a geometric tail bound."""
    if x < 0 or terms < 0 or x >= terms + 2:
        raise ValueError("Require 0 <= x < terms + 2 and terms >= 0")
    term = total = F(1)
    for k in range(1, terms + 1):
        term *= x / k
        total += term
    next_term = term * x / (terms + 1)
    upper = total + next_term / (1 - x / (terms + 2))
    return total, upper


def check(label, condition):
    if not condition:
        raise AssertionError(label)
    print("PASS:", label)


def main():
    lower, upper = exp_bounds(F(3, 2))
    check("exp(3/2) < 9/2, hence C1 < 1 and C2 < 9/8", upper < F(9, 2))

    # Logarithmic inequalities follow by strict monotonicity of exp.
    comparisons = [
        (F(177, 10), 50_000_000, "upper", "log(50,000,000) > 17.7"),
        (F(1773, 100), 50_000_000, "lower", "log(50,000,000) < 17.73"),
        (F(9), 7000, "lower", "log(7000) < 9"),
        (F(2303, 1000), 10, "lower", "log(10) < 2.303"),
        (F(52, 25), 8, "lower", "log(8) < 2.08"),
    ]
    for exponent, target, endpoint, label in comparisons:
        lower, upper = exp_bounds(exponent)
        check(label, upper < target if endpoint == "upper" else lower > target)

    q0 = 50_000_000
    H = 10**9
    N = q0**18
    M = q0**24
    check("M^3 = N^4", M**3 == N**4)
    check("Banks parameter hypotheses at q0",
          q0 >= 9 and 319 <= H <= N and M >= 8
          and 10**6 * M >= 2 * 97**2)
    check("S1/(N^4 M) > 25", F(10**6, 4 * 97**2) > 25)
    check("S23/S1 < 1/135", F(768 * 97**2, H) < F(1, 135))
    check("coefficient of log(q) < 1.63",
          F(9, 8) + F(1, 2 * H) + F(68, 135) < F(163, 100))
    check("log(1000) < 7", 3 * F(2303, 1000) < 7)
    check("2 log(N)/(25 M) < 1/1000 for N >= 1000",
          F(2 * 7, 25 * 10_000) < F(1, 1000))
    check("remaining determinant terms < 23",
          9 * F(2303, 1000) + F(2, 25)
          + F(136, 135) * F(52, 25) + F(1, 1000) < 23)

    delta_lower = (F(88, 15) - F(163, 100) - F(230, 177)) / 576
    check("determinant zero bound > 0.00509",
          delta_lower > F(509, 100_000))

    harmonic = sum((F(1, n*n) for n in range(1, 31)), F(0))
    check("sum_{n=1}^{30} 1/n^2 > 1.612", harmonic > F(1612, 1000))
    lower, upper = exp_bounds(F(1), terms=6)
    check("e > 19/7", lower > F(19, 7))
    gaussian_tail = F(7, 19)**5 / (1 - F(7, 19)**15)
    check("Gaussian tail < 0.007", gaussian_tail < F(7, 1000))

    theta_certificate = (
        F(7, 11) * (1 - F(2, 7000)) * (1 - F(18, 7000))
        * (F(1612, 1000) - F(1320, 49000) - F(7, 1000))
    )
    check("theta certificate equals stated exact fraction",
          theta_certificate == F(37_781_022_837, 37_730_000_000))
    check("theta certificate > 1", theta_certificate > 1)
    check("sqrt(50,000,000) > 7071", 7071**2 < q0)
    delta_upper = 2 * F(1773, 100) / 7071
    check("theta zero bound < 0.00502", delta_upper < F(502, 100_000))
    check("strict contradiction", delta_upper < F(502, 100_000)
          < F(509, 100_000) < delta_lower)

    print("\nAll exact arithmetic checks passed.")
    print("Conditional analytic cutoff: q < 50,000,000.")
    print("Improvement over 10^10:", 10**10 // q0)
    print("External lemmas and analytic deductions are not checked by this program.")


if __name__ == "__main__":
    main()
