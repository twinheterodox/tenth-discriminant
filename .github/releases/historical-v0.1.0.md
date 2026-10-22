**Could the class-number-one theorem have been proved in 1891?**
A reconstruction from Weber's modular theory, with **`q < 196`** and a
complete finite classification.

**Replacement dated 22 October 2026, retaining `historical-v0.1.0`.**
This release now contains the Weber paper. It supersedes the earlier 1830
determinant reconstruction, whose historical claim does not meet the
revised requirement that substantial methods themselves were already
published. The release name and download URLs remain unchanged.

[Read the fourteen-page paper](https://github.com/twinheterodox/tenth-discriminant/releases/download/historical-v0.1.0/historical-v0.1.0.pdf) ·
[Download the replacement source and verification bundle](https://github.com/twinheterodox/tenth-discriminant/releases/download/historical-v0.1.0/historical-v0.1.0.zip) ·
[Current source and reproduction instructions](https://github.com/twinheterodox/tenth-discriminant/tree/main/companions/historical)

Research note prepared with Codex

The paper develops
[Pratt's proposal of 1891](https://terrytao.wordpress.com/2026/10/20/an-experimental-ai-math-challenge-using-tenth-discriminant-bounds-to-explore-arguments-ruling-out-siegel-zeroes/comment-page-1/#comment-698625)
for [Tao's historical variant, communicated by Ben Green](https://terrytao.wordpress.com/2026/10/20/an-experimental-ai-math-challenge-using-tenth-discriminant-bounds-to-explore-arguments-ruling-out-siegel-zeroes/#comment-698559).
The modular toolkit is stated explicitly and located in Weber's 1891 book.
The paper then supplies:

- the special root-control repair of Weber's class-invariant argument,
  using the product method already described in his section 76;
- Heegner's comparison of cubic equations and the Diophantine restriction
  `y² = 2x(x³ + 1)`;
- an elementary solution including Euler's descent with a strict decrease;
- `q < 196`, four small-prime exclusions above 163, and the finite
  classification below 164.

The result leaves exactly `3, 4, 7, 8, 11, 19, 43, 67, 163`.
Historical references H1-H3 and modern references M1-M6 distinguish old
inputs from later provenance. Heegner, Stark, and Pratt are credited in
context. The cutoff is a defensible historical proposal under the stated
criterion, not a proved earliest year or a claim that the proof was known
in 1891. The paper is self-contained after its stated classical modular
toolkit; it does not rebuild elliptic-function theory from elementary
analysis.

The exact algebra, multiplier residue calculations, finite exclusions,
and reduced-form checks pass. An isolated extraction of the replacement
bundle reproduces the recorded output. **No independent audit verdict is
asserted for this reconstruction.** These checks do not establish the
analytic modular toolkit, the infinite descent, or historical
admissibility, and they are not formal verification. See the
[review record](https://github.com/twinheterodox/tenth-discriminant/blob/main/companions/historical/REVIEW.md).

**Use the attached replacement ZIP for the Weber source.** The original
tag `historical-v0.1.0` is preserved, so GitHub's automatic “Source code”
archives still contain the superseded 1830 paper. Its
[original publication snapshot](https://github.com/twinheterodox/tenth-discriminant/tree/5d358722319d90f9458a7e95fb76c4044e24f486/companions/historical)
and Git history remain available. The
[companion changelog](https://github.com/twinheterodox/tenth-discriminant/blob/main/companions/historical/CHANGELOG.md)
records the replacement. The numbered bounds and elementary companion
are unchanged.
