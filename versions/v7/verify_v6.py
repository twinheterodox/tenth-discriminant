#!/usr/bin/env python3
"""Exact rational certificate for the consolidated v6 research draft.

Only Python's standard library is used. Floating-point displays are never
used in acceptance decisions. This checks numerical inequalities, not the
general mathematical proof or an independent audit of it.
"""
import json,sys
from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
from math import isqrt,gcd,comb
from exact_arithmetic import I,PI,ln,exp,power
from exact_high import constants,zeta,loggamma_psi

ROOT=Path(__file__).resolve().parent
PARAM=json.loads((ROOT/'parameters.json').read_text())
T,C,TAU,GAM=(F(PARAM[k]) for k in ('t','C','tau','gamma'))
CT=F(12703,12500)
TABLE=[(F(a),F(b)) for a,b in PARAM['rs_table']]
COUNT=0

def check(condition,label):
    global COUNT
    assert condition,label
    COUNT+=1

def floorq(x,digits=14):return F((F(x)*10**digits).__floor__(),10**digits)
def ceilq(x,digits=14):return F((F(x)*10**digits).__ceil__(),10**digits)

def sqrt(x):
    x=I(x);sc=10**60
    def root(y):return isqrt(y.numerator*sc*sc//y.denominator)
    return I(F(root(x.lo),sc),F(root(x.hi)+1,sc))

def logi(x):
    x=I(x);return I(ln(x.lo).lo,ln(x.hi).hi)

def absmax(x):
    x=I(x);return max(abs(x.lo),abs(x.hi))

def fpow(x,s):return exp(logi(x)*F(s))

def prime_list(n):
    flags=bytearray(b'\x01')*(n+1);flags[:2]=b'\x00\x00'
    for p in range(2,isqrt(n)+1):
        if flags[p]:flags[p*p:n+1:p]=b'\x00'*((n-p*p)//p+1)
    return [p for p in range(2,n+1) if flags[p]]

def theta_bounds(x):
    x=I(x)
    assert x.lo>=ln(563).hi
    hi=min(CT,(1+1/(2*x)).hi);lo=(1-1/(2*x)).lo
    for b,ep in TABLE:
        if b<=x.lo:
            hi=min(hi,1+ep)
            lo=max(lo,(1-ep-F(51,50)*exp(-x/2)-3*exp(-2*x/3)).lo)
    return lo,hi

@lru_cache(None)
def norm_points(q0,q1):
    out=[]
    for b in range(1,isqrt((q0*q0-1)//(4*q1))+1):
        for a in range((-b)//2+1,(q0+3)//4):
            p=F((2*a+b)**2+q1*b*b,4)
            if p>=F(q0,4)**2:break
            if gcd(a,b)==1:out.append((p,a,b))
    return sorted(out)

@lru_cache(None)
def sieve_constants(q0,q1,n,h):
    pts=norm_points(q0,q1)[:n]
    assert len(pts)==n
    ps0=[F((2*a+b)**2+q0*b*b,4) for _,a,b in pts]
    ps1=[p for p,a,b in pts]
    rs=[p for p in prime_list((q0-1)//4) if p>7][:h]
    assert len(rs)==h
    u=2*sum((1/p for p in ps1),F(0))+sum((F(1,r*r) for r in rs),F(0))
    u2=2*sum((1/p**2 for p in ps1),F(0))+sum((F(1,r**4) for r in rs),F(0))
    umax=2*sum((1/p for p in ps0),F(0))+sum((F(1,r*r) for r in rs),F(0))
    assert umax<1
    v=2*sum((1/sqrt(p) for p in ps0),I(0))+sum((F(1,r) for r in rs),F(0))
    v2=2*sum((1/p for p in ps0),F(0))+sum((F(1,r*r) for r in rs),F(0))
    vlo=sqrt(F(q0,4));vhi=sqrt(F(q1,4));nevents=2*n+h
    aa=PI*F(768,1225)/(4*vlo)*(1-u+(u*u-u2)/2)
    bb=PI*sqrt(1+1/(vlo*vlo))/4*F(96,35)*(1+v+(v*v-v2)/2)
    cc=2*PI*(vhi+1/vhi)*(1+F(nevents*(nevents+1),2))
    return aa,bb,cc

def psi_integral(j):
    a=2*TAU
    part=j*j/(2*a)-j**3/(3*(a-1))+j**4/(12*(a-2))
    part-=2*power(j,a+2)/(a*(a-1)*(a-2)*(a+1)*(a+2))
    return (j*2*TAU*TAU/(2*TAU+1)-(1-TAU)*part+j/2-3*j*j/4
            +(1-j)**2*ln(1-j)/2+j**3/6-j**4/24)

def archimedean(M,j,e):
    eps=F(1,M);m=ln(M);nu=C*(1+2*e)**2
    B=(1-TAU)*j*(1-ln(j));I0=2*TAU*TAU/(2*TAU+1)
    D=-3*TAU/2+2*nu/(T-eps)*(psi_integral(j)
       +j*(B+5*e/(3*(1+e)))+(I0+B)/M)-2*B
    delta=j*C/(T-eps)*((1+2*e)**2+e/(2+e))-1
    assert 0<delta<1 and delta>=e
    sg=(T-eps)*(F(1,4)-delta+3*delta*delta/4-delta*delta*ln(delta)/2)
    sg+=eps*ln(delta)/2
    sgain=max(F(0),sg.lo)
    return D+2*m/M-sgain,sgain

def build_band(band,ps,logs):
    q0,q1=band['q0'],band['q1'];pts=norm_points(q0,q1)
    K2=sum((ln(p)/p**2 for p,a,b in pts),I(0))+ln(q1)/q1**2
    H=(1/T).__floor__();small=[p for p in ps if p<=H]
    assert H*4<q0 and all(p*T<=1 for p in small)
    theta=sum((logs[p] for p in small),I(0))
    ah=sum((logs[p]/p for p in small),I(0))
    W=sum((logs[p]*(T-F(p,3)*T*T) for p in small),I(0))
    P=PARAM['prime_cutoff']
    BH=sum((logs[p]/p**2 for p in ps if p>H),I(0))+2*CT/P-sum(logs.values(),I(0))/P**2
    assert (BH-K2).lo>0
    h32=sum((F(1,i) for i in range(1,33)),F(0))
    fa=(ln(33)-h32-F(1,33)+1)/2;fb=(h32-ln(33))/2
    base=[]
    for row in band['rows']:
        a,end=row['a'],row['b'];M=2**a;eps=F(1,M);m=ln(M)
        k=F(row['k']);n,h=row['sieve_n']
        assert end>a and k>1 and m.lo>4 and M>q1
        if n:assert M>pts[n-1][0]
        low,high=theta_bounds(m)
        aa,bb,cc=sieve_constants(q0,q1,n,h)
        margins=[]
        for power2 in (a,end):
            X=2**power2;x=ln(X);ell=x+ln(k)
            margin=k*low-high-ell*(aa*(k-1)+bb*(1+sqrt(k))/sqrt(X)+cc/X)
            margins.append(margin.lo)
        check(min(margins)>0,f'{q0}-{q1}, a={a}: auxiliary inert prime')
        v=sqrt(F(q1,4));rho=sqrt(1+v*v)/2;rad=sqrt(C*M*v/PI)
        e=ceilq((rho/rad).hi,24);nu=C*(1+2*e)**2
        b=floorq((T-eps)/nu,24);j=F(1,9)+eps
        jeff=j-b/2+b*eps;alpha=(1-T)/2-jeff;beta=1+T-2*jeff
        assert 0<b<j<1 and 0<alpha<F(1,2) and 0<beta<4*GAM
        assert ((rad+rho)/M).hi<F(1,10) and rho.lo>1
        assert (ln(T)+2*m).lo>2
        # n>=CR and J=ceil(R/9) give nJ>=tR^2>=RS.
        assert C/9==T
        ac,sgain=archimedean(M,j,e)
        geom=(ln(C)-ln(2)-logi(PI))/2+ln(1+e)
        floorlo,floorhi=theta_bounds(m-ln(33))
        fg=max(F(0),(fb*floorlo-fa*floorhi).lo)
        sf=I(0);rg=I(0);cg=I(0)
        for p in ps:
            if 4*p>=q0:break
            pp=p*p
            while pp<M:
                sf+=logs[p]*max(F(0),(b-eps)/pp-2*eps);pp*=p
            sf+=logs[p]*max(F(0),(T-eps)/(p*p)-3*eps)
            mean=(F(1,2*p*p)-T/(2*p)+T*T/6) if p*T<=1 else 1/(6*T*p**3)
            rg+=logs[p]*max(F(0),2*mean/p-(2+F(2,p**3))*eps)
            cg+=2*logs[p]*max(F(0),(1-F(1,p))*(mean-(1+F(1,p*p))*eps-jeff)-eps)
        err=2*theta/M+m/((T-eps)*M)+2*(ln(T)+2*m)/M
        cost=beta/4*ln(q0)+ah-W+high+(BH-K2)/(3*(T-eps))+beta*geom+ac+err
        cost+=F(667,500)+1/(2*m)-fg-sf-rg-cg+alpha*ln(k)
        start=ceilq((m+ln(k)).hi);finish=floorq((end*ln(2)+ln(k)).lo)
        out=dict(a=a,b=end,start=start,end=finish,A=floorq(alpha),D=ceilq(cost.hi),bcol=b,
                 sgain=sgain,residual=rg.lo,coupling=cg.lo,margin=min(margins))
        base.append(out)
        check(True,f'{q0}-{q1}, a={a}: geometry and determinant bounds')
    history=[];old=[];shift=GAM*ln(F(q1,q0)).hi
    for stage in range(band['stages']+1):
        def phi(x):
            x=I(x);value=F(0)
            for line in old:
                if x.lo>=line['start']:
                    value=max(value,line['A']*min(x.lo,line['end'])-line['D']-shift)
            return value
        new=[]
        for p in base:
            M=2**p['a'];m=ln(M);eps=F(1,M);z=p['bcol']-eps;tt=T-eps
            assert z>0
            gain=z*phi(m+ln(z))+tt*max(F(0),phi(m+ln(tt))-ln(q0).hi/q0)
            row=p.copy();row['D']=ceilq(p['D']-gain);row['feedback']=gain;new.append(row)
        history.append(new);old=new
        check(True,f'{q0}-{q1}: acyclic feedback stage {stage}')
    return old,history

def segments(lines):
    breaks=sorted({p['start'] for p in lines}|{p['end'] for p in lines})
    out=[]
    for ix,lo in enumerate(breaks):
        hi=breaks[ix+1] if ix+1<len(breaks) else None
        active=[(F(0),F(0))]
        for p in lines:
            if p['start']<=lo:
                if p['end']>lo:active.append((p['A'],-p['D']))
                else:active.append((F(0),p['A']*p['end']-p['D']))
        while hi is None or lo<hi:
            a,b=max(active,key=lambda z:(z[0]*lo+z[1],z[0]))
            stop=hi
            for c,f in active:
                if c>a:
                    cross=(b-f)/(c-a)
                    if cross>lo and (stop is None or cross<stop):stop=cross
            # Rounding a switch affects maximality, never validity: both
            # affine candidates are valid on this whole activity interval.
            if stop is not None and stop!=hi:
                stop=min(hi,ceilq(stop,14)) if hi is not None else ceilq(stop,14)
            out.append((lo,stop,a,b))
            if stop is None:break
            assert stop>lo
            lo=stop
    return out

def mellin(seg,d):
    total=I(0)
    for lo,hi,a,b in seg:
        total+=exp(-d*I(lo))*(a*(lo+1/d)+b)
        if hi is not None:total-=exp(-d*I(hi))*(a*(hi+1/d)+b)
    return total

def kernel_coefficients(kernel):
    d,e=F(kernel['delta']),F(kernel['epsilon'])
    p=[int(v) for v in kernel['polynomial']];degree=kernel['degree']
    assert len(p)==degree+1 and any(p)
    raw=[sum(p[i]*p[j-i] for i in range(max(0,j-degree),min(j,degree)+1)) for j in range(2*degree+1)]
    ds=[d+i*e for i in range(len(raw))]
    norm=sum((F(a)/s for a,s in zip(raw,ds)),F(0))
    assert d>0 and e>0 and norm>0
    coeff=[F(a)/s/norm for a,s in zip(raw,ds)]
    assert sum(coeff)==1
    return ds,coeff

def shifted(xs):
    n=len(xs)-1
    return [sum((xs[i]*comb(i,j) for i in range(j,n+1)),I(0))*(-1)**j for j in range(n+1)]

def polyval(xs,x):
    total=I(0)
    for c in reversed(xs):total=total*x+c
    return total

def upper_certificate(band,ds,coeff):
    q0,q1=band['q0'],band['q1'];ell=ln(F(q0,4));ellmax=ln(F(q1,4))
    v0=sqrt(F(q0,4));v1=sqrt(F(q1,4))
    hs=[];rs=[];kaps=[];av=[];effective=[];error=I(0)
    for d,c in zip(ds,coeff):
        s=1+d;a=F(1,2)+d;ci,z1,z2,cs,kap=constants(d)
        ff=ci*z1*power(F(q0,4),-a);r=ff/z2
        hh=ff*(ell+kap)/(2*(z2+ff))
        mult=2*d*zeta(1+d)[0]/((1+d)*(2+d))
        assert 0<r.lo<r.hi<F(1,4) and hh.lo>0 and cs.lo>0
        assert (a*(ell+kap)-1-r).lo>0 # each H decreases with q
        dist=floorq(((2*s-1)/(2*PI)).lo,6)
        assert 0<dist<v0.lo
        z=exp(-2*PI*v0);y=exp(-2*PI*(v0-dist))
        ea=2*ci*power(dist,1-2*s)*y/((1-z)*(1-y))
        _,psi1=loggamma_psi(s);_,psi0=loggamma_psi(s-F(1,2));gg=psi1-psi0
        en=ea*(2*logi(2*v1)+2*absmax(ln(dist))+gg+PI/2+2*z/(1-z))
        he=(en+(cs+2*hh)*ea)/(2*(1-ea))
        assert ea.hi<1 and he.lo>0
        error+=abs(c)*mult*he
        hs.append(hh);rs.append(r);kaps.append(kap);av.append(a);effective.append(c*mult)
    check(True,f'{q0}-{q1}: special functions and contour-shift norm error')
    ram=ln(q0)/(2*(q0-1))
    upper=sum((c*h for c,h in zip(effective,hs)),I(0))+error+ram
    # Stable geometric-polynomial certificate for d/d log(q) of the
    # signed upper main term. No derivative of an error bound is needed.
    maxell=max((ellmax+kap).hi for kap in kaps)
    length=24
    while True:
        tail=I(0)
        for c,r,a,kap in zip(effective,rs,av,kaps):
            tail+=absmax(c)*r**(length+1)/2*(1/(1-r)+a*maxell*((length+1)/(1-r)+r/(1-r)**2))
        if tail.hi<F(1,10**10):break
        length+=8
        assert length<=120
    polys=[]
    for ll in range(1,length+1):
        common=[c*((-1)**(ll+1))*r**ll for c,r in zip(effective,rs)]
        jj=[u*(1-ll*a*(ell+kap)) for u,a,kap in zip(common,av,kaps)]
        kk=[-u*ll*a for u,a in zip(common,av)]
        polys.append((shifted(jj),shifted(kk)))
    ymax=ln(F(q1,q0)).hi
    ncells=(ymax*1000).__ceil__();worst=None
    d,e=ds[0],ds[1]-ds[0]
    for cell in range(ncells):
        y=I(F(cell,1000),F(cell+1,1000))
        ef=exp(-(F(1,2)+d)*y);et=exp(-e*y);fp=I(1);tp=I(1);val=I(0)
        for jj,kk in polys:
            fp*=ef;tp*=et;h=1-tp;h=I(max(F(0),h.lo),h.hi)
            val+=fp*(polyval(jj,h)+y*polyval(kk,h))/2
        bound=val.hi+tail.hi
        worst=bound if worst is None else max(worst,bound)
        assert bound<-GAM,(q0,q1,cell,'derivative bound',str(bound))
    check(True,f'{q0}-{q1}: {ncells} log-q cells, upper derivative < -0.3')
    return upper,dict(norm_error=error.hi,ramified_error=ram.hi,derivative_upper=worst,
                      derivative_tail=tail.hi,geometric_terms=length,log_q_cells=ncells)

def printable(x):
    if isinstance(x,F):return str(x)
    if isinstance(x,dict):return {k:printable(v) for k,v in x.items()}
    if isinstance(x,(tuple,list)):return [printable(v) for v in x]
    return x

def decimal(x,digits=12,upper=False):
    scaled=F(x)*10**digits
    n=scaled.__ceil__() if upper else scaled.__floor__()
    sign='-' if n<0 else '';n=abs(n)
    return sign+str(n//10**digits)+'.'+str(n%10**digits).zfill(digits)

def run():
    if not __debug__:
        raise RuntimeError('Run this certificate without Python -O or -OO.')
    selected=None if len(sys.argv)==1 else set(map(int,sys.argv[1:]))
    ps=prime_list(PARAM['prime_cutoff']);logs={p:ln(p) for p in ps};results=[]
    mertens=ln(319)-sum((logs[p]/p for p in ps if p<=319),I(0))+1/(2*ln(319))
    check(mertens.hi<F(667,500),'ordinary prime-sum constant < 1.334')
    for band in PARAM['bands']:
        q0,q1=band['q0'],band['q1']
        if selected is not None and q0 not in selected:continue
        print('BEGIN',q0,q1,flush=True)
        lines,history=build_band(band,ps,logs)
        seg=segments(lines);ds,coeff=kernel_coefficients(band['kernel'])
        lower=sum((c*mellin(seg,d) for c,d in zip(coeff,ds)),I(0))
        print('  determinant and positive-kernel lower bound complete',flush=True)
        upper,detail=upper_certificate(band,ds,coeff)
        gap=lower.lo-upper.hi
        check(gap>0,f'{q0}-{q1}: strict contradiction')
        print('PASS',q0,q1,'lower >',decimal(lower.lo),'upper <',decimal(upper.hi,upper=True),
              'gap >',decimal(gap),'norm error <',decimal(detail['norm_error'],18,upper=True),flush=True)
        results.append(dict(q0=q0,q1=q1,lower=lower.lo,upper=upper.hi,gap=gap,detail=detail,
                            lines=lines,segments=seg,feedback_stages=history))
        (ROOT/f'certificate_{q0}_{q1}.json').write_text(json.dumps(printable(results[-1]),indent=2)+'\n')
    out=dict(checks=COUNT,bands=results)
    target='certificate_results.json' if selected is None else 'certificate_selected.json'
    (ROOT/target).write_text(json.dumps(printable(out),indent=2)+'\n')
    print('All',COUNT,'exact checks passed. General proof and independent review remain separate.',flush=True)

if __name__=='__main__':run()
