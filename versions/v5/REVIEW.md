# Verification record — v0.5.0

Recorded on 20 October 2026. The v5 argument gives `q < 2,000` by
excluding `2,000 <= q <= 4,000` and citing the verified v4 result
for the remaining infinite range.

**V5 has passed a manual mathematical audit with exact computational
checks.** The audit identified one minor wording correction in §6.2,
implemented in this wording correction. This is not formal verification. The
[audit record](AUDIT.md) contains the supplied finding, the reviewed
commit, and the correction.

| Component | Evidence | Scope |
|---|---|---|
| General v5 argument | Completed manual mathematical audit with exact computational checks, reported on 20 October 2026 | One wording correction in §6.2; no change to the conclusion; no formal verification |
| §6.2 correction | Explicit bound `(log R)/S <= 110.001 log(R)/R`, followed by monotonicity of `(log R)/R` | The certificate already uses this bound; its two relevant exact inequalities were confirmed when applying the patch |
| Numerical constants and contradiction | All 37 exact arithmetic checks passed; [recorded output](checks.txt) | Calculations and numerical results retained from v0.5.0; a uniform gap greater than `0.017` |
| Valuation formulas and row transformations | 2,880 valuation cases and 60,000 derivative cases passed | Unchanged calculations and results, including inert `p = 2` and high derivative orders |
| Primitive-norm Euler factors | 10,000 coefficients checked by direct enumeration in five known fields | Unchanged finite implementation and identity checks |
| Remaining range and nine survivors | All 249 candidate integers below 2,000 checked, followed by reduced-form enumeration; [output](finite_range_checks.txt) | Program and output retained byte-for-byte |
| Earlier-version input | Fixed v4 paper excludes `q >= 4,000`; independent verification confirmed on 20 October 2026 | The infinite-range proof is cited; the new interval argument is included in full |
| PDF | Clean LaTeX build, rendering, and visual inspection | Presentation, layout, and cross-references |

The audit applies to v0.5.0 with the reported correction. Codex applied
that correction in v0.5.0, checked that the mathematical change is
confined to the explanation in §6.2, and confirmed that all certificate
calculations are unchanged. The verifier's final status message now
refers to this review record. The recorded numerical results and finite
checks are retained; the full suite was not rerun for this wording correction.

No reviewer identity or report beyond the supplied comment was provided.
The stated Rosser–Schoenfeld ordinary-prime estimates, classical quadratic
ideal theory, Euler–Maclaurin summation, gamma identities, and reduction
of binary quadratic forms remain external inputs. The exact formulas and
remainder bounds used in numerical evaluation are stated in the paper.

This wording correction retains version v0.5.0. The release PDF and
bundle were updated on 20 October 2026. The original publication is
preserved at the v0.5.0 tag and
[original commit](https://github.com/twinheterodox/tenth-discriminant/tree/7a883b764213cc52c76c9849925b823861eefc38/versions/v5).
Later reviews belong in the
[current repository review log](https://github.com/twinheterodox/tenth-discriminant/blob/main/REVIEW.md).
