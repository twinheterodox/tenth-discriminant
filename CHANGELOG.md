# Mathematical changelog

## Subsequent verification of v0.4.0 — 20 October 2026

- Independent mathematical verification of v4 passed.
- Updates the current README, review record, and release descriptions.
  The v4 paper, source, verification files, bundle, and fixed tag are
  unchanged; the mathematical bound remains `q < 4,000`.

## v0.4.0 — 20 October 2026

**Analytic cutoff: `q < 4,000` (previously `q < 1,000,000`).**

- Improves the analytic cutoff by a factor of 250 using Green's derivative
  determinant in the quadratic field, replacing Banks's quartic-field
  determinant. The direct split-prime count from v3 is retained.
- Proves the determinant argument in the paper, including a sharpened
  resultant nonsingularity criterion. Uses an adapted lattice rectangle
  and retains the decrease of polynomial degree under differentiation.
- Chooses `R = q^4`, `S = floor(R/50)`, and `J = floor(R/55)`. The
  determinant comparison gives a uniform contradiction for `q >= 4,000`,
  with an exact rational gap greater than `0.007`.
- Supplies a self-contained ten-page proof, 39 exact arithmetic checks,
  and 62,880 finite sanity cases for the valuation identities and
  derivative row transformations, including inert `p = 2`.
- Checks all 499 remaining candidate integers below 4,000 and verifies
  the nine surviving discriminants by reduced-form enumeration.
- Records independent mathematical review of v4 as pending. The stated
  Rosser–Schoenfeld estimates and classical quadratic theory remain
  external inputs; the determinant argument is included in full.
- Preserves all earlier version snapshots, tags, papers, and bundles.

Paper and reproduction files: [versions/v4](versions/v4/README.md).
Fixed release: [v0.4.0](https://github.com/twinheterodox/tenth-discriminant/releases/tag/v0.4.0).

## Review update for both v3 papers — 20 October 2026

- Both the original v0.3.0 paper and the expanded v0.3.1 paper have passed
  independent mathematical cross-checks.
- Records completion in the current README, review log, and release
  notes. The fixed papers, tags, bundles, and publication-time review
  records remain unchanged. Reviewer/model details and full reports were
  not supplied for inclusion in this repository.
- These checks do not cover the new v4 argument.

See the [current review record](REVIEW.md) for scope and provenance.

## v0.3.1 — 20 October 2026

**Expanded v3 exposition; the analytic cutoff remains `q < 1,000,000`.**

- Adds the problem statement, definitions, and a proof roadmap, so the
  paper can be read without v1, v2, or the original v3 paper.
- Explains class number, prime splitting, the norm lattice, and the
  small-prime obstruction used in the finite exclusion.
- Defines Banks's determinant, retained row indices, and degree sums;
  states the exact external estimates and expands their application.
- Includes the complete finite-exclusion argument, reduced-form
  correspondence, enumeration bounds, and nine surviving forms.
- Adds a short direct verifier for all 124,999 candidate integers below
  `10^6`, with deterministic output. It passes and agrees with both
  retained larger-range computations, which were rerun successfully.
- Preserves the analytic constants and original checker byte-for-byte;
  all 26 arithmetic checks and 22 finite sanity cases still pass.
- Compiles and visually verifies the expanded ten-page paper.
- Leaves the original v0.3.0 files, tag, and release unchanged. Independent
  mathematical review of v3 remains pending.

Paper and reproduction files: [versions/v3.1](versions/v3.1/README.md).
Fixed release: [v0.3.1](https://github.com/twinheterodox/tenth-discriminant/releases/tag/v0.3.1).

## v0.3.0 — 20 October 2026

**Analytic cutoff: `q < 1,000,000` (previously `q < 50,000,000`).**

- Improves the analytic cutoff by a factor of 50 using a direct bound on
  the weighted sum of split primes under the class-number-one assumption.
- Counts primitive lattice points, using inclusion–exclusion over
  `2, 3, 5, 7`, in place of the theta-integral zero construction and the
  zero-dependent prime-bias estimate.
- Uses Banks's determinant construction and Lemmas 4.2, 5.1, and 6.2,
  including the preceding interpolation results, together with
  Rosser–Schoenfeld's explicit prime estimates. These remain external inputs.
- Sets `H = 10^9`, `N = q^13`, and `M = N^(4/3)`. For `q >= 1,000,000`,
  the determinant comparison requires a value greater than `4.238` to be
  less than `4.216`; the certified rational gap exceeds `0.022`.
- Adds a five-page proof of the new cutoff, 26 exact arithmetic checks,
  and 22 finite sanity cases for the lattice formulas and prime-norm
  multiplicities.
- Includes the original finite-sieve code and outputs unchanged. Their
  existing range covers the new remaining interval; the final list of
  nine discriminants is unchanged.
- Records the independent mathematical cross-check of v3 as pending.
  The completed v2 check applies to v2.
- Preserves v1 and v2 snapshots, tags, and release files.

Paper and reproduction files: [versions/v3](versions/v3/README.md).
Fixed release: [v0.3.0](https://github.com/twinheterodox/tenth-discriminant/releases/tag/v0.3.0).

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
