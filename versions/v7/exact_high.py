"""Exact rational intervals for the concentrated-kernel certificate.

Euler--Maclaurin for zeta, and positive-real Stirling remainders for
log Gamma and psi. All acceptance arithmetic is integer/Fraction.
"""
from fractions import Fraction as F
from functools import lru_cache
from math import factorial,comb
from exact_arithmetic import I,PI,ln,exp,power

def bernoulli(nmax):
    bs=[F(1)]
    for n in range(1,nmax+1):
        bs.append(-sum(F(comb(n+1,k))*bs[k] for k in range(n))/(n+1))
    return bs

BERN=bernoulli(40)

@lru_cache(None)
def zeta(s):
    s=F(s);N=64;m=18
    assert s>1
    val=sum((power(n,-s) for n in range(1,N)),I(0))
    der=-sum((ln(n)*power(n,-s) for n in range(1,N)),I(0))
    term=power(N,1-s)/(s-1);val+=term;der-=term*(ln(N)+1/(s-1))
    term=power(N,-s)/2;val+=term;der-=term*ln(N)
    for k in range(1,m+1):
        rising=F(1);h=F(0)
        for j in range(2*k-1):rising*=s+j;h+=1/(s+j)
        term=power(N,1-s-2*k)*BERN[2*k]*rising/factorial(2*k)
        val+=term;der+=term*(h-ln(N))
    rising=F(1);h=F(0)
    for j in range(2*m):rising*=s+j;h+=1/(s+j)
    err=power(N,1-s-2*m)*abs(BERN[2*m])*rising/(factorial(2*m)*(s+2*m-1))
    derr=err*(h+ln(N)+1/(s+2*m-1))
    return val+I(-err.hi,err.hi),der+I(-derr.hi,derr.hi)

@lru_cache(None)
def loggamma_psi(x):
    x=F(x);n=64;m=20;z=x+n
    assert x>0
    log2pi=ln(2)+I(ln(PI.lo).lo,ln(PI.hi).hi)
    lg=(z-F(1,2))*ln(z)-z+log2pi/2
    ps=ln(z)-1/(2*z)
    for k in range(1,m):
        lg+=BERN[2*k]/(2*k*(2*k-1)*z**(2*k-1))
        ps-=BERN[2*k]/(2*k*z**(2*k))
    er=abs(BERN[2*m])/(2*m*(2*m-1)*z**(2*m-1))
    ep=abs(BERN[2*m])/(2*m*z**(2*m))
    lg+=I(-er,er);ps+=I(-ep,ep)
    lg-=sum((ln(x+j) for j in range(n)),I(0))
    ps-=sum((1/(x+j) for j in range(n)),F(0))
    return lg,ps

@lru_cache(None)
def constants(d):
    s=1+F(d)
    l1,p1=loggamma_psi(s-F(1,2));l2,p2=loggamma_psi(s)
    logpi=I(ln(PI.lo).lo,ln(PI.hi).hi)
    ci=exp(logpi/2+l1-l2);gi=p2-p1
    z1,zp1=zeta(1+2*d);z2,zp2=zeta(2+2*d)
    cs=-2*zp2/z2;kap=gi-2*zp1/z1-cs
    return ci,z1,z2,cs,kap
