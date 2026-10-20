# Mathematical changelog

## Review update — 20 October 2026

- The v2 mathematical argument passed an independent cross-check with a
  different frontier model.
- Updates the current README, review record, and release notes to record
  completion. The bound, proof, verification programs, and fixed version
  snapshots are unchanged.

See the [current review record](REVIEW.md) for scope and provenance.

## v0.2.0 — 20 October 2026

**Analytic cutoff: `q < 50,000,000` (previously `q < 10^10`).**

- Adds a complete cumulative paper containing the original proof, the
  refinement, and the finite classification.
- Strengthens the theta estimate from `1 - beta < 10/sqrt(q)` for
  `q >= 10^10` to `1 - beta < 2/sqrt(q)` for `q >= 49,000,000`.
- Uses Banks's Lemma 4.2, Lemma 5.1, and Corollary 6.3, with their preceding
  construction and hypotheses, at `H = 10^9`, `N = q^18`. This gives
  `(1 - beta) log q > 0.00509` for `q >= 50,000,000`, contradicting the
  refined theta bound of less than `0.00502`.
- Changes the external dependency for the refinement from the statement
  of Banks's Theorem 1.1 to intermediate results in its proof. Those
  intermediate results remain external assumptions.
- Adds a certificate with 23 exact rational checks of the new constants.
- Reuses the original finite-sieve code and outputs without changing them.
  The final list of nine fields is unchanged.
- At publication, recorded that the refinement was awaiting a separate-model
  mathematical cross-check. The completed check is recorded in the review
  update above.

Paper and reproduction files: [versions/v2](versions/v2/README.md).
Fixed release: [v0.2.0](https://github.com/twinheterodox/tenth-discriminant/releases/tag/v0.2.0).

## v0.1.0 — 20 October 2026

**Original analytic cutoff: `q < 10^10`.**

- Takes Banks's Theorem 1.1 for `q >= 10^10` as an external input.
- Supplies an explicit classical theta-integral argument with
  `1 - beta < 10/sqrt(q)`.
- Uses two exact integer sieve implementations and reduced-form
  enumeration to obtain `3, 4, 7, 8, 11, 19, 43, 67, 163`.
- Contains the original source, five-page PDF, programs, outputs, source
  provenance, checksums, and downloadable bundle.

Original commit: [`b305496`](https://github.com/twinheterodox/tenth-discriminant/commit/b30549663b6d2660b2df3c916822802774e2486d).
An exact copy of every tracked file in that commit is available in
[versions/v1](versions/v1/README.md). The original proof, code, outputs,
and bundle also remain at their existing root paths.

The archived documents retain their original statements about review and
publication status. The later report of a different-frontier-model
cross-check is recorded in [REVIEW.md](REVIEW.md), without modifying that
historical snapshot.
