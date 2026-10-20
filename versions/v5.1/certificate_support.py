"""Elementary certificate helpers and retained finite determinant checks.
Adapted from independently verified v4. The general proof is in proof.tex;
these finite cases are not an independent mathematical review of v5.
"""
from fractions import Fraction as F
from functools import lru_cache
from math import comb, factorial, isqrt

class Checks:
    def __init__(self):
        self.count = 0

    def __call__(self, label, condition):
        if not condition:
            raise AssertionError(label)
        self.count += 1
        print('PASS:', label)


def atanh_log_bounds(y, terms=60):
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


def primes_up_to(n):
    return [p for p in range(2, n+1)
            if all(p % d for d in range(2, isqrt(p)+1))]


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


def derivative_value(r,s,j,z,q):
    if j>r:
        return (0,0)
    conjugate=(z[0]+z[1],-z[1])
    value=mul(power(z,r-j,q),power(conjugate,s,q),q)
    coeff=factorial(r)//factorial(r-j)
    return coeff*value[0],coeff*value[1]


def sanity_checks():
    check=Checks()
    cases=0
    for rsize in range(2,38):
        for ssize in range(2,12):
            for p in primes_up_to(19):
                direct=sum(min(r//p,ssize-1-s)
                           for r in range(rsize) for s in range(ssize))
                layered=sum((ssize-h)*max(rsize-p*h,0)
                            for h in range(1,ssize))
                coeff=F(2*direct,rsize*rsize*ssize)
                lower=(1-F(rsize-1,2*rsize*ssize))/p-F(1,rsize)
                lower-=F((rsize-1)*(2*rsize-1),6*rsize*ssize*p*p)
                assert direct==layered and coeff>=lower
                if p*(ssize-1)<=rsize-1:
                    small=F(ssize-1,rsize)-F(p*(ssize*ssize-1),3*rsize*rsize)
                    assert coeff==small
                cases+=1
    check(f'exact valuation sums and tail inequalities in {cases} finite cases', True)

    cases=0
    for q in (3,7,11,19,43,67,163):
        for p in primes_up_to(7):
            inert=(q%8==3) if p==2 else pow((-q)%p,(p-1)//2,p)==p-1
            if not inert:
                continue
            for r in range(10):
                for s in range(5):
                    h=min(r//p,4-s)
                    for j in range(12):
                        for z in ((0,0),(1,0),(0,1),(-2,1),(3,-2)):
                            a=b=0
                            for i in range(h+1):
                                u,v=derivative_value(r-p*i,s+i,j,z,q)
                                coeff=(-1)**i*comb(h,i)
                                a+=coeff*u; b+=coeff*v
                            assert a%p**h==b%p**h==0
                            cases+=1
    check(f'Frobenius row transformations, including p=2 and high derivatives, in {cases} cases',True)
    print('Finite cases check implementation and identities; they do not replace the proof.')
