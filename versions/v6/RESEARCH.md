# Research record for the consolidated v6 draft

The aim was to improve the analytic tenth-discriminant bound without adding the stronger quadratic zero-location machinery discussed by Tao. The search included the live challenge comments, the cited determinant papers, ordinary-prime estimates, sieve methods, and several new numerical and algebraic refinements. The final comment reread included 25 comments through comment 698497; the last two additions concerned quasi-GRH and idoneal numbers and did not change this method.

## Contributions used

| Source | Contribution used here |
| --- | --- |
| Ben Green, *On Landau-Siegel zeros*, v2 | Derivative determinant and the stronger Frobenius divisibility framework. Green's provenance statement credits ChatGPT for the mathematical arguments and Green for the exposition. |
| Roelof van Dijk, Frobenius determinant note, v1 | Nonvanishing using an auxiliary inert prime. The full finite-field argument needed here is proved in the manuscript. |
| Green, comment 698463 | Attribution of the auxiliary-prime route, including mention of a related unpublished argument of Jacob Pescador. The unpublished Pescador text was not used. |
| Kyle Pratt, comment 698476 | Combine a norm-counting auxiliary inert prime, Green's stronger divisibility, and disk interpolation. |
| Bryce Kerr, comment 698475 and arXiv:2610.21099 | Inspiration to retain higher Frobenius relations and to examine different monomial regions. The final proof does not use the quartic-field construction or Masser nonvanishing. |
| michaelmross, comment 698466, and Tao, comment 698471 | The classical one-coordinate Poisson expansion of the principal norm form. Here it is used for a weighted comparison at real `s > 1`, with a new explicit error calculation. |
| Rosser-Schoenfeld (1962) | Ordinary-prime estimates and Table I. The table entries were checked against the rendered source page. |

The manuscript gives direct links, and `sources.json` identifies the primary sources. The smoothed comparison, finite factorial refinement, compatible residual factors, joint radius/order estimate, and their assembly were developed during this session. They are presented without a priority claim.

## Refinements retained

1. Use an inert prime `p0` as the monomial width `R`, making the exponents `r + p0*s` fill an interval with no gaps. The auxiliary-prime interval then costs a logarithmic shift in the lower bound rather than larger derivative orders.
2. Sieve primitive norm representations with the exact restrictions at 2, 3, 5, and 7, selected split prime ideals, and selected inert rational prime ideals. A second Bonferroni inequality keeps the constants explicit.
3. Retain the exact smoothing function from the floor sum in the inert-prime valuation. Its Mellin transform is explicit. This was a substantial improvement over the ordinary cumulative prime sum.
4. Use the same smoothed sum in the row and column factorial gains, iterating only from earlier stages. The final version starts from zero and needs neither a fixed-point assumption nor a known-norm seed.
5. Combine `z^p-w`, `z^(p^2)-z`, and `w^(p^2)-w` in one triangular row basis. Keep both the residual divisibility and an additional gain involving derivative orders.
6. Couple derivative size and point radius in one pointwise bound with fixed `tau = 3/10`. An analytic inequality captures a further contribution from the second monomial exponent without shell quadrature.
7. Choose positive squared-polynomial kernels and bound the large signed coefficient cancellation using exact intervals and a contour-shift estimate for the norm-series error.

## Alternatives examined

| Route | Outcome of this research pass |
| --- | --- |
| Per-scale optimization of determinant parameters | Produced useful exploratory improvements, but fixed `t,C,tau` already certify 570 and make the final proof easier to inspect. |
| Earlier resultant rank bounds | Useful in the existing versions, but not needed in the new interval. |
| Separate radius and derivative bounds | Weaker than the retained joint inequality; their savings cannot simply be added to it. |
| Quantile factorial refinements and fractional-part corrections | Superseded by direct feedback using the smoothed sum. |
| Disk orthogonal polynomials and numerical transport optimization | A midpoint numerical experiment gave a small gain; it was exploratory, not an exact certificate. The gain did not justify a substantially more complicated proof. |
| More concentrated or higher-degree kernels | Large coefficient norms made the approximation error increasingly expensive. Explicit error control ruled out treating numerical cancellation as free. |
| Higher-order inclusion-exclusion in the sieve | Considered but not certified. Potential area savings compete with rapidly growing boundary and constant terms. No successful computation is claimed. |
| Variable point multiplicities or weighted monomial regions | Considered. They complicate the exact finite-field degree packing and order estimates. No stronger certified result was obtained. |
| Gaudet's sieve for a small split prime in a specified ideal class | Relevant background, but its additional analytic inputs and unspecified numerical exponent did not give a useful explicit replacement here. It is not an input to the proof. |
| Quartic-field/Masser methods and quadratic zero-free estimates | Not imported into this result. |

Moderate-degree kernel searches at 560 did not yield a positive gap in the tested family. That failure does not prove 560 impossible. Further improvements may come from a sharper joint estimate, new compatible valuation factors, a different positive kernel, or a genuinely different argument.

## Why stop at 570

The final certificate has a positive margin at 570 with fixed determinant parameters and manageable signed-sum error. The additional routes tested offered small gains, substantially greater complexity, or no certified improvement. This is a reason to consolidate and seek an independent audit, not a claim that all lighter methods have been exhausted.

Intermediate drafts and exploratory scripts remain in the local research workspace. They are not dependencies of this package, and the earlier public version snapshots are preserved unchanged.
