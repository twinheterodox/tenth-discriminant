# Verification record — v0.3.0

Recorded on 20 October 2026. This record applies to the new direct
split-prime argument giving `q < 1,000,000`.

| Component | Evidence | Scope |
|---|---|---|
| New numerical constants | 26 exact arithmetic checks pass; [output](checks.txt) | Rational inequalities, exponential bounds, and parameter checks |
| Lattice formulas | 15 finite cases compare direct enumeration, row counting, inclusion–exclusion, and the geometric bounds | Finite examples, not a proof of the general lemmas |
| Prime-norm multiplicities | All primes at most 2,000 checked in each of the seven known class-number-one fields with `q > 4` | Seven finite cases, not an independent analytic review |
| New analytic argument | Written and checked by the generating Codex assistant | Independent mathematical cross-check pending |
| Finite exclusion | Original two algorithms and recorded outputs copied byte-for-byte | Existing evidence covers the full original range below `10^10` and checks reduced forms of the nine survivors; not rerun for v3 |
| External results | Banks's determinant construction and Lemmas 4.2, 5.1, 6.2; Rosser–Schoenfeld Theorems 6 and 9 | Precise dependencies stated in the proof; not independently established here |
| PDF | LaTeX compiled; all five pages rendered and visually inspected | Presentation and cross-references |

The new checker uses integers and exact fractions for all arithmetic
decisions. Logarithmic comparisons use rational Taylor bounds for the
exponential function with a justified tail estimate. Its success does not
constitute a formalization or an independent model review of the proof.

Codex produced the new argument and checker, as well as the inherited
finite-verification programs. The completed independent cross-check of v2
does not cover this new argument. No independent human review or Lean
formalization of v3 is recorded here.

This file records the status at publication. Subsequent reviews belong in
the [current review record](https://github.com/twinheterodox/tenth-discriminant/blob/main/REVIEW.md),
identifying the version or commit, reviewer/model when available, claims
examined, findings, and any corrective commit.
