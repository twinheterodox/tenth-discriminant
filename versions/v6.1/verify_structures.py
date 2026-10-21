"""Exact finite checks of the continued research lemmas, not a proof audit."""
from fractions import Fraction as F
from math import factorial,comb
from certificate_support import mul,power

def vp(x,p):
    if not x:return 10**6
    out=0
    while x%p==0:x//=p;out+=1
    return out

def run():
    count=0
    for q in (11,19,43):
      for p in (2,3,5):
        inert=q%8==3 if p==2 else pow(-q%p,(p-1)//2,p)==p-1
        if not inert:continue
        for R,S in ((15,7),(31,11)):
          for r in range(R):
            for s in range(S):
              a=min(r//p,S-1-s);c=(r-p*a)//(p*p);b=s//(p*p);terms={}
              for i in range(a+1):
                for j in range(c+1):
                  for l in range(b+1):
                    rr=r-p*i-(p*p-1)*j;ss=s+i-(p*p-1)*l
                    terms[rr,ss]=terms.get((rr,ss),0)+(-1)**(i+j+l)*comb(a,i)*comb(c,j)*comb(b,l)
              assert terms[r,s]==1
              assert all(0<=rr<R and 0<=ss<S and (rr,ss)<=(r,s) for rr,ss in terms)
              for z in ((1,1),(2,1),(-1,2)):
                w=(z[0]+z[1],-z[1])
                for k in (0,1,2,3,4,7,12,20):
                  val=(0,0)
                  for (rr,ss),co in terms.items():
                    if k<=rr:
                      term=mul(power(z,rr-k,q),power(w,ss,q),q)
                      co*=factorial(rr)//factorial(rr-k)
                      val=(val[0]+co*term[0],val[1]+co*term[1])
                  extra=0;pp=p*p
                  while pp<=k:extra+=k//pp;pp*=p
                  loss=min(k,c)+(k-min(k,c))//p
                  strong=a+b+c+k//p-loss+extra
                  coupled=a+b+c//p+extra+max(F(0),F(p-1,p)*(c-k)-1)
                  assert strong>=coupled
                  assert min(vp(val[0],p),vp(val[1],p))>=strong
                  count+=1
    print('PASS residual Frobenius entries, coupling, and triangularity:',count)
    count=0
    for R in range(2,65):
      for S in range(2,16):
        t=F(S,R)
        for p in (2,3,5,7,11):
          cs=[(r-p*min(r//p,S-1-s))//(p*p) for r in range(R) for s in range(S)]
          A=(F(1,2*p*p)-t/(2*p)+t*t/6) if p*t<=1 else 1/(6*t*p**3)
          assert F(sum(cs),R*R*S)>=A-F(1,R)*(1+F(1,p*p))
          assert F(2*sum(c//p for c in cs),R*R*S)>=max(F(0),2*A/p-F(1,R)*(2+F(2,p**3)))
          count+=1
    print('PASS residual Frobenius cell-integral bounds:',count)
    count=0
    for R in range(2,81):
      for p in range(2,R+5):
        a=R//p;fp=F(2*a*p,R)-F(a*(a+1)*p*p,R*R)
        assert F(2*sum(r//p for r in range(R)),R*R)==fp/p
        for S in (2,3,5,11,20):
          exact=F(2*sum(min(r//p,S-1-s) for r in range(R) for s in range(S)),R*R*S)
          lower=fp/p-F(R-1,2*R*S*p)-F((R-1)*(2*R-1),6*R*S*p*p)
          assert exact>=lower
          count+=1
    for n in range(1,12):
      for N in range(n,100):
        K=N//n
        for p in range(2,17):
          assert F(sum((i//n)//p for i in range(N)),N)>=F(sum(k//p for k in range(K)),K)
          count+=1
    print('PASS smoothed floor identity, valuation bound, and factorial feedback:',count)
    print('These are finite exact checks, not formal verification or independent review.')

if __name__=='__main__':
    if not __debug__:raise RuntimeError('Run without Python -O or -OO.')
    run()
