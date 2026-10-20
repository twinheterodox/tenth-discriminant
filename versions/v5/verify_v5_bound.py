#!/usr/bin/env python3
"""Rational interval certificate for the v5 bound q < 2000.

No floating-point operations or third-party libraries are used in acceptance
decisions. The general mathematical arguments are proved in proof.tex.
The independently verified v4 paper is cited for the range q >= 4000.
"""
import argparse
from fractions import Fraction as F
from functools import lru_cache
from math import factorial, gcd, isqrt
from certificate_support import Checks, log_bounds, primes_up_to, sanity_checks

SCALE = 10**45


def down(x):
    return F((x*SCALE).__floor__(), SCALE)


def up(x):
    return F((x*SCALE).__ceil__(), SCALE)


class I:
    """Outward-rounded rational interval, with 45 decimal places."""
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
    total = sum((x**n/F(factorial(n)) for n in range(81)), F(0))
    tail = x**81/F(factorial(81))/(1-x/82)
    return I(total, total+tail)**(2**k)


def exp(x):
    x = I(x)
    return I(exp_exact(x.lo).lo, exp_exact(x.hi).hi)


def power(x, s):
    return exp(ln(F(x))*F(s))


def arctan(x):
    x = F(x)
    terms = 40
    partial = sum(((-1)**k*x**(2*k+1)/(2*k+1)
                   for k in range(terms)), F(0))
    # Forty terms end with a negative term.
    return I(partial, partial+x**(2*terms+1)/(2*terms+1))


PI = 16*arctan(F(1, 5))-4*arctan(F(1, 239))


@lru_cache(None)
def zeta(s):
    """Euler--Maclaurin enclosures for zeta(s) and its derivative, s>1.

    N=64, four Bernoulli correction terms. Both remainders are bounded
    from the periodic Bernoulli integral, including its s derivative.
    """
    s = F(s)
    assert s > 1
    N, m = 64, 4
    val = sum((power(n, -s) for n in range(1, N)), I(0))
    der = -sum((ln(n)*power(n, -s) for n in range(1, N)), I(0))
    term = power(N, 1-s)/(s-1)
    val += term
    der -= term*(ln(N)+1/(s-1))
    term = power(N, -s)/2
    val += term
    der -= term*ln(N)
    bern = [F(1, 6), F(-1, 30), F(1, 42), F(-1, 30)]
    for k, bk in enumerate(bern, 1):
        rising = F(1)
        h = F(0)
        for j in range(2*k-1):
            rising *= s+j
            h += 1/(s+j)
        term = power(N, 1-s-2*k)*(bk*rising/F(factorial(2*k)))
        val += term
        der += term*(h-ln(N))
    rising = F(1)
    h = F(0)
    for j in range(2*m):
        rising *= s+j
        h += 1/(s+j)
    err = power(N, 1-s-2*m)*(abs(bern[-1])*rising /
                             (factorial(2*m)*(s+2*m-1)))
    derr = err*(h+ln(N)+1/(s+2*m-1))
    return (val+I(-err.hi, err.hi), der+I(-derr.hi, derr.hi))


def integral_constants(delta):
    """C(s)=sqrt(pi) Gamma(s-1/2)/Gamma(s), g(s)=-C'(s)/C(s).

    The log-Gamma expansion is taken to degree 10. Its tails are bounded
    by geometric series using 1 < zeta(n) < 2, n >= 2.
    """
    d = F(delta)
    log_ratio = -2*ln(2)*d
    g = 2*ln(2)
    nmax = 10
    for n in range(2, nmax+1):
        zn = zeta(F(n))[0]
        log_ratio += zn*((-1)**n*F(2**n-2, n)*d**n)
        g += zn*((-1)**(n+1)*(2**n-2)*d**(n-1))
    tail = 2*(2*d)**(nmax+1)/(1-2*d)
    log_ratio += I(-tail, tail)
    g += I(-tail/d, tail/d)
    return PI*exp(log_ratio), g


