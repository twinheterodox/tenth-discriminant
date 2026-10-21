# Version 6, revised exposition: q < 570

**v0.6.1 · 21 October 2026 · Revised exposition**

This revision reorganizes the v6 paper around its proof: construction of the determinant, a lower bound for a smoothed prime sum, and an incompatible upper bound from the quadratic norm series. Citations now appear beside the ideas they support. The result, displayed equations, parameters, certificate programs, and recorded numerical outputs are unchanged. See the [editorial change record](EDITORIAL.md) for the section mapping and checks. The existing review status is unchanged; the original [v0.6.0 files and downloads](https://github.com/twinheterodox/tenth-discriminant/releases/tag/v0.6.0) remain available.

This is a contribution to [Terence Tao's tenth-discriminant challenge](https://terrytao.wordpress.com/2026/10/20/an-experimental-ai-math-challenge-using-tenth-discriminant-bounds-to-explore-arguments-ruling-out-siegel-zeroes/), following his request for bounds obtained without quadratic zero-location machinery.

The claimed implication is

```text
h(Q(sqrt(D))) = 1  implies  q = |D| < 570,
```

for a negative fundamental discriminant `D`. The new proof excludes the whole real interval `[570,2000]`, without enumerating discriminants in that interval. The published, audited [v5 result](https://github.com/twinheterodox/tenth-discriminant/releases/tag/v0.5.0) supplies the range `q >= 2000`. V5 in turn cites v4 for `q >= 4000`; those arguments also avoid quadratic zero-free-region inputs.

[Read the seventeen-page proof](output/pdf/proof.pdf) · [LaTeX source](proof.tex) · [Download the proof and verification bundle](https://github.com/twinheterodox/tenth-discriminant/releases/download/v0.6.1/tenth-discriminant-v0.6.1.zip)

[Original review record](REVIEW.md) · [Research and attribution](RESEARCH.md) · [Fixed v0.6.1 snapshot](https://github.com/twinheterodox/tenth-discriminant/tree/v0.6.1/versions/v6.1)

The retained review and reproduction records describe the original v0.6.0 package. The [editorial checks](EDITORIAL_CHECKS.json) document equation and file preservation, the revised PDF build, and its layout review.

This package consolidates the entire new interval argument. None of the intermediate unpublished drafts is a mathematical dependency. The earlier published versions remain available separately.

## What improves the bound

The proof combines Green's derivative determinant, van Dijk's auxiliary-prime rank argument, and the norm-counting and disk ideas discussed in the challenge comments. The main refinements are:

- Retain the smoothed noninert-prime sum naturally present in the exact floor valuation. This gives a stronger comparison with the quadratic norm series.
- Feed that same sum directly into the split row and noninert column factorials, through eight finite stages beginning with the zero bound.
- Use compatible residual Frobenius factors, including an additional gain coupling residual row divisibility with derivative orders.
- Bound derivative sizes and interpolation radii together, and retain a further radius contribution from the second monomial exponent.
- Use the auxiliary inert prime itself as the monomial width, a mixed ideal sieve to find that prime, and a positive kernel formed from a squared polynomial.

The determinant parameters are fixed at `t = 3/64`, `C = 27/64`, and `tau = 3/10`. The five interval certificates use 184 auxiliary-prime parameter rows. The positive kernels have polynomial degree 16 in the first band and degree 12 in the other four. Signed coefficient cancellation and the Poisson approximation error are bounded explicitly.

The external number-theoretic inputs are quadratic ideal theory, the published v5 implication, and stated ordinary-prime estimates of Rosser and Schoenfeld. Classical Poisson summation and special-function identities are used in the region `s > 1`. No quasi-Riemann hypothesis, quadratic zero-free theorem, quartic-field determinant, or Masser theorem is imported.

## Reproduce the checks

Python 3.8 or newer and its standard library suffice. Run from this directory, without `-O` or `-OO`:

```sh
python3 verify_v6.py
python3 verify_structures.py
python3 verify_finite.py
```

The first command performs exact rational interval checks of all five bands and writes exact endpoints to `certificate_results.json` and the per-band JSON files. It may take several minutes. Optional integer arguments select lower endpoints, for example `python3 verify_v6.py 570`.

The recorded run passed 429 grouped checks, including 1,258 interval cells for uniform dependence on `q`. Its smallest contradiction margin exceeds `0.010389`, after the stated error allowances. See [certificate output](certificate_output.txt), [exact results](certificate_results.json), and the [review record](REVIEW.md).

The second checks 101,524 finite instances of the residual Frobenius transformations, valuation bounds, smoothed floor identity, and factorial averaging inequality. These tests supplement the general proofs; they do not replace them.

The third separately scans the 70 candidate integers below the analytic cutoff and checks reduced binary quadratic forms for the nine survivors:

```text
3, 4, 7, 8, 11, 19, 43, 67, 163.
```

This finite computation is not used to establish the analytic cutoff of 570. The programs never construct the enormous theoretical determinant.

The fixed inputs are in [parameters.json](parameters.json). Floating-point searches selected those inputs, but no optimizer or floating-point acceptance test is part of the certificate. Logarithm, exponential, zeta, gamma, digamma, and square-root enclosures include explicit remainders or integer bounds.

## Review status and AI disclosure

**Independent mathematical review of this v6 draft is pending.** The prior reviews of v3, v4, and v5 do not cover it. Exact numerical certification, finite algebraic tests, a mathematical audit, and formal verification are different things. This is not formally verified.

Codex developed the refinements, chose parameters, wrote the manuscript and programs, and checked their outputs. The specific external contributions are attributed in the proof and [source record](sources.json). No priority claim is made for the new refinements.

The cutoff 570 is a practical stopping point for this research pass, not an optimality theorem. The [research record](RESEARCH.md) describes tested alternatives and remaining possibilities.

## Rebuild the paper

With the LaTeX packages specified in `proof.tex`:

```sh
mkdir -p output/pdf
python3 build_numerical_table.py
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=output/pdf proof.tex
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=output/pdf proof.tex
```

The table builder rounds the exact certificate endpoints outward for the manuscript. `MANIFEST.json` records the packaged files and their SHA-256 hashes. Third-party papers are cited rather than redistributed.
