**A modern reconstruction using tools documented by 1830:** the cutoff
`q < 32,768`, followed by a complete printed finite certificate leaving
`3, 4, 7, 8, 11, 19, 43, 67, 163`.

[Read the fourteen-page paper](https://github.com/twinheterodox/tenth-discriminant/releases/download/historical-v0.1.0/historical-v0.1.0.pdf) ·
[Download the source and verification bundle](https://github.com/twinheterodox/tenth-discriminant/releases/download/historical-v0.1.0/historical-v0.1.0.zip) ·
[Fixed source and reproduction instructions](https://github.com/twinheterodox/tenth-discriminant/tree/historical-v0.1.0/companions/historical)

Research note prepared with Codex

This is the first release of the historical companion series, addressing
[Tao's historical variant, communicated by Ben Green](https://terrytao.wordpress.com/2026/10/20/an-experimental-ai-math-challenge-using-tenth-discriminant-bounds-to-explore-arguments-ruling-out-siegel-zeroes/#comment-698559).
The proposed historical cutoff is 1830, under the interpretation of
"results and concepts" stated in Section 1.1. The claim concerns available
foundations; it does not assert that this proof was known in 1830 or that
the year is optimal.

The reconstruction replaces the elementary companion's ideal theory by
explicit quadratic forms and Hadamard's inequality by determinant
permutation expansion. It explains the required arithmetic modulo an
irreducible quadratic and includes all prime estimates, numerical
inequalities, and finite exclusions in the paper. The finite certificate
contains 119 modular witnesses and a reduced-form table; software is
supplementary.

Historical references H1-H4 document the foundations in Gauss, Cauchy,
and Galois. Modern references M1-M8 credit the sources of the argument,
with attribution footnotes at their points of use. Every assertion needed
from a modern source is proved in the paper. The historical judgment is
whether the determinant construction is an admissible new use of the
documented older concepts.

Exact rational checks, all printed witnesses, a separate sieve of 4,095
candidates, and the nine reduced-form lists pass. An isolated run of the
release bundle reproduces the recorded program outputs. The PDF and
source are unchanged from the revised local draft.

**No independent audit verdict is asserted for this historical
reconstruction.** Mathematical correctness and historical eligibility
require separate review. The computational checks are not formal
verification. See the [review record](https://github.com/twinheterodox/tenth-discriminant/blob/historical-v0.1.0/companions/historical/REVIEW.md).

This is a research prerelease with its own `historical-` version series.
The numbered bounds and elementary companion retain their separate
histories and review records. The downloads include the paper, source,
verification programs, recorded outputs, historical documentation, and
checksums.
