# Could the class-number-one theorem have been proved in 1891?

## A reconstruction from Weber's modular theory

**Proposed historical cutoff: N ≤ 1891. Bound: `q < 196`, followed by a
complete finite classification.**

Research note prepared with Codex

**[Read the fourteen-page paper](output/pdf/historical-1891.pdf)** ·
[LaTeX source](proof.tex) ·
[Download the source and verification bundle](historical-v0.1.0.zip) ·
[Release and downloads](https://github.com/twinheterodox/tenth-discriminant/releases/tag/historical-v0.1.0)

**Replacement dated 22 October 2026, retaining `historical-v0.1.0`.**
This paper supersedes the earlier proposal based on tools documented by
1830. That determinant construction does not meet the revised historical
criterion: substantial general methods must already have been published,
and deriving a later method from older foundations does not backdate it.
The original paper remains in the
[original publication snapshot](https://github.com/twinheterodox/tenth-discriminant/tree/5d358722319d90f9458a7e95fb76c4044e24f486/companions/historical)
and Git history; the existing release downloads now contain this Weber paper.

This companion addresses [Tao's historical variant, communicated by Ben
Green](https://terrytao.wordpress.com/2026/10/20/an-experimental-ai-math-challenge-using-tenth-discriminant-bounds-to-explore-arguments-ruling-out-siegel-zeroes/#comment-698559):
how early could one prove that there is no tenth discriminant using results
and concepts already in the literature? It develops
[Pratt's proposal of 1891](https://terrytao.wordpress.com/2026/10/20/an-experimental-ai-math-challenge-using-tenth-discriminant-bounds-to-explore-arguments-ruling-out-siegel-zeroes/comment-page-1/#comment-698625)
into an explicit proof and source audit. The historical variant permits
modular methods, including the ingredients used by Heegner; the original
numerical challenge's exclusion of Heegner's solution does not apply here.

## Proof and historical scope

The paper proves that the negative fundamental discriminants of class
number one have absolute values exactly
`3, 4, 7, 8, 11, 19, 43, 67, 163`. It states the imported classical
modular toolkit explicitly and identifies its locations in Weber's
1891 *Elliptische Functionen und algebraische Zahlen*. Beyond that toolkit,
it supplies the following steps:

1. An explicit product over modular transforms repairs the root-control
   gap in Weber's class-invariant argument, following Stark's repair.
   The product method itself is already in Weber's section 76.
2. The square class invariant is recovered without Weber's stronger,
   conjectural assertion about the cube invariant or general irreducibility
   of class polynomials.
3. Heegner's comparison of cubic equations yields
   `y² = 2x(x³ + 1)`; the integer solutions are found by elementary
   factorizations and Euler's descent, with the decrease made explicit.
4. The coefficient bounds give `q < 196`. Four small-prime witnesses
   exclude the remaining values above 163, and a reduced-form calculation
   completes the classification below 164.

The proposed cutoff permits new applications and problem-specific
completions of already published methods. Heegner's later deduction and
Stark's repair are credited where used. The source audit examines why
these applications may meet that criterion. **1891 is a historical
upper-bound proposal, not a proved earliest year or a claim that the proof
was known then.** The paper does not reconstruct all of elliptic-function
theory from elementary analysis.

References **H1-H3** document historical inputs in Gauss, Euler, and Weber.
References **M1-M6** give later provenance, interpretation, and exposition.
See [the historical source audit](historical_sources.txt) and Appendix C
for exact sections and printed page numbers in the 1891 edition.

## Reproduction and review status

Use Python 3 and SymPy, without `-O` or `-OO`. The checked SymPy version
is pinned in [requirements.txt](requirements.txt):

```sh
python3 -m pip install -r requirements.txt
python3 verify.py
```

The [checker](verify.py) verifies the multiplier conversion in all 1,024
admissible residue matrices, the complete root-selection residue
calculation, representative modular matrix identities, cubic resultants,
the descent identities, the exact exponential bound, finite exclusions,
and the nine reduced-form lists. [verification.txt](verification.txt)
records its output. An isolated extraction of the release bundle reproduces
that output.

**No independent audit verdict is asserted for this Weber reconstruction.**
The exact checks do not establish the analytic modular toolkit, the
infinite descent, or historical admissibility. They are not formal
verification. The mathematical argument and historical judgment require
separate review; see [REVIEW.md](REVIEW.md).

Build the PDF with the LaTeX packages named in `proof.tex`:

```sh
mkdir -p build
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=build -jobname=historical-1891 proof.tex
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=build -jobname=historical-1891 proof.tex
```

The distributed PDF is in `output/pdf/`. The legacy path
`output/pdf/historical-1830.pdf` contains the same revised PDF so that
previous links remain usable; its filename does not describe the current
historical claim. [MANIFEST.json](MANIFEST.json) and [SHA256SUMS](SHA256SUMS)
identify the distributed files.

## Citation and publication history

Suggested citation:

> *Could the class-number-one theorem have been proved in 1891? A
> reconstruction from Weber's modular theory*, historical-v0.1.0,
> replacement dated 22 October 2026. Research note prepared with Codex.

The release name and asset URLs are unchanged. The original tag
`historical-v0.1.0` preserves the superseded 1830 publication; it is not
the source snapshot for the replacement downloads. Use the current
companion files or the replacement commit linked from the release notes.
The [changelog](CHANGELOG.md) records both publications and the reason
for replacement. No new version or release is created.

The paper and computational checks were prepared with OpenAI Codex.
Mathematical credits appear in context. The numbered bounds and the
elementary companion retain their separate histories and review records.
