# Review record

**Status: v0.6.0 research draft; independent mathematical audit pending.**

The claimed new result is the analytic exclusion of `[570,2000]`. The published v5 implication handles the range above 2000. The previous independent reviews do not cover the new argument.

The certificate checks numerical inequalities with rational intervals. It includes the auxiliary-prime sieve, determinant constants, eight acyclic feedback refinements, positive-kernel normalization, the norm-series error after signed coefficients, and the derivative inequality over each whole discriminant band. The finite structural checks test concrete algebraic cases. Neither type of computation proves the general lemmas on its own, and this is not formal verification.

## Numerical results

All five interval certificates passed. The margins below are rounded down from the exact rational endpoints and include the norm-series and ramified-prime error allowances.

| Band | Certified gap exceeds |
| --- | ---: |
| `[570,580]` | 0.010389 |
| `[580,600]` | 0.021938 |
| `[600,700]` | 0.072367 |
| `[700,1050]` | 0.383240 |
| `[1050,2000]` | 1.446776 |

The final checker includes 429 grouped exact checks, with 1,258 interval cells for the derivative bound. The finite structural program passed 101,524 cases. The finite discriminant scan checked 70 candidates and verified the nine surviving class numbers by reduced forms.

The fifteen-page PDF was compiled without warnings, rendered, and visually inspected on every page. `archive_check.txt` records reproduction and bundle integrity checks. These are checks within the same Codex session, not an independent mathematical audit.

## Mathematical audit targets

Particular points for an independent reader:

- The mixed ideal sieve must count all split primes in the auxiliary interval, with uniform endpoint choices in its area, boundary, and constant terms.
- The compatible three-factor row transformation and the extra coupled valuation must be valid simultaneously for the same nonzero minor.
- The factorial refinement must use only a previous stage and the same smoothed sum; it must not assume a fixed point.
- The joint archimedean inequality must apply to any nonzero minor, including its column selection. The extra `s`-radius saving must not duplicate that bound.
- Every signed kernel term must use the same lower envelope. Positivity comes from the squared polynomial, not from signs of its expanded coefficients.
- The Poisson error must be multiplied by coefficient magnitudes. The derivative certificate concerns the main term; the approximation and ramified errors are uniform constants.
- The ordinary-prime bounds and Table I must have their stated directions and ranges. Only the published v5 result is used for the earlier interval.

The manuscript and programs were produced and reviewed within the same Codex session. There has been no separate-model or independent-person review of v6 in this session. Publication as v0.6.0 does not change the pending independent-audit status.

## Publication preparation

The publication copy changes the title-page version/date labels and documentation from the consolidated local draft. The mathematical text, fixed parameters, certificate programs, numerical outputs, and numerical table are unchanged. Their hashes were checked against the fully reproduced draft. The publication PDF was rebuilt and visually inspected; the certificate was not rerun for these publication-only changes.
