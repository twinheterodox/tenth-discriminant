#!/usr/bin/env python3
"""Exact rational intervals, adapted from v5 with higher precision.
Standard library only; every elementary operation rounds outward.
"""
from fractions import Fraction as F
from functools import lru_cache
from math import factorial
from certificate_support import log_bounds

SCALE = 10**65


def down(x):
    return F((x*SCALE).__floor__(), SCALE)


def up(x):
    return F((x*SCALE).__ceil__(), SCALE)


class I:
    """Outward-rounded rational interval, with 65 decimal places."""
    def __init__(self, lo, hi=None):
        if isinstance(lo, I):
            self.lo, self.hi = lo.lo, lo.hi
        else:
            self.lo, self.hi = down(F(lo)), up(F(lo if hi is None else hi))
        assert self.lo <= self.hi

    def __add__(self, other):
        o = I(other)
        return I(self.lo+o.lo, self.hi+o.hi)
    __radd__ = __add__

    def __neg__(self):
        return I(-self.hi, -self.lo)

    def __sub__(self, other):
        return self+-I(other)

    def __rsub__(self, other):
        return I(other)+-self

    def __mul__(self, other):
        o = I(other)
        vals = [a*b for a in (self.lo, self.hi) for b in (o.lo, o.hi)]
        return I(min(vals), max(vals))
    __rmul__ = __mul__

    def __truediv__(self, other):
        o = I(other)
        assert o.lo*o.hi > 0
        return self*I(1/o.hi, 1/o.lo)

    def __rtruediv__(self, other):
        return I(other)/self

    def __pow__(self, n):
        assert isinstance(n, int)
        if n < 0:
            return (1/self)**(-n)
        out = I(1)
        while n:
            if n & 1:
                out *= self
            self *= self
            n //= 2
        return out


@lru_cache(None)
def ln(x):
    return I(*log_bounds(F(x)))


def exp_exact(x):
    """Enclose exp of a rational by a positive series and range reduction."""
    x = F(x)
    if x < 0:
        return 1/exp_exact(-x)
    k = 0
    while x > 1:
        x /= 2
        k += 1
    # Rounded interval recurrence avoids very large intermediate rational
    # denominators. Every rounding is outward; no float is involved.
    term = total = I(1)
    xi = I(x)
    for n in range(1, 81):
        term = term*xi/n
        total += term
    # Here 0 <= x <= 1. The positive tail beginning at n=81 is at
    # most (1/81!)/(1-1/82), independently of rounding in xi.
    tail = F(82, 81*factorial(81))
    return (total+I(0, tail))**(2**k)


def exp(x):
    x = I(x)
    return I(exp_exact(x.lo).lo, exp_exact(x.hi).hi)


@lru_cache(None)
def power(x, s):
    return exp(ln(F(x))*F(s))


def arctan(x):
    x = F(x)
    terms = 60
    partial = sum(((-1)**k*x**(2*k+1)/(2*k+1)
                   for k in range(terms)), F(0))
    # Sixty terms end with a negative term.
    return I(partial, partial+x**(2*terms+1)/(2*terms+1))


PI = 16*arctan(F(1, 5))-4*arctan(F(1, 239))

