# Version 4: q < 4,000

**v0.4.0 · 20 October 2026 · AI-assisted research draft**

[Read the self-contained ten-page proof](output/pdf/proof.pdf) ·
[LaTeX source](proof.tex) ·
[Download the proof and verification bundle](https://github.com/twinheterodox/tenth-discriminant/releases/download/v0.4.0/tenth-discriminant-v0.4.0.zip)

This contribution to
[Terence Tao's tenth-discriminant challenge](https://terrytao.wordpress.com/2026/10/20/an-experimental-ai-math-challenge-using-tenth-discriminant-bounds-to-explore-arguments-ruling-out-siegel-zeroes/)
improves the analytic cutoff by a factor of **250** over v3:

```text
h(Q(sqrt(D))) = 1  implies  q = |D| < 4,000.
```

Here `D < 0` is a fundamental discriminant. An exhaustive integer check
below the cutoff leaves exactly

```text
q = 3, 4, 7, 8, 11, 19, 43, 67, 163.
```

The paper includes the background, analytic argument, and finite
classification. Reading earlier versions is not required.

## What changed mathematically

The direct split-prime count from v3 is retained. Banks's quartic-field
determinant is replaced with Green's derivative determinant in the
quadratic field. The paper includes that argument and three refinements:

- a sharper resultant criterion proving that the derivative evaluation
  vectors are independent;
- a rectangle adapted to the quadratic-integer lattice, giving smaller
  evaluation points for the required number of points;
- an absolute-value estimate that keeps the decrease in polynomial
  degree when taking derivatives.

With `R = q^4`, `S = floor(R/50)`, and `J = floor(R/55)`, the absolute-value
and inert-prime divisibility bounds contradict each other for every
`q >= 4,000`. The exact certificate verifies a uniform gap greater than
`0.007`. The determinant is a theoretical construction; the programs do
not attempt to construct its enormous matrix.

The derivative determinant and the original resultant method are due to
Ben Green, *On Landau–Siegel zeros*, source snapshot `2610.00311v2`.
The paper gives the full argument it uses, including the new refinements.
Theorems 6 and 9 of
[Rosser–Schoenfeld (1962)](https://doi.org/10.1215/ijm/1255631807), quadratic
ideal theory, and reduction of binary quadratic forms remain external
inputs. No Banks determinant theorem, Heegner method, or computed
zero-free region for quadratic Dirichlet L-functions is used.

## Reproduce the checks

Run from this directory with Python 3.8 or newer. No third-party packages
or earlier-version files are needed:

```sh
python3 verify_green_bound.py --sanity
python3 verify_finite_range.py
```

The first command passes **39 exact arithmetic checks** and **62,880 finite
sanity cases**: 2,880 for the valuation sums and 60,000 for the derivative
row transformations, including inert `p = 2` and high derivative orders.
All arithmetic decisions in the certificate use integers or exact
fractions, with rigorous logarithm intervals. Recorded output:
[checks.txt](checks.txt).

The second command scans all **499** integers with `11 <= q < 4,000` and
`q = 3 (mod 8)`. It applies the necessary small-prime inertness conditions,
then checks fundamental discriminants and reduced forms for the nine
survivors. Recorded output: [finite_range_checks.txt](finite_range_checks.txt).

## Review status

**Independent mathematical review of v4 is pending.** Both v3 papers
have passed independent mathematical checks, but those checks do not
cover the new v4 argument. Codex prepared the derivation and verification
programs. The numerical certificate and finite sanity cases do not
constitute an independent review or a formalization of the general proof.

The supplied PDF was compiled, rendered, and all ten pages visually
inspected. See the [v4 verification record](REVIEW.md) and the
[current repository review record](https://github.com/twinheterodox/tenth-discriminant/blob/main/REVIEW.md).

## Rebuild the paper

With the LaTeX packages specified in the source:

```sh
mkdir -p output/pdf
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=output/pdf proof.tex
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=output/pdf proof.tex
```

[Source provenance](sources.json) records the sources and snapshot hashes.
Third-party research snapshots are not redistributed.
[Artifact checksums](artifact-manifest.json) identify this version's files;
the [repository manifest](https://github.com/twinheterodox/tenth-discriminant/blob/v0.4.0/artifact-manifest.json)
also covers the bundle. The fixed release is
[v0.4.0](https://github.com/twinheterodox/tenth-discriminant/releases/tag/v0.4.0).
Earlier releases remain available at their original links.
