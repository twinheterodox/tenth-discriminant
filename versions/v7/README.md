# Version 7: a unified proof of q < 570

**v0.7.0 · 26 October 2026 · Self-contained consolidation**

[Read the 23-page paper](output/pdf/proof.pdf) · [LaTeX source](proof.tex) · [Release and downloads](https://github.com/twinheterodox/tenth-discriminant/releases/tag/v0.7.0) · [Review record](REVIEW.md)

This version proves `q < 570` and the complete imaginary quadratic
class-number-one classification in one paper, without importing a result
from an earlier version. It contributes to
[Terence Tao's tenth-discriminant challenge](https://terrytao.wordpress.com/2026/10/20/an-experimental-ai-math-challenge-using-tenth-discriminant-bounds-to-explore-arguments-ruling-out-siegel-zeroes/).
The analytic cutoff is unchanged from v6. The improvement is a common
mathematical argument and a self-contained exposition of the entire proof.

## One determinant, two applications

The paper proves the finite-field rank argument, compatible Frobenius and
factorial divisibility, and complex-size estimates once. A common
comparison proposition forces a lower bound for the same smoothed sum
over split and ramified primes throughout.

- **`q >= 2,000`:** a simple norm sieve gives an inert prime
  `q^3 < R <= 3q^3/2`. One factorial refinement and a direct primitive-norm
  upper bound give a contradiction. Monotonicity reduces the infinite
  range to the endpoint 2,000, with normalized gap greater than `0.018345`.
- **`570 <= q <= 2,000`:** the existing five-band calculation uses a finer
  auxiliary-prime sieve, eight finite factorial refinements, positive
  averaging kernels, and the quadratic norm Euler product. Its parameters,
  verification programs, and exact band outputs are retained unchanged.
- **`q < 570`:** a complete residue sieve checks 70 candidate integers.
  Reduced-form enumeration verifies class number one for the nine survivors.

Both analytic applications use `t = 3/64`, `C = 27/64`, and `tau = 3/10`.
There is no longer a proof boundary at 4,000, a separate resultant rank
argument, or an inherited v4/v5 theorem. The primitive norm count is
derived in the paper. The [consolidation record](CONSOLIDATION.md) explains
the generalization of the common estimates and what was preserved.

The mathematical lineage is credited in context: OpenAI's originating
determinant argument, Green's derivative variant, van Dijk's rank argument,
and the suggestions of Silberman, Pratt, Kerr, michaelmross, and Tao.
The paper includes a proof roadmap and an appendix of numerical remainders.

## Inputs and scope

The background inputs are standard quadratic ideal theory and reduction
of binary quadratic forms, the explicitly stated ordinary-prime estimates
of Rosser and Schoenfeld, and classical summation and special-function
identities. The determinant argument and the required norm estimates are
proved here. The fixed parameter tables and exact arithmetic programs are
included in this directory and the release bundle.

The proof uses no Heegner method, quasi-Riemann hypothesis, quadratic
zero-free theorem, quartic-field determinant theorem, or Masser theorem.
The cutoff is an analytic exclusion of the whole range `q >= 570`, not an
enumeration of discriminants in that range. The determinant itself is
theoretical; the programs check the stated inequalities.

## Reproduce the checks

Python 3.8 or newer and its standard library suffice. Run from this
directory without Python's `-O` or `-OO` options:

```sh
python3 verify_tail.py
python3 verify_v6.py
python3 verify_structures.py
python3 verify_finite.py
```

The filename `verify_v6.py` is deliberately retained: it is byte-for-byte
the existing bounded-interval checker, included here with all its local
dependencies. No program reads another version's directory or requires
network access.

The recorded runs pass:

| Check | Scope | Recorded result |
|---|---|---|
| [Uniform tail](tail_output.txt) | Constants and endpoint for `q >= 2,000` | 34 exact rational-interval checks |
| [Bounded interval](certificate_output.txt) | Five bands covering `[570,2,000]` | 429 grouped checks, including 1,258 derivative cells |
| [Structural cases](structural_checks.txt) | Frobenius transformations, floor identities, and factorial inequalities | 101,524 finite exact cases |
| [Finite classification](finite_checks.txt) | All remaining candidates below 570 and the converse | 70 candidates; nine class-number-one fields |

The band outputs reproduce the v6.1 JSON files byte-for-byte, with minimum
gap greater than `0.010389`. See [exact band results](certificate_results.json),
[exact tail results](tail_checks.json), and [reproduction record](REPRODUCTION.json).
All four commands also pass from an isolated extraction of the packaged
code and inputs, with identical output. The [release validation](VALIDATION.json)
records the clean LaTeX build and inspection of all 23 rendered pages.
The displayed gaps concern different normalized quantities and should not
be compared directly with one another.

The final list is `3, 4, 7, 8, 11, 19, 43, 67, 163`. Floating-point searches
previously selected the bounded-interval parameters; acceptance uses
rational intervals and explicit remainder bounds. Decimal terminal output
is for display only.

## Review status and AI disclosure

**The v0.7.0 paper has passed a cross-check by another AI model.** The
repository owner confirmed completion on 26 October 2026. A model name
and detailed report were not supplied. The successful computational checks
above are separate development-session evidence.

The retained v6 argument has a reported second-model cross-check and a
separate AI-assisted audit coordinated by Henric Larsson. His
[clarification](https://terrytao.wordpress.com/2026/10/20/an-experimental-ai-math-challenge-using-tenth-discriminant-bounds-to-explore-arguments-ruling-out-siegel-zeroes/comment-page-1/#comment-698595)
reports no proof or certificate requiring correction. Those reports
predate v7 and are separate from the new v7 model cross-check.
The [review record](REVIEW.md) states the distinctions explicitly.

The published paper, release ZIP, fixed tag, and original validation record
retain their publication-time status, when the v7 cross-check was pending.
This documentation and the release notes record its subsequent completion;
the proof and computational files are unchanged.

Codex prepared the mathematics, exposition, and verification programs
through collaboration with the repository owner. No human peer review
or formal verification of v7 is claimed. Peter W. Murphy's external Lean
adaptation concerns the separate elementary companion, not this paper.
The cutoff 570 is not asserted to be optimal.

## Rebuild and cite

With the LaTeX packages listed in `proof.tex`:

```sh
mkdir -p output/pdf
python3 build_numerical_table.py
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=output/pdf proof.tex
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=output/pdf proof.tex
```

Repeat LaTeX if it requests another pass. The table builder rounds exact
certificate endpoints outward. [MANIFEST.json](MANIFEST.json) records the
source, numerical outputs, documentation, and PDF hashes. The manifest
does not hash itself or the ZIP that contains it. On the main branch it
tracks the current documentation; the unchanged release ZIP retains its
own publication-time documentation and manifest.

For a stable citation use the
[v0.7.0 release](https://github.com/twinheterodox/tenth-discriminant/releases/tag/v0.7.0)
or [fixed source snapshot](https://github.com/twinheterodox/tenth-discriminant/tree/v0.7.0/versions/v7).
All preceding versions and release assets remain available. V7 is a new
mathematical consolidation, not a replacement of the earlier snapshots.
