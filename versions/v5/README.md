# Version 5: q < 2,000

**v0.5.0 · 20 October 2026 · AI-assisted research draft**

[Read the eleven-page proof](output/pdf/proof.pdf) ·
[LaTeX source](proof.tex) ·
[Download the proof and verification bundle](https://github.com/twinheterodox/tenth-discriminant/releases/download/v0.5.0/tenth-discriminant-v0.5.0.zip)

This contribution to
[Terence Tao's tenth-discriminant challenge](https://terrytao.wordpress.com/2026/10/20/an-experimental-ai-math-challenge-using-tenth-discriminant-bounds-to-explore-arguments-ruling-out-siegel-zeroes/)
halves the preceding analytic cutoff:

```text
h(Q(sqrt(D))) = 1  implies  q = |D| < 2,000.
```

Here `D < 0` is a fundamental discriminant. An exhaustive integer check
below the cutoff leaves exactly

```text
q = 3, 4, 7, 8, 11, 19, 43, 67, 163.
```

## What changed mathematically

The new argument averages Green's derivative determinant inequality
over its size parameter. This gives a lower bound for a convergent
weighted sum of split and ramified primes. The Euler product of primitive
quadratic norms gives a competing upper bound that retains the effect
of composite norms. Euler summation controls the norm series and its
derivative, and rational intervals certify a contradiction gap greater
than **0.017** throughout `2,000 <= q <= 4,000`.

The paper also sharpens the derivative size estimate by averaging over
the monomial rows, and computes a tighter prime-square tail. It uses
`S = floor(R/110)`, `J = floor(R/160)`, and every integer
`R >= 50,000,000`, then averages with exponent `1 + 1/70`.

## Relationship to v4

The only earlier-version input is the independently verified
[v4 result](https://github.com/twinheterodox/tenth-discriminant/releases/tag/v0.4.0)
excluding `q >= 4,000`. Its infinite-range proof is cited rather than
repeated. The new interval argument is self-contained relative to its
stated classical inputs: it includes the determinant, resultant,
Frobenius, averaging, Euler-product, and summation arguments, with the
numerical formulas and explicit remainder bounds.

The derivative determinant and original resultant method are due to
Ben Green, *On Landau–Siegel zeros*, source snapshot `2610.00311v2`.
The refined rank criterion and lattice construction are retained from
v4. Other inputs are the stated Rosser–Schoenfeld ordinary-prime
estimates, quadratic ideal theory, classical Euler–Maclaurin and gamma
identities, and reduction of binary quadratic forms. No Heegner method
or computed zero-free region for quadratic Dirichlet L-functions is used.

The analytic improvement is uniform over the real interval `[2000,4000]`;
it does not enumerate discriminants in that interval.

## Reproduce the checks

Run from this directory with Python 3.8 or newer. Only the standard
library and files in this directory are required:

```sh
python3 verify_v5_bound.py --sanity
python3 verify_finite_range.py
```

The first command performs **37 exact arithmetic checks**, including
rational enclosures for logarithms, exponentials, zeta values and
derivatives, and a gamma ratio. Every acceptance decision uses integers
or rational intervals with explicit remainders. It also checks **2,880**
valuation cases, **60,000** derivative row transformations, and **10,000**
primitive-norm coefficients against Euler factors in five known fields.
It may take a few minutes. Recorded output: [checks.txt](checks.txt).

The second command checks all **249** candidate integers below 2,000
and verifies the nine survivors by reduced-form enumeration.
Recorded output: [finite_range_checks.txt](finite_range_checks.txt).

The determinant is a theoretical construction; the programs do not
attempt to build its enormous matrix. The arithmetic checks and finite
examples do not establish the general mathematical proof.

## Review and AI disclosure

**Independent mathematical review of v5 is pending.** Codex developed
the new derivation, exposition, and verification programs. The separate
independent verification of v4 has passed, as have the checks of both
v3 papers. Those checks do not cover the new v5 deductions.

The eleven-page PDF was compiled, rendered, and visually inspected.
See the [version review record](REVIEW.md) and the
[current repository review record](https://github.com/twinheterodox/tenth-discriminant/blob/main/REVIEW.md).
This release preserves the mathematical text of the working v5 draft;
the publication changes identify the version and package the files.

## Rebuild the paper

With the LaTeX packages specified in `proof.tex`:

```sh
mkdir -p output/pdf
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=output/pdf proof.tex
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=output/pdf proof.tex
```

[Source provenance](sources.json) records the fixed v4 dependency and
primary sources. Third-party research snapshots are not redistributed.
[Artifact checksums](artifact-manifest.json) identify this version's files;
the [repository manifest](https://github.com/twinheterodox/tenth-discriminant/blob/v0.5.0/artifact-manifest.json)
also covers the bundle. Earlier papers, tags, and release assets remain
available unchanged at their original links.
