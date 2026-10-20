# Verification record — v0.4.0

Recorded on 20 October 2026. This record applies to the derivative
determinant argument giving `q < 4,000`.

| Component | Evidence | Scope |
|---|---|---|
| Numerical constants and uniform contradiction | All 39 exact arithmetic checks pass; [output](checks.txt) | Rational logarithm enclosures, parameter hypotheses, monotonicity bounds, and a contradiction gap greater than `0.007` |
| Valuation formulas | 2,880 finite cases check the layer-count identity, small-prime formula, and tail inequality | Finite sanity checks, not a proof for all parameters |
| Frobenius row transformations | 60,000 finite cases, including inert `p = 2` and derivative orders at least `p` | Exercises exact divisibility in the full quadratic integer ring |
| Remaining range | All 499 candidates with `11 <= q < 4,000`, `q = 3 (mod 8)`, checked by a direct residue scan; [output](finite_range_checks.txt) | Complete finite exclusion under the necessary small-prime inertness condition |
| Nine surviving fields | Fundamental-discriminant tests and reduced-form enumeration give one form each | Uses the classical correspondence between form classes and ideal classes |
| General mathematical argument | Derived and checked by the generating Codex assistant; determinant and resultant arguments included in the paper | Independent mathematical review pending |
| External inputs | Rosser–Schoenfeld Theorems 6 and 9, classical quadratic ideal theory, and reduction of binary quadratic forms | Statements used are identified; these inputs are not independently reproved |
| PDF | Clean LaTeX build; all ten pages rendered and visually inspected | Presentation, layout, and cross-references |

**The completed independent checks of v0.3.0 and v0.3.1 do not cover v4.**
The new argument replaces Banks's construction with Green's derivative
determinant and introduces a sharper nonsingularity lemma and size
estimates. Those general mathematical steps require their own review.

The certificate uses integers and exact fractions for every acceptance
decision. The derivative determinant itself is not constructed by the
programs. Neither the numerical gap nor the finite examples formalize
the general proof. The proof and programs were produced by the same
assistant; no independent mathematical check or Lean formalization of
v4 is recorded at publication.

Later reviews should be recorded in the
[current repository review log](https://github.com/twinheterodox/tenth-discriminant/blob/main/REVIEW.md),
identifying the reviewed version, reviewer/model when available, scope,
findings, and any corrective commit. Fixed snapshots retain their status
at publication.
