# Tenth-discriminant bounds

AI-assisted contributions to [Terence Tao's tenth-discriminant challenge](https://terrytao.wordpress.com/2026/10/20/an-experimental-ai-math-challenge-using-tenth-discriminant-bounds-to-explore-arguments-ruling-out-siegel-zeroes/):
find effective bounds for a hypothetical tenth imaginary quadratic field
of class number one. Write `q = |D|` for the absolute fundamental discriminant.

**All three current papers complete the classification**, leaving exactly
`3, 4, 7, 8, 11, 19, 43, 67, 163`. The bounds below are intermediate
analytic cutoffs; each paper then eliminates the finite remainder.

## Start here

| Paper and purpose | Analytic cutoff | Read and reproduce | Review status |
|---|---|---|---|
| **V7: optimized proof** — strongest bound in the numbered series; 23 pages | **`q < 570`** | [PDF](versions/v7/output/pdf/proof.pdf) · [Source](versions/v7/README.md) · [Release](https://github.com/twinheterodox/tenth-discriminant/releases/tag/v0.7.0) | Model cross-check passed ([record](versions/v7/REVIEW.md)) |
| **Elementary companion** — simpler proof; 8 pages | **`q < 32,768`** | [PDF](companions/elementary/output/pdf/elementary-companion.pdf) · [Source](companions/elementary/README.md) · [Release](https://github.com/twinheterodox/tenth-discriminant/releases/tag/elementary-v0.1.0) · [Lean adaptation](https://github.com/DrMurphyIsIn/tenth-discriminant/tree/f0995bf604056a98f0af0d182ed152c6bd996419/determinant) | Model cross-check passed ([record](companions/elementary/REVIEW.md)) |
| **Historical companion** — Weber reconstruction with proposed date 1891; 14 pages | **`q < 196`** | [PDF](companions/historical/output/pdf/historical-1891.pdf) · [Source](companions/historical/README.md) · [Release](https://github.com/twinheterodox/tenth-discriminant/releases/tag/historical-v0.1.0) | No independent audit recorded ([scope](companions/historical/REVIEW.md)) |

The optimized and elementary proofs avoid Heegner's methods. The historical
variant permits Weber's modular approach, including ingredients later used
by Heegner, so its smaller cutoff uses a different permitted toolkit.

[Earlier versions](#versions-and-improvements) · [Review evidence](REVIEW.md) ·
[Changelog](CHANGELOG.md) · [Reproduction and citation](#reproduction-and-citation) ·
[License](#license)

## Reading guide

### Optimized proof

**Begin with v7 for the complete optimized argument.** It proves the
common determinant estimates once, then applies them uniformly above
2,000 and through five certified numerical bands below 2,000. Earlier
versions are not prerequisites. The [consolidation record](versions/v7/CONSOLIDATION.md)
explains how it replaces the inherited v4/v5 arguments while retaining
v6's cutoff of 570.

<a id="companion-papers"></a>

### Elementary companion

Choose this for a shorter determinant proof with fewer analytic inputs.
It derives its ordinary-prime estimates from factorials and binomial
coefficients and uses a rectangular interpolation grid and one endpoint
comparison. Its larger cutoff still permits a short finite sieve.

### Historical companion

This addresses [Tao's historical variant, communicated by Ben Green](https://terrytao.wordpress.com/2026/10/20/an-experimental-ai-math-challenge-using-tenth-discriminant-bounds-to-explore-arguments-ruling-out-siegel-zeroes/#comment-698559):
how early could the theorem have been proved using results and concepts
already in the literature? It develops [Kyle Pratt's proposal of 1891](https://terrytao.wordpress.com/2026/10/20/an-experimental-ai-math-challenge-using-tenth-discriminant-bounds-to-explore-arguments-ruling-out-siegel-zeroes/comment-page-1/#comment-698625)
through Weber's modular theory. The proposed date requires historical
assessment; it is not a claim that the proof was known then or that 1891
is the earliest possible year. The [source audit](companions/historical/historical_sources.txt)
identifies the historical inputs.

## Review and formalization

The [review record](REVIEW.md) distinguishes cross-checks by another AI
model, exact computational checks, and formal verification. V7's model
cross-check was confirmed on 26 October 2026. Detailed reports, check
counts, and review status for each version are linked there.

**Peter W. Murphy has formalized an adaptation of the elementary proof
in Lean**, with [reported acceptance by Lean and nanoda](https://github.com/DrMurphyIsIn/tenth-discriminant/blob/f0995bf604056a98f0af0d182ed152c6bd996419/determinant/formalization/VERIFICATION.md).
His adaptation changes some estimates and the proof for the nine surviving
fields; its scope is described in the [elementary review record](companions/elementary/REVIEW.md).
The numbered and historical papers have no recorded formal verification.

## Versions and improvements

The numbered series records improvements to bounds and to their proofs.
V7 is the current starting point; these earlier papers remain available
for comparison and citation.

| Version | Analytic cutoff | Main development | Files |
|---|---|---|---|
| v6.1 · v0.6.1 | `q < 570` | Revised v6 exposition | [PDF](versions/v6.1/output/pdf/proof.pdf) · [Source](versions/v6.1/README.md) · [Release](https://github.com/twinheterodox/tenth-discriminant/releases/tag/v0.6.1) |
| v6 · v0.6.0 | `q < 570` | Smoothed determinant, factorial refinements, positive kernel | [PDF](versions/v6/output/pdf/proof.pdf) · [Source](versions/v6/README.md) · [Release](https://github.com/twinheterodox/tenth-discriminant/releases/tag/v0.6.0) |
| v5 · v0.5.0 | `q < 2,000` | Averaging and the primitive-norm Euler product | [PDF](versions/v5/output/pdf/proof.pdf) · [Source](versions/v5/README.md) · [Release](https://github.com/twinheterodox/tenth-discriminant/releases/tag/v0.5.0) |
| v4 · v0.4.0 | `q < 4,000` | Derivative determinant with sharper rank and size estimates | [PDF](versions/v4/output/pdf/proof.pdf) · [Source](versions/v4/README.md) · [Release](https://github.com/twinheterodox/tenth-discriminant/releases/tag/v0.4.0) |
| v3 expanded · v0.3.1 | `q < 10⁶` | Expanded exposition and complete finite verification | [PDF](versions/v3.1/output/pdf/proof.pdf) · [Source](versions/v3.1/README.md) · [Release](https://github.com/twinheterodox/tenth-discriminant/releases/tag/v0.3.1) |
| v3 · v0.3.0 | `q < 10⁶` | Direct split-prime count and Banks's determinant | [PDF](versions/v3/output/pdf/proof.pdf) · [Source](versions/v3/README.md) · [Release](https://github.com/twinheterodox/tenth-discriminant/releases/tag/v0.3.0) |
| v2 · v0.2.0 | `q < 5 × 10⁷` | Refined use of Banks's zero-free estimate | [PDF](versions/v2/output/pdf/proof.pdf) · [Source](versions/v2/README.md) · [Release](https://github.com/twinheterodox/tenth-discriminant/releases/tag/v0.2.0) |
| v1 · v0.1.0 | `q < 10¹⁰` | Theta-integral argument using Banks's theorem | [PDF](versions/v1/output/pdf/proof.pdf) · [Source](versions/v1/README.md) · [Release](https://github.com/twinheterodox/tenth-discriminant/releases/tag/v0.1.0) |

The [mathematical changelog](CHANGELOG.md) records the changes and dependencies.
The [elementary](companions/elementary/CHANGELOG.md) and
[historical](companions/historical/CHANGELOG.md) companions have separate
version histories.

<a id="fixed-versions-for-citation"></a>

## Reproduction and citation

Each **Source** link leads to the paper's LaTeX source, verification
programs, recorded outputs, and reproduction instructions. Release pages
provide downloadable PDFs and bundles. Use the version number and the
appropriate release link when citing a paper; the review records describe
later checks of those publication snapshots. All releases are research drafts.

**For the historical paper, use the attached Weber PDF and bundle.**
They replaced the earlier 1830 reconstruction on 22 October 2026 under
`historical-v0.1.0`. The original tag and GitHub's automatic source archives
still contain the superseded paper. The [historical citation guide](companions/historical/README.md#citation-and-publication-history)
identifies the replacement and its source snapshot.

## License

The papers, LaTeX sources, and prose documentation are licensed under
[CC BY 4.0](LICENSE). Verification code, computational certificates,
parameters, and numerical outputs are licensed under [MIT](LICENSE-MIT).
These grants also cover earlier versions and release downloads. See
[licensing scope and attribution](LICENSING.md) for details and third-party
exceptions.

## Credits and archive

The papers and verification programs were prepared with OpenAI Codex.
The determinant work builds on [OpenAI's originating manuscript](https://github.com/openai/math/blob/main/preprints/Uniform-exclusion-of-Landau-Siegel-zeros-October-1-2026/paper.pdf)
and contributions to Tao's challenge discussion. Citations appear beside
the relevant mathematics in each paper; the [research and attribution record](versions/v6.1/RESEARCH.md)
and [v7 consolidation record](versions/v7/CONSOLIDATION.md) document the development.

<a id="original-readme--v1-as-published"></a>

The [original v1 README](versions/v1/README.md) is preserved in its archive,
along with the [original publication snapshot](https://github.com/twinheterodox/tenth-discriminant/tree/v0.1.0).