def v5_certificate():
    check = Checks()
    q0, q1, M = 2000, 4000, 50_000_000
    d, s = F(1, 70), F(71, 70)
    t, j, C, eta = F(1, 110), F(1, 160), F(16, 5), F(2001, 2000)
    beta = 1+t-2*j
    alpha = 1-(1+t)/2-j
    check('Mellin parameters and positive coefficient beta',
          beta == F(877, 880) and alpha == F(861, 1760))
    check('2000 <= q <= 4000 implies 44 < sqrt(q) < 64',
          44**2 < q0 and 64**2 > q1)
    check('all primes <= 110 are inert throughout this interval', 4*110 < q0)
    # Grid sides sqrt(C R sqrt(q)/2), sqrt(2 C R/sqrt(q)).
    check('both unrounded grid sides exceed 2000',
          C*M*44/2 > 2000**2 and 2*C*M/64 > 2000**2)
    check('n < 4R and grid zero-count constant A/R < 0.00144',
          C*eta**2 < 4 and eta**2*C*64/(2*M) < F(144, 100000)**2)
    check('strict nonsingularity condition uniformly for all R >= M',
          C*j-2*t > C/M+F(144, 100000)*(1+t))
    check('T/R < 0.00102 < 1 throughout the interval',
          eta**2*C*64/(4*M) < F(102, 100000)**2)
    check('S and J positive and R/S <= 110.001',
          M > 160 and F(M)/(F(M, 110)-1) < F(110001, 1000))
    check('log(eta) < 0.0005', ln(eta).hi < F(1, 2000))
    m = ln(M)
    check('Gram prefactor < 0.000001',
          (ln(F(1, 20))+2*m).hi/M < F(1, 10**6))
    check('mean-derivative residual 2j T/R plus prefactor < 0.00002',
          2*j*F(102, 100000)+F(1, 10**6) < F(1, 50000))

    ps = primes_up_to(10000)
    small = [p for p in ps if p <= 110]
    a = sum((ln(p)/p for p in small), I(0))
    theta = sum((ln(p) for p in small), I(0))
    W = sum((ln(p)*(t-F(p, 3)*t*t) for p in small), I(0))
    theta_n = sum((ln(p) for p in ps), I(0))
    ctheta = F(12703, 12500)
    a319 = sum((ln(p)/p for p in ps if p <= 319), I(0))
    check('ordinary-prime constant is greater than -1.334',
          (ln(319)-a319+1/(2*ln(319))).hi < F(667, 500))
    check('A_pr(x) < 2 log(x) for every x >= 2 follows from theta',
          ctheta < 2 and ctheta < 2*ln(2).lo)
    tail = (sum((ln(p)/p**2 for p in ps if p > 110), I(0))
            +2*ctheta/10000-theta_n/10000**2)
    check('small-prime sum a_110 < 3.546874', a.hi < F(3546874, 10**6))
    check('theta(110) < 103 and W_110 > 0.759467',
          theta.hi < 103 and W.lo > F(759467, 10**6))
    check('prime-square tail b_110 < 0.00820476',
          tail.hi < F(820476, 10**8))
    check('small-prime floor loss < 0.000005', 2*F(103, M) < F(5, 10**6))
    check('large-prime floor loss < 0.00004',
          F(110001, 1000)*m.hi/M < F(4, 10**5))
    check('0.0001 absorbs both prime floor losses', F(45, 10**6) < F(1, 10000))
    arch_const = beta/2*ln(F(4, 5))+beta*ln(eta)-2*j+F(1, 50000)
    det_const = (F(3546874, 10**6)-F(759467, 10**6)+ctheta
                 +F(110001, 3000)*F(820476, 10**8)+arch_const+F(1, 10000))
    check('determinant constant C_* < 3.982', det_const.hi < F(1991, 500))

    # Euler summation on each horizontal line of the quadratic lattice.
    # At v=sqrt(q)/2 >= 22: zeta(3)<1.203, sum(log b)/b^3 < 1/4.
    z3, zp3 = zeta(F(3))
    check('zeta(3) < 1.203 and -zeta_prime(3) < 1/4',
          z3.hi < F(1203, 1000) and -zp3.lo < F(1, 4))
    check('s < 1.02 and derivative coefficients bounded by 11 and 19',
          s < F(51, 50) and 4*s*s+6*s < 11 and 10+8*s < 19)
    err_a = 11*PI/(24*22**3)*z3
    err_n = PI/(24*22**3)*((41+22*ln(22))*z3+22*(-zp3))
    check('uniform Epstein series error E_A < 0.0002', err_a.hi < F(1, 5000))
    check('uniform differentiated error E_N < 0.002', err_n.hi < F(1, 500))

    ci, gi = integral_constants(d)
    z1, zp1 = zeta(1+2*d)
    z2, zp2 = zeta(2+2*d)
    cc = -2*zp2/z2
    kappa = gi-2*zp1/z1-cc
    check('zeta(2s) > 1.6 and 0 < c < 1.2',
          z2.lo > F(8, 5) and 0 < cc.lo < cc.hi < F(6, 5))
    check('65 < kappa < 80', 65 < kappa.lo < kappa.hi < 80)
    check('rounded constants for the stated Euler-product bound',
          z2.lo > F(161893624, 10**8) and cc.hi < F(1090928, 10**6)
          and kappa.hi < F(69106001, 10**6))
    # These explicit rationals are the constants printed in the paper.
    kappaup = F(69106001, 10**6)
    ea, en = F(1, 5000), F(1, 500)
    A0 = F(161873624, 10**8)
    E0 = F(2219, 10**6)
    check('rounded denominator and error constants are conservative',
          A0 < z2.lo-ea and E0 > en+cc.hi*ea)
    F2000 = ci*z1*power(F(q0, 4), F(1, 2)-s)
    F4000 = ci*z1*power(F(q1, 4), F(1, 2)-s)
    check('3 < F(q) < 5 throughout 2000 <= q <= 4000',
          F4000.lo > 3 and F2000.hi < 5)
    check('1.6 < A0 < 1.7 and 0 < E0 < 0.003',
          F(8, 5) < A0 < F(17, 10) and 0 < E0 < F(3, 1000))
    check('6 < log(q/4) < 7 on the interval',
          ln(F(q0, 4)).lo > 6 and ln(F(q1, 4)).hi < 7)
    # V'(log q) = F/(A0+F) [1 - a(A0(ell+kappa)-E0)/(A0+F)].
    bracket_upper = 1-F(1, 2)*(F(8, 5)*71-F(3, 1000))/F(67, 10)
    vprime_upper = F(3, 8)*bracket_upper
    check('the upper prime bound has log-q derivative < -1',
          bracket_upper < 0 and vprime_upper/2 < -1)
    check('the lower prime bound has log-q derivative > -1/4', beta/4 < F(1, 4))
    check('ramification upper bound log(q)/q^s decreases', s*ln(q0).lo > 1)

    P = exp(-d*m)*(alpha*(m+1/d)-beta/4*ln(q0)
                   -F(1991, 500)-F(667, 500)-1/(2*m))
    U = (F2000*(ln(F(q0, 4))+kappaup)+E0)/(2*(A0+F2000))
    U += ln(q0)*power(q0, -s)
    check('Mellin lower bound P(2000) > 27.696', P.lo > F(3462, 125))
    check('Euler-product upper bound U(2000) < 27.679', U.hi < F(27679, 1000))
    check('new contradiction gap > 0.017', P.lo-U.hi > F(17, 1000))
    print(f'\nAll {check.count} new exact arithmetic checks passed.')
    print('Certified new gap exceeds 17/1000 on 2000 <= q <= 4000.')
    print('The cited, independently verified v4 paper excludes q >= 4000.')
    print('Analytic cutoff established by the accompanying argument: q < 2000.')
    return check.count


