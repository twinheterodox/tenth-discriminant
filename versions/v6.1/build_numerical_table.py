"""Render outward-rounded display bounds from the exact certificate output."""
import json
from fractions import Fraction as F
from pathlib import Path

ROOT=Path(__file__).resolve().parent

def decimal(x,digits,upper=False):
    x=F(x)*10**digits
    n=x.__ceil__() if upper else x.__floor__()
    sign='-' if n<0 else '';n=abs(n)
    return sign+str(n//10**digits)+'.'+str(n%10**digits).zfill(digits)

def scientific_upper(x,digits=3):
    x=F(x)
    if x==0:return '0'
    assert x>0
    exponent=0
    while x<1:x*=10;exponent-=1
    while x>=10:x/=10;exponent+=1
    return decimal(x,digits,True)+r'\times10^{'+str(exponent)+'}'

def main():
    result=json.loads((ROOT/'certificate_results.json').read_text())
    bands=result['bands']
    assert [(b['q0'],b['q1']) for b in bands]==[(570,580),(580,600),(600,700),(700,1050),(1050,2000)]
    out=[r'\begin{center}',r'\small',r'\begin{tabular}{@{}rrrrr@{}}',r'\toprule',
         r'Band & Lower bound & Upper bound & Gap $>$ & Norm error $<$\\',r'\midrule']
    for b in bands:
        out.append('$['+str(b['q0'])+','+str(b['q1'])+']$ & '+decimal(b['lower'],6)+
                   ' & '+decimal(b['upper'],6,True)+' & '+decimal(b['gap'],6)+
                   ' & $'+scientific_upper(b['detail']['norm_error'])+r'$\\')
    out.extend([r'\bottomrule',r'\end{tabular}',r'\end{center}',
                'All displayed bounds are rounded outward. The upper bound includes',
                'both the norm-series error and the ramified-prime allowance.',
                'The exact certificate endpoints are recorded in the JSON output.'])
    (ROOT/'numerical_table.tex').write_text('\n'.join(out)+'\n')

if __name__=='__main__':main()
