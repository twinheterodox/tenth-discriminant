# Verification record — v0.3.1

Recorded on 20 October 2026. This patch expands the exposition of v3
without changing the analytic cutoff `q < 1,000,000`, its constants, or
the original arithmetic checker. It adds a direct finite-range verifier.

| Component | Evidence | Scope |
|---|---|---|
| Analytic constants | The original checker and output are unchanged; all 26 exact checks reproduce successfully | Rational inequalities, exponential bounds, and parameter hypotheses |
| Lattice and prime-norm formulas | All 22 original finite sanity cases reproduce successfully | Finite examples, not a proof of the general lemmas |
| Exact remaining range | New direct scan checks all 124,999 candidates in `11 <= q < 10^6`, `q = 3 (mod 8)`; [output](finite_range_checks.txt) | Exhaustive application of the necessary small-prime conditions, with no earlier-version input files |
| Surviving fields | Fundamental-discriminant tests and exhaustive reduced-form enumeration yield one form for each of the nine survivors | Uses the classical correspondence between reduced forms and ideal classes, stated in the paper |
| Larger finite range | Retained C++ and Python programs rerun successfully; outputs agree with the original records except runtime | Covers `q < 10^10`; supports the new direct finite check |
| Expanded mathematical exposition | Checked by the generating Codex assistant against the original v3 deductions and cited determinant estimates | Independent mathematical cross-check pending |
| External results | Banks's construction and Lemmas 4.2, 5.1, 6.2; Rosser–Schoenfeld's prime estimates; classical quadratic theory | Statements and notation supplied in the paper, not independently reproved |
| PDF | Clean LaTeX build; all ten pages rendered and visually inspected | Presentation, layout, and cross-references |

All arithmetic decisions in the two current Python verifiers use integers
or exact fractions. The direct finite scan includes nonfundamental
integers in its candidate set, so it cannot discard a genuine candidate
through a squarefreeness filter. Its residue tables are also checked
against Euler's criterion.

Codex authored the exposition and all programs. Neither the program
checks nor the generating assistant's review constitute an independent
model review or a formal verification of the analytic proof. The
completed v2 cross-check does not cover v3. No independent human review
or Lean formalization of v3 is recorded.

The original v0.3.0 publication and its review record remain unchanged.
Later checks should identify the exact reviewed version or commit and be
recorded in the
[current review log](https://github.com/twinheterodox/tenth-discriminant/blob/main/REVIEW.md).
