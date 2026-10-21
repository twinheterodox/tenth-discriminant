"""Exact logarithm enclosures and quadratic-ring arithmetic.
Adapted from the earlier certificates; no review status is implied.
"""
from fractions import Fraction as F
from functools import lru_cache

def atanh_log_bounds(y, terms=80):
    """For 1 <= y <= 2, bound log(y) using a positive series and its tail."""
    if not 1 <= y <= 2:
        raise ValueError('Expected 1 <= y <= 2')
    t = (y-1)/(y+1)
    total = 2*sum((t**(2*k+1)/F(2*k+1) for k in range(terms)), F(0))
    tail = 2*t**(2*terms+1)/((2*terms+1)*(1-t*t))
    return total, total+tail


@lru_cache(None)
def log_bounds(x):
    """Enclose log of a positive rational, with exact range reduction."""
    x = F(x)
    if x <= 0:
        raise ValueError('Positive argument required')
    if x < 1:
        lo, hi = log_bounds(1/x)
        return -hi, -lo
    k = 0
    while x >= 2:
        x /= 2
        k += 1
    lo, hi = atanh_log_bounds(x)
    l2, u2 = atanh_log_bounds(F(2))
    return lo+k*l2, hi+k*u2


def mul(x,y,q):
    a,b=x; c,d=y
    return a*c-((q+1)//4)*b*d, a*d+b*c+b*d


def power(x,n,q):
    result=(1,0)
    while n:
        if n & 1:
            result=mul(result,x,q)
        x=mul(x,x,q)
        n//=2
    return result

