# Verification record — v0.5.0

Recorded on 20 October 2026. This record applies to the argument giving
`q < 2,000` by excluding the interval `2,000 <= q <= 4,000` and citing
the verified v4 result for the remaining infinite range.

**Independent mathematical review of v5 is pending.**

| Component | Evidence | Scope |
|---|---|---|
| Numerical constants and contradiction | All 37 exact arithmetic checks pass; [output](checks.txt) | Parameter hypotheses, rational intervals with explicit special-function remainders, monotonicity, and a uniform gap greater than `0.017` |
| Valuation formulas | 2,880 finite cases retained from v4 | Exercises the layer identity, small-prime formula, and tail inequality |
| Frobenius row transformations | 60,000 finite cases retained from v4 | Includes inert `p = 2` and derivative orders at least `p` |
| Primitive-norm Euler factors | 10,000 coefficients checked by direct lattice enumeration in five known fields | Finite implementation and identity check, not a proof of the general Euler product |
| Remaining range | All 249 candidate integers below 2,000 checked; [output](finite_range_checks.txt) | Exhaustive exclusion under the necessary small-prime inertness conditions |
| Nine surviving fields | Fundamental-discriminant tests and reduced-form enumeration | Gives one reduced form for each survivor, using the classical form-class correspondence |
| General v5 argument | Derived and checked by the generating Codex assistant | Independent mathematical review pending; no formal verification |
| Earlier-version input | Fixed v4 paper excludes `q >= 4,000`; independent verification confirmed on 20 October 2026 | The infinite-range proof is cited rather than repeated; the new interval argument is given in full |
| PDF | Clean LaTeX build and visual inspection of all eleven pages | Presentation, layout, and cross-references |

The proof and programs were produced by the same assistant. The finite
examples and arithmetic certificate do not establish the general
resultant, determinant, Mellin, Euler-product, or summation arguments.
The completed independent verification of v4 does not extend to the
new v5 deductions. No reviewer identity or detailed report for v4 was
supplied for inclusion in this repository.

Other external inputs are the stated Rosser–Schoenfeld ordinary-prime
estimates, classical quadratic ideal theory, Euler–Maclaurin summation,
gamma identities, and reduced binary quadratic forms. The formulas and
remainder bounds used in numerical evaluation are stated in the paper.

The publication retains the working draft's mathematical text and all
verification programs and outputs. Its title and date identify the
fixed release. Earlier papers, bundles, and tags remain unchanged.

Later checks belong in the
[current repository review log](https://github.com/twinheterodox/tenth-discriminant/blob/main/REVIEW.md),
identifying the reviewed version, reviewer/model when available, scope,
findings, and any corrective commit. This snapshot records the status
at publication.