def primitive_euler_sanity():
    """Compare norm enumeration with Euler factors in five known fields."""
    limit = 2000
    ps = primes_up_to(limit)
    for q in (11, 19, 43, 67, 163):
        counted = [0]*(limit+1)
        counted[1] = 1  # The primitive rational unit ideal.
        for b in range(1, isqrt(4*limit//q)+1):
            radius = isqrt(limit)+b+1
            for a in range(-radius, radius+1):
                norm = a*a+a*b+((q+1)//4)*b*b
                if norm <= limit and gcd(a, b) == 1:
                    counted[norm] += 1
        product = [0]*(limit+1)
        product[1] = 1
        for p in ps:
            if p == 2:
                splitting = -1  # These five q are 3 modulo 8.
            elif p == q:
                splitting = 0
            else:
                splitting = 1 if pow((-q) % p, (p-1)//2, p) == 1 else -1
            if splitting == -1:
                continue
            before = product[:]
            prime_power = p
            while prime_power <= limit:
                factor = 1 if splitting == 0 else 2
                for n in range(1, limit//prime_power+1):
                    product[n*prime_power] += factor*before[n]
                if splitting == 0:
                    break
                prime_power *= p
        assert product == counted, q
    print('PASS: primitive Euler factors agree with direct norm enumeration '
          'in 10000 coefficients across five class-number-one fields.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--sanity', action='store_true')
    args = parser.parse_args()
    print('New v5 certificate:')
    new = v5_certificate()
    if args.sanity:
        sanity_checks()
        primitive_euler_sanity()
    print(f'\nTOTAL: {new} new exact arithmetic checks passed.')
    print('Independent mathematical review of v5 remains pending.')
