#!/usr/bin/env python3
"""Exact rational certificate for the v7 uniform exclusion q >= 2000.

Checks the numerical constants of Section 7 of proof.tex. Only the Python
standard library and the interval utilities included in this directory
are used. The general mathematical deductions are proved in the paper.
"""
import json
import sys
from fractions import Fraction as F
from math import isqrt
from pathlib import Path

ROOT = Path(__file__).resolve().parent
from exact_arithmetic import I, PI, ln, power

CHECKS = []
VALUES = {}


def check(condition, label):
    if not condition:
        raise AssertionError(label)
    CHECKS.append(label)


def record(name, value):
    x = I(value)
    VALUES[name] = {'lower': str(x.lo), 'upper': str(x.hi)}
    return x


def sqrt(value):
    x = I(value)
    scale = 10**60
    def root(y):
        return isqrt(y.numerator * scale * scale // y.denominator)
    return I(F(root(x.lo), scale), F(root(x.hi) + 1, scale))


def log_interval(value):
    x = I(value)
    return I(ln(x.lo).lo, ln(x.hi).hi)


def primes_to(n):
    flags = bytearray(b'\x01') * (n + 1)
    flags[:2] = b'\x00\x00'
    for p in range(2, isqrt(n) + 1):
        if flags[p]:
            flags[p*p:n+1:p] = b'\x00' * ((n-p*p)//p + 1)
    return [p for p in range(2, n+1) if flags[p]]


def run():
    q0 = 2000
    M = q0*q0
    eps = F(1, M)
    t, C, tau = F(3, 64), F(27, 64), F(3, 10)
    e, b0 = F(33, 10000), F(2193, 20000)
    kappa = F(3, 2)
    ct = F(12703, 12500)
    L, m = ln(q0), ln(M)
    u, v = sqrt(q0), sqrt(F(q0, 4))
    rho = sqrt(1+v*v)/2
    r0 = sqrt(C*M*v/PI)
    check((rho/r0).hi < e, 'uniform disk relative error < 0.0033 at q=2000')
    check((2*(r0+rho)/M).hi < 1, 'distinct nodes modulo the auxiliary prime')
    check((r0+rho).lo > 1 and rho.lo > 1, 'radius and covering-radius hypotheses')
    check(L.lo > F(38, 5), 'log q >= log 2000 > 7.6')
    check((m-ln(33)).lo > ln(563).hi, 'ordinary-prime estimates cover all floor intervals')
    check(C/9 == t, 'disk count times derivative multiplicity covers all rows')

    # Only the 210 condition is used to find the auxiliary inert prime.
    # The expression on the right bounds the split-prime weight uniformly
    # for q>=q0 and q^2<=U<=kappa*q^3; see the monotonicity proof in the note.
    density = F(768, 1225)
    aa = PI*density/(2*u)
    bb = PI/4*sqrt(1+F(4, q0))*F(96, 35)
    cc = 2*PI*(v+1/v)
    ell = 3*L + 2*ln(kappa)
    sieve_cost = ell*(aa*(kappa-1) + bb*(1+sqrt(kappa))/q0 + cc/(q0*q0))
    sieve_margin = record('auxiliary_prime_margin', kappa*(1-1/(2*m))-ct-sieve_cost)
    check(sieve_margin.lo > F(116, 1000), 'auxiliary-prime weight margin > 0.116')

    # The existing v6 determinant inequalities, specialized uniformly to
    # R>=q^2, with no norm-prime subtraction and no factorial feedback yet.
    nu = C*(1+2*e)**2
    check(b0 <= (t-eps)/nu, 'b0 <= S/n uniformly')
    j = F(1, 9)+eps
    jstar = j-b0/2+b0*eps
    alpha, beta = (1-t)/2-jstar, 1+t-2*jstar
    record('alpha', alpha)
    record('beta_over_four', beta/4)
    check(alpha > F(21, 50), 'base slope exceeds 0.42')
    check(0 < beta/4 < F(117, 500), 'base log-q cost is below 0.234')

    a = 2*tau
    part = j*j/(2*a)-j**3/(3*(a-1))+j**4/(12*(a-2))
    part -= 2*power(j, a+2)/(a*(a-1)*(a-2)*(a+1)*(a+2))
    K = j*2*tau*tau/(2*tau+1)-(1-tau)*part+j/2-3*j*j/4
    K += (1-j)**2*ln(1-j)/2+j**3/6-j**4/24
    B = (1-tau)*j*(1-ln(j))
    I0 = 2*tau*tau/(2*tau+1)
    joint = -3*tau/2 + 2*nu/(t-eps)*(K+j*(B+5*e/(3*(1+e)))+eps*(I0+B))-2*B
    delta = j*C/(t-eps)*((1+2*e)**2+e/(2+e))-1
    check(e <= delta < 1, 'radius-factor saving hypotheses')
    gs = (t-eps)*(F(1, 4)-delta+3*delta*delta/4-delta*delta*ln(delta)/2)+eps*ln(delta)/2
    check(gs.lo > 0, 'positive additional radius saving')
    record('joint_size_constant', joint)
    record('additional_radius_saving', gs)
    g = (ln(C)-ln(2)-log_interval(PI))/2+ln(1+e)

    ps = primes_to(10000)
    logs = {p: ln(p) for p in ps}
    small = [p for p in ps if p <= 21]
    theta = sum((logs[p] for p in small), I(0))
    ah = sum((logs[p]/p for p in small), I(0))
    wh = sum((logs[p]*(t-F(p, 3)*t*t) for p in small), I(0))
    bh = sum((logs[p]/p**2 for p in ps if p > 21), I(0))
    bh += 2*ct/10000-sum(logs.values(), I(0))/10000**2
    mertens = ln(319)-sum((logs[p]/p for p in ps if p <= 319), I(0))+1/(2*ln(319))
    check(mertens.hi < F(667, 500), 'ordinary-prime sum constant < 1.334')
    h32 = sum((F(1, n) for n in range(1, 33)), F(0))
    fa, fb = (ln(33)-h32-F(1, 33)+1)/2, (h32-ln(33))/2
    floor_gain = fb*(1-1/(2*(m-ln(33))))-fa*ct
    check(floor_gain.lo > 0, 'positive floor-remainder gain')

    # These primes are inert for every q>=2000. Use only this fixed list.
    small_gain, residual_gain, coupling_gain = I(0), I(0), I(0)
    for p in ps:
        if p >= 500:
            break
        pp = p*p
        while pp < M:
            small_gain += logs[p]*max(F(0), (b0-eps)/pp-2*eps)
            pp *= p
        small_gain += logs[p]*max(F(0), (t-eps)/(p*p)-3*eps)
        ap = F(1, 2*p*p)-t/(2*p)+t*t/6 if p*t <= 1 else 1/(6*t*p**3)
        residual_gain += logs[p]*max(F(0), 2*ap/p-(2+F(2, p**3))*eps)
        coupling_gain += 2*logs[p]*max(F(0), (1-F(1, p))*(ap-(1+F(1, p*p))*eps-jstar)-eps)

    cost = ah-wh+ct+bh/(3*(t-eps))+beta*g+joint+2*m/M-gs
    cost += 2*theta/M+m/((t-eps)*M)+2*(ln(t)+2*m)/M+F(667, 500)+1/(2*m)
    cost -= floor_gain+small_gain+residual_gain+coupling_gain
    record('floor_gain', floor_gain)
    record('small_prime_gain', small_gain)
    record('residual_gain', residual_gain)
    record('coupling_gain', coupling_gain)
    record('quadratic_prime_tail', bh)
    record('base_cost', cost)
    check(cost.hi < F(2211, 1000), 'base cost < 2.211 < 2.22')
    check((ln(t)+2*m).lo > 2, 'decreasing determinant rounding errors')

    # First transfer the zero-feedback estimate to real scales; then use
    # just ONE previously established factorial refinement, pointwise in q.
    A, Bq, K0, K1 = F(21, 50), F(117, 500), F(111, 50), F(12, 5)
    check((K0+A*ln(kappa)).hi < K1, 'transfer cost < 2.4')
    z, h = F(109, 1000), F(23, 500)
    check(z < b0-eps and h < t-eps, 'safe column and row factorial scale fractions')
    check(min(z, h)*q0 > kappa, 'factorial scales lie above the transferred interval start')
    check(max(z, h) < kappa, 'factorial scales lie below the transferred interval end')
    check((L/q0).hi < F(1, 250), 'ramified subtraction < 0.004 for q>=2000')
    for f in (z, h):
        check(((3*A-Bq)*L+A*ln(f)-K1-F(1, 250)).lo > 0,
              f'positive previously proved factorial bound at scale fraction {f}')
    refined_cost = K0+K1*(z+h)-A*(z*ln(z)+h*ln(h))+h*F(1, 250)
    record('refined_cost', refined_cost)
    check(refined_cost.hi < F(137657, 50000), 'refined cost < 2.75314 < 2.76')
    check((3*A-Bq)*(1+z+h) > F(237, 200), 'refined main coefficient exceeds 1.185')

    # Smooth norm upper bound, reduced to a scalar decreasing function.
    log4, logk = ln(4), ln(kappa)
    linear = 6*logk+2*log4-F(14, 5)
    constant = logk*logk-log4*log4-2*log4-F(8, 5)*logk+F(8, 5)
    check((PI*density/4).hi < F(2463, 5000), 'primitive norm density < 0.4926')
    check(linear.hi < F(1203, 500), 'norm-bound linear coefficient < 2.406')
    check(constant.hi < -F(1789, 500), 'norm-bound constant < -3.578')
    check((log4-1).lo > F(193, 500), 'log 4 - 1 > 0.386')
    check((3-2*sqrt(2)).hi < F(1, 5), 'floor weight f(u) <= 1 - (4/5)u')
    # Elementary derivative bounds hold uniformly for L>=7.6.
    Lmin = F(38, 5)
    first_deriv = 8+F(1789, 500)/Lmin**2-4*Lmin-F(1203, 1000)+F(1789, 1000)/Lmin
    boundary_deriv = F(193, 500)/Lmin**2-F(1, 2)*(1-F(193, 500)/Lmin)
    check(first_deriv < 0, 'first normalized norm term decreases for log q>=7.6')
    check(boundary_deriv < 0, 'both boundary terms decrease for log q>=7.6')
    right = F(2463, 5000)/u*(8*L+F(1203, 500)-F(1789, 500)/L)
    right += 2/u*(F(88, 35)+F(192, 35)/u)*(1-F(193, 500)/L)+F(1, q0)+F(69, 25)/L
    record('normalized_upper_at_2000', right)
    gap = record('normalized_contradiction_gap', F(237, 200)-right)
    check(right.hi < F(233331, 200000), 'normalized necessary upper bound < 1.166655 < 1.167 at q=2000')
    check(gap.lo > F(18, 1000), 'uniform normalized contradiction gap > 0.018')
    out = {'status': 'all numerical inequalities passed; mathematical derivation is separate',
           'checks': CHECKS, 'values': VALUES,
           'scope': 'Uniform exclusion q >= 2000; the separate interval certificate covers 570 <= q <= 2000'}
    (ROOT/'tail_checks.json').write_text(json.dumps(out, indent=2)+'\n')
    print(f'PASS: {len(CHECKS)} exact interval checks')
    for key in ('auxiliary_prime_margin', 'base_cost', 'refined_cost',
                'normalized_upper_at_2000', 'normalized_contradiction_gap'):
        vals = VALUES[key]
        print(key, 'in', float(F(vals['lower'])), float(F(vals['upper'])))
    print('Decimals above are displays only; all acceptance comparisons use rational endpoints.')


if __name__ == '__main__':
    run()
