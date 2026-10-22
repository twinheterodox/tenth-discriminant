"""Exact rational checks of the historical adaptation's numerical constants.

No floating-point arithmetic, parameter search, special-function library,
earlier-version code, or downloaded data is used. These inequalities support
the written mathematical proof; they do not constitute a formal proof of it.
"""

from fractions import Fraction as F


def log_unit_interval(y):
    """Enclose log(y) for 1 <= y <= 2 by a positive series and its tail."""
    assert 1 <= y <= 2
    t = (y - 1) / (y + 1)
    lower = 2 * sum((t ** (2*j + 1) / (2*j + 1) for j in range(16)), F(0))
    tail = 2 * t**33 / (33 * (1 - t*t))
    return lower, lower + tail


def log_interval(x):
    y, shift = F(x), 0
    assert y >= 1
    while y > 2:
        y /= 2
        shift += 1
    lo, hi = log_unit_interval(y)
    two_lo, two_hi = log_unit_interval(F(2))
    return lo + shift*two_lo, hi + shift*two_hi


def main():
    # Every logarithmic input used in the written proof.
    for x, lo, hi in [(2, F(69, 100), F(7, 10)),
                      (3, F(1), F(11, 10)),
                      (10, F(2), F(5, 2))]:
        lower, upper = log_interval(x)
        assert lo < lower <= upper < hi
        print(f"log({x}) in ({lo}, {hi})")

    # arctan(x) < x - x^3/3 + x^5/5 for 0 < x < 1.
    pi_upper = 4 * sum((x - x**3/3 + x**5/5
                        for x in [F(1, 2), F(1, 3)]), F(0))
    assert pi_upper < F(16, 5)
    print("pi < 16/5")

    # The short series bounds printed in the appendix.
    assert F(69, 100) < F(56, 81)
    assert F(2, 3) + 2*F(1, 3)**3/(3*(1-F(1, 9))) == F(25, 36) < F(7, 10)
    assert 1 + F(1, 12) + F(1, 60) == F(11, 10)
    assert pi_upper == F(6115, 1944)
    print("short rational bounds printed in Appendix A checked")

    # The power-of-two endpoint needs only the bounds for log(2).
    q0 = 32768
    assert q0 == 2**15 and 180**2 < q0
    Llo, Lhi = 15*F(69, 100), 15*F(7, 10)
    assert Llo == F(207, 20) and Lhi == F(21, 2)
    assert Lhi/180 == F(7, 120)
    assert Llo - 2*F(7, 10) > 2  # log(q/4) > 2
    print("207/20 < log(32768) < 21/2; sqrt(32768) > 180")
    print("uniformly for q >= 32768: log(q)/sqrt(q) < 7/120")

    # Sum over 2 and the odd integers, using a half-integral tail.
    B = F(7, 40) + F(5, 18)*F(11, 10) + F(1, 6)
    assert B == F(233, 360) < F(2, 3)
    assert F(3, 2) + F(13, 3)*F(2, 3) == F(79, 18)
    assert F(79, 18) + F(7, 3) == F(121, 18)
    print(f"prime-square sum < {B} < 2/3")

    # The weighted interval (q^4,q^5] contains an inert prime.
    aux_first = F(23, 6)/Llo
    aux_second = F(4, 5*180)*(9*Lhi+8)
    aux_tail = 2*(4+1/Llo)/(180*q0*q0)
    assert aux_first == F(10, 27)
    assert aux_second == F(41, 90)
    assert aux_tail < F(1, 1000)
    assert aux_first + aux_second + F(1, 1000) < F(5, 6) < 1
    print("auxiliary-prime inequality < 10/27 + 41/90 + 1/1000 < 5/6")

    # Bounds behind the unshifted grid and floor/ceiling estimates.
    assert 11*q0 > 25                    # |omega| <= 3u/5
    assert q0**7 > 100**2                # q^4 > 100 sqrt(q)
    assert q0**4 > 10**16 > 156
    assert F(8, 5) + F(8, 50) == F(44, 25) < 2
    assert F(13, 12) - F(1, 24) == F(25, 24)
    assert F(25, 48) + F(1, 24) == F(9, 16)
    print("rectangular grid and determinant coefficients checked")

    # log(10)<5/2 gives log(10^16)<40.
    first_error = (5*Lhi+4)/q0
    second_error = (F(25, 2)*40+F(39, 4))/10**16
    assert first_error == F(113, 65536)
    assert second_error == F(2039, 4*10**16)
    assert first_error + second_error < F(1, 500)
    assert F(25, 24)*F(7, 10) == F(35, 48)
    assert F(121, 18) + F(35, 48) + F(1, 500) < F(15, 2)
    print("all boundary and rounding errors < 1/500; G(log R) < 15/2")

    # Concavity reduces the interval to its smaller endpoint, 4L.
    assert F(7, 16) - F(36, 5)*F(7, 120) == F(7, 400) > 0
    assert F(7, 4) - F(25, 96) == F(143, 96)
    endpoint = F(64, 5)*F(7, 120) + F(15, 2)/Llo
    assert endpoint == F(56, 75)+F(50, 69) == F(846, 575)
    assert endpoint < F(143, 96)
    margin = F(143, 96)-endpoint
    assert margin == F(1009, 55200)
    print(f"final endpoint < {endpoint} < 143/96; margin {margin}")
    print("PASS: all numerical constants; the uniform argument is in proof.tex.")


if __name__ == "__main__":
    if not __debug__:
        raise RuntimeError("Run without Python -O or -OO.")
    main()
