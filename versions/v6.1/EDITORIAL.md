# v0.6.1: editorial revision of v6

Published as v0.6.1 on 21 October 2026, based on the [original v0.6.0 source](https://github.com/twinheterodox/tenth-discriminant/tree/v0.6.0/versions/v6). The result remains `q < 570`, with the same dependency on v5 for `q >= 2000`.

The rewrite explains the argument in the order a reader needs it. The introduction gives the theorem, the exact earlier-version dependency, and a three-step proof roadmap. Each technical section explains its purpose before introducing the estimates. Contributions from the challenge comments are cited at the relevant steps. The numerical remainder bounds have moved to an appendix, and the research history remains in `RESEARCH.md`.

## Section mapping

| Published v6 | Editorial draft |
| --- | --- |
| 1. Scope, provenance, and the result | 1. Introduction; contextual citations throughout; closing acknowledgements |
| 2–3. Arithmetic consequences and ordinary-prime inputs | 2. Arithmetic and ordinary-prime estimates |
| 4–5. Auxiliary-prime sieve and nonvanishing | 3. Constructing the determinant |
| 6–8. Smoothed valuation, higher Frobenius factors, and factorials | 4. Prime divisibility of the determinant |
| 9. Joint derivative/radius estimate | 5. An upper bound for the complex size |
| 10. Affine bounds and finite iteration | 6. Assembling the lower bound for the prime sum |
| 11–12. Positive kernels and norm-series error | 7. Positive kernels and the quadratic norm series |
| 13. Certification | 8. Exact certification and completion of the proof |
| 13.1. Numerical remainder bounds | Appendix A |
| 14. Directions tested and stopping point | Existing `RESEARCH.md`; brief closing scope statement |

The draft also explains the existing finite discriminant check in §8.2. It distinguishes that computation from the analytic proof of the cutoff. Silberman's small-prime observation and Pratt's finite-sieving comment are now cited where those arguments are used.

## Preservation and checks

- All 81 displayed mathematical blocks are byte-identical to the published source, in the same order. The theorem, lemma, and proof environments are also byte-identical.
- All verification programs, arithmetic support files, parameters, exact certificate results, recorded check outputs, and the numerical table are unchanged.
- `REVIEW.md`, `REPRODUCTION.json`, `archive_check.txt`, and `RESEARCH.md` are preserved as historical records of the original package. Their original page counts and build descriptions refer to that package.
- The revised PDF is built and checked separately; `EDITORIAL_CHECKS.json` records those checks. The full numerical certificate is not rerun for this exposition-only revision.

The original v0.6.0 directory, tag, PDF, and downloadable bundle are preserved. The new v0.6.1 tag and release provide a distinct citation for the rewrite. The title-page version and date distinguish this paper from both the original and the local editorial draft. The existing audit status is unchanged.
