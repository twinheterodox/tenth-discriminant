# Research record for v7

The objective was to make the optimized `q < 570` proof self-contained and
clearer. The inherited divisions at 4,000 and 2,000 reflected the sequence
of earlier releases; the investigation asked which divisions the final
argument actually needed.

The useful common structure is the v6 derivative minor, its finite-field
nonvanishing proof, and the smoothed noninert-prime sum arising from the
exact floor valuation. The elementary companion also uses the same
finite-field rank idea. Retaining that idea throughout avoids introducing
the older resultant argument and a second determinant construction.

The existing v6 constants prove enough for `q >= 2,000` without the full
positive-kernel machinery. At scales above `q^2`, geometric errors admit
fixed uniform bounds even as `q` grows. A simple 210 sieve provides the
necessary inert primes. One factorial refinement and the primitive norm
count previously used in v4 then give a contradiction. Retaining a simple
linear upper bound on the original smoothing weight is useful here.

The resulting infinite-range inequality is decreasing in `q` after
normalization by `log q`. Its endpoint has a comfortable margin, so the
investigation did not optimize the transition value below 2,000. That
endpoint already joins the existing certified interval and removes every
earlier-version proof dependency.

The final structure has one determinant argument and two upper estimates.
Forcing a fixed finite-band envelope and kernel to cover all `q` would
require further scale or parameter changes; no clarity benefit was found
in doing so. The five certificate bands near 570 remain useful numerical
subdivisions of the same argument, rather than five different proofs.

This version does not seek or claim a smaller analytic cutoff, an optimal
cutoff, or a new solution of the general Landau–Siegel zero problem.
The preceding [v6 research record](https://github.com/twinheterodox/tenth-discriminant/blob/v0.6.1/versions/v6.1/RESEARCH.md)
documents the broader optimization work and alternatives considered there.
The present mathematical changes are described in
[CONSOLIDATION.md](CONSOLIDATION.md), with review scope in
[REVIEW.md](REVIEW.md).
