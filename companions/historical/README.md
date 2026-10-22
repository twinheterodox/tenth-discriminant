# No tenth discriminant

## A modern reconstruction using tools documented by 1830

**Proposed historical cutoff: 1830. Analytic cutoff: `q < 32,768`, followed
by a complete printed finite certificate.**

Research note prepared with Codex

**[Read the fourteen-page paper](output/pdf/historical-1830.pdf)** ·
[LaTeX source](proof.tex) ·
[Download the source and verification bundle](historical-v0.1.0.zip) ·
[Release and downloads](https://github.com/twinheterodox/tenth-discriminant/releases/tag/historical-v0.1.0)

This companion addresses [Tao's historical variant, communicated by Ben
Green](https://terrytao.wordpress.com/2026/10/20/an-experimental-ai-math-challenge-using-tenth-discriminant-bounds-to-explore-arguments-ruling-out-siegel-zeroes/#comment-698559):
how early could one give a self-contained proof that there is no tenth
discriminant, using only results and concepts already in the literature?
The paper proves that the negative fundamental discriminants of class
number one have absolute values exactly
`3, 4, 7, 8, 11, 19, 43, 67, 163` and proposes 1830 as an admissible year.
It does not claim that the proof was known then or that this is the
earliest possible date.

## Historical scope and modern attribution

The mathematical proof and the proposed historical cutoff are separate
claims. Section 1.1 states the interpretation of "results and concepts":
new constructions and deductions may use objects, operations, and results
documented by 1830. Giving a later concept an elementary definition or
proof does not by itself establish its historical eligibility.

In particular, the paper treats its finite array of polynomial derivatives
as a new construction from determinants, polynomials, derivatives, and
quadratic congruences. Whether this is an admissible new use of old concepts
is the historical judgment underlying the proposal.

- **H1-H4** document the historical foundations in Gauss (1801), Cauchy
  (1821 and 1823), and Galois (1830).
- **M1-M8** credit modern sources and the context of the challenge.
  Footnotes headed *Modern attribution* appear beside the corresponding
  arguments. Every mathematical assertion needed from those sources is
  proved in the paper.

[Historical source documentation](historical_sources.txt) identifies the
relevant passages, editions, and links. Mathematical review and historical
review remain separate; neither is established by the computational checks.

## Changes from the elementary companion

The reconstruction adapts the [elementary companion](../elementary/README.md)
while retaining `q < 32,768`:

1. Explicit primitive quadratic forms replace ideal theory.
2. Arithmetic modulo an irreducible quadratic, including the required
   power-conjugation identity, is explained and proved.
3. The permutation expansion of a determinant replaces Hadamard's
   inequality. The resulting larger error term still permits the cutoff.
4. A printed certificate replaces the computer sieve as a proof input:
   104 modular witnesses above 163 and 15 below it, followed by a small
   reduced-form enumeration for the nine survivors.

The ordinary-prime estimates are proved from factorials, binomial
coefficients, and elementary calculus. The paper includes all numerical
inequalities and finite tables; the software is supplementary. No earlier
paper is needed to follow the mathematical proof.

## Reproduction and review status

Run with Python 3 and its standard library, without `-O` or `-OO`:

```sh
python3 verify_constants.py
python3 verify_certificate.py
```

- [verify_constants.py](verify_constants.py) checks the rational bounds
  and endpoint margin `1009/55200`.
- [verify_certificate.py](verify_certificate.py) reads the printed tables
  directly from `proof.tex`, checks all 119 modular witnesses, cross-checks
  the finite range by an Euler-criterion sieve of 4,095 candidates, and
  enumerates the reduced forms for the nine survivors.
- [checks.txt](checks.txt) records the outputs and PDF production checks.
- [MANIFEST.json](MANIFEST.json) and [SHA256SUMS](SHA256SUMS) identify the
  distributed files.

The release bundle reproduces the recorded computational outputs.
These are exact arithmetic checks, not formal verification or an
independent mathematical audit. **No independent audit verdict is
asserted for this historical reconstruction.** The elementary companion's
review does not automatically cover these adaptations or the historical
claim. See the [review record](REVIEW.md).

To build the PDF with the LaTeX packages named in `proof.tex`:

```sh
mkdir -p output/pdf
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=output/pdf -jobname=historical-1830 proof.tex
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=output/pdf -jobname=historical-1830 proof.tex
```

All tables are embedded in the source. An additional pass may be needed
after changing table widths.

## Versioning, citation, and AI disclosure

This is **`historical-v0.1.0`**, the first release in the historical
companion series. It has its own history alongside the numbered bounds
and the `elementary-` series. Future historical revisions retain the
`historical-` prefix, including any improvement to the proposed date.
Publication snapshots and release links remain available for citation.

Suggested citation:

> *No tenth discriminant: a modern reconstruction using tools documented
> by 1830*, historical-v0.1.0, 21 October 2026. Research note prepared
> with Codex.

The paper and programs were prepared with OpenAI Codex. Mathematical
credits appear where the ideas enter the proof, including Silberman,
Pratt, Green, and van Dijk, together with Green's report of Pescador's
related unpublished argument. The acknowledgements retain the source
papers' AI attributions.

[Fixed publication snapshot](https://github.com/twinheterodox/tenth-discriminant/tree/historical-v0.1.0/companions/historical) ·
[Release](https://github.com/twinheterodox/tenth-discriminant/releases/tag/historical-v0.1.0) ·
[Historical companion changelog](CHANGELOG.md)
