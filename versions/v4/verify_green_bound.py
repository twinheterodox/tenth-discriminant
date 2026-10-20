#!/usr/bin/env python3
"""Exact arithmetic certificate for the q < 4000 derivative-determinant draft.

Only integers and fractions are used for decisions. The certificate checks
constants, parameter inequalities, and the final uniform numerical gap. It
does not formally verify the general determinant or analytic arguments.
Optional finite checks exercise the valuation formulas and derivatives.
"""

import argparse
from fractions import Fraction as F
from functools import lru_cache
from math import comb, factorial, isqrt

Q0 = 4000
H = 50
C_THETA = F(12703, 12500)


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


def arithmetic_certificate():
    check = Checks()
    r0 = Q0**4
    log_low, log_high = F(8294049, 10**6), F(165881, 20000)
    sqrt_low = F(63245553, 10**6)
    lq, uq = log_bounds(Q0)
    check('8.294049 < log(4000) < 8.294050', log_low < lq <= uq < log_high)
    check('sqrt(4000) > 63.245553 > 60', 60 < sqrt_low and sqrt_low**2 < Q0)
    check('log(q) > 8 throughout the excluded range', log_low > 8)

    rho = F(1)
    positive = signed = F(1)
    for p in (2,3,5,7):
        rho *= 1-F(1,p*p)
        positive *= 1+F(1,p)
        signed *= 1-F(1,p)
    check('primitive density 768/1225', rho == F(768,1225))
    check('boundary constants 88/35 and 192/35',
          positive-signed == F(88,35) and 2*positive == F(192,35))
    check('pi*rho/4 < 0.4926, using pi < 22/7', F(22,7)*rho/4 < F(2463,5000))
    l4,u4 = log_bounds(4)
    check('2 log(4)+2 < 4.773', 2*u4+2 < F(4773,1000))
    check('log(4)^2+2 log(4) > 4.694', l4*l4+2*l4 > F(2347,500))
    check('log(4)-1 > 0.386', l4-1 > F(193,500))

    p319 = primes_up_to(319)
    p50 = primes_up_to(H)
    a319_low = sum((log_bounds(p)[0]/p for p in p319), F(0))
    l319,u319 = log_bounds(319)
    b0_upper = u319-a319_low+1/(2*l319)
    check('prime-sum constant B0 < 1.334', b0_upper < F(667,500))
    check('A_pr(x) < 2 log(x) for x >= 2 follows from the theta estimate',
          C_THETA < 2 and C_THETA < 2*log_bounds(2)[0])
    a50_upper = sum((log_bounds(p)[1]/p for p in p50), F(0))
    theta50_low = sum((log_bounds(p)[0] for p in p50), F(0))
    theta50_high = sum((log_bounds(p)[1] for p in p50), F(0))
    w50_low = sum(((F(1,50)-F(p,7500))*log_bounds(p)[0] for p in p50), F(0))
    check('A(50) < 2.77035', a50_upper < F(55407,20000))
    check('40.9602 < theta(50) < 41', F(204801,5000) < theta50_low <= theta50_high < 41)
    check('small-prime determinant contribution W > 0.6732', w50_low > F(1683,2500))
    check('every prime <= 50 is inert under the class-number-one hypothesis', 4*H < Q0)
    check('largest prime <= 50 is 47', max(p50) == 47)

    b_tail = 2*C_THETA/H-F(204801,5000)/(H*H)
    check('tail bound B < 0.02426552 (equality for our rational upper bound)',
          b_tail == F(303319,12500000))

    # Grid rounding: both unrounded side lengths exceed q^(3/2) >= 240000.
    rounding = F(10001,10000)
    check('ceil rounding factor < 1.0001', 1+F(1,240000) < rounding)
    check('grid cardinality n <= 3R', F(9,4)*rounding**2 < 3)
    check('grid side A <= 2 q^(9/4)', (rounding*F(3,2))**2 < 8)
    check('grid norm T < R', rounding*F(3,4) < 240000)
    check('R/S <= 50.001', r0 >= 2_500_050)
    check('J is positive and J <= 2R+A', r0 > 55 and F(1,55) < 2)
    check('coefficient margin in the rank condition is 1/1100',
          F(9,220)-F(1,25) == F(1,1100))
    check('nJ > 2RS + A(R+S) uniformly for q >= 4000',
          F(9,4*r0)+F(51,25*240000) < F(1,1100))
    check('R >= 319 and R >= q/4', r0 > 319 and Q0**3 > F(1,4))
    check('log(6) < 2 for the Gram norm prefactor', log_bounds(6)[1] < 2)

    # L/q^4 and (2+8L)/q^4 decrease for L >= 8.
    check('Gram norm prefactor contributes < 10^-6', (2+8*log_high)/r0 < F(1,10**6))
    check('large-prime floor loss contributes < 10^-6',
          F(50001,1000)*4*log_high/r0 < F(1,10**6))
    check('small-prime floor loss contributes < 10^-6', F(82,r0) < F(1,10**6))
    check('all rounding and prefactor losses fit in 0.001',
          F(1,10000)+3*F(1,10**6) < F(1,1000))
    l43,_ = log_bounds(F(4,3))
    check('log(4/3) > 0.28768', l43 > F(899,3125))
    beta = F(541,550)
    delta = F(3611,2200)
    check('Archimedean coefficients beta and delta',
          beta == 1+F(1,50)-F(2,55)
          and delta == 4-(F(8,55)+F(9,4)*beta))
    k_upper = (F(667,500)+F(55407,20000)+C_THETA
               +F(16667,1000)*b_tail-F(1683,2500)
               -beta*F(899,3125)+F(1,1000))
    check('0 < K < 4.570', 0 < k_upper < F(457,100))

    # These inequalities prove all nonconstant terms in the final RHS
    # decrease as functions of L for L >= 8, as explained in the paper.
    c1,c2,c3 = F(4773,1000),F(2347,500),F(193,500)
    check('split main term positive and decreasing for L >= 8',
          15*8+c1-c2/8 > 0
          and 15+c2/64-(15*8+c1-c2/8)/2 < 0)
    check('split boundary terms positive and decreasing for L >= 8',
          1-c3/8 > 0 and c3/64-(1-c3/8)/2 < 0)
    bq = F(88,35)+F(192,35)/sqrt_low
    split_over_log_upper = (
        F(2463,5000)*(15*log_high+c1-c2/log_high)/sqrt_low
        +2*bq*(1-c3/log_high)/sqrt_low
    )
    rhs = split_over_log_upper+F(4,Q0)+k_upper/log_low+1/(8*log_low**2)
    check('determinant coefficient > 1.641', delta > F(1641,1000))
    check('necessary right side < 1.634', rhs < F(817,500))
    check('strict uniform contradiction gap > 0.007', delta-rhs > F(7,1000))
    print(f'\nAll {check.count} exact arithmetic checks passed.')
    print('Exact rational contradiction gap:', delta-rhs)
    print('Analytic cutoff established by the accompanying argument: q < 4000.')
    return check.count


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


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--sanity',action='store_true')
    args=parser.parse_args()
    arithmetic_certificate()
    if args.sanity:
        print('\nFinite sanity checks:')
        sanity_checks()
    print('\nIndependent mathematical review remains pending.')
