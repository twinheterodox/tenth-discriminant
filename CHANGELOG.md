# Mathematical changelog

This changelog records the numbered series of bounds and proof revisions. Companion
papers have separate histories: [elementary companion](companions/elementary/CHANGELOG.md)
and [historical reconstruction](companions/historical/CHANGELOG.md).

On 22 October 2026, the historical companion was replaced within
`historical-v0.1.0` by the Weber reconstruction proposing 1891 and
`q < 196`. Its own changelog records the superseded 1830 claim and the
retained original publication snapshot.

## Repository licensing — 26 October 2026

- Licenses the papers, LaTeX sources, documentation, verification programs,
  computational certificates, parameters, and numerical outputs under Apache 2.0.
- Adds the full license text, [NOTICE](NOTICE), and a [scope statement](LICENSING.md)
  explicitly covering the project's material in earlier commits, tagged
  versions, and release downloads. Preserves third-party terms and notices.
- Adds licensing links to the README. Published papers, bundles, tags,
  mathematical results, and review records are unchanged.

## Repository reading guide — 26 October 2026

- Reorganizes the main README around the three current papers: optimized,
  elementary, and historical, with direct paper, source, release, and
  review links near the top.
- Explains that the displayed bounds are analytic cutoffs preceding a
  complete finite classification, and that the historical route permits
  a different toolkit. Keeps Murphy's Lean adaptation beside the elementary
  paper and records its scope.
- Replaces repeated release and audit descriptions with a compact table
  of earlier versions and links to the detailed records. Links the archived v1
  README instead of appending it, and retains the historical replacement's
  citation instructions.
- Changes repository navigation only; paper versions, mathematical results,
  review verdicts, programs, and release assets are unchanged.

## v0.7.0 — model cross-check completed, 26 October 2026

- Records the repository owner's confirmation that the v0.7.0 paper passed
  an independent cross-check by another AI model. No model name or detailed
  report was supplied; this is not human peer review or formal verification.
- Updates the main README, version documentation, review records, and
  release notes. The published paper, bundle, fixed tag, mathematical
  argument, and computational outputs retain their original contents.
- Refreshes the current documentation's source manifest. The release ZIP
  keeps its publication-time manifest and review status.

See the [current v7 review record](versions/v7/REVIEW.md).

## v0.7.0 — unified self-contained proof, 26 October 2026

**The analytic cutoff remains `q < 570`.**

- Proves the full analytic bound and finite classification in one paper,
  with no earlier-version theorem as an input.
- States one determinant comparison under explicit local hypotheses and
  applies it in both ranges. The finite-field rank argument, divisibility
  transformations, and size bounds are proved once.
- Replaces the inherited v4/v5 exclusions with a new uniform argument for
  `q >= 2,000`, using one factorial refinement, a direct smoothed
  primitive-norm bound, and an endpoint comparison with normalized gap
  greater than `0.018345`. There is no longer a boundary at 4,000.
- Retains the five-band certificate for `[570,2,000]` byte-for-byte. A full
  rerun reproduces all five band JSON files and their combined output.
- Passes 34 new exact rational checks, the retained 429 grouped interval
  checks, 101,524 finite structural cases, and the full finite finish.
- Adds an integrated proof roadmap, in-context citations including the
  originating OpenAI manuscript, a common comparison proposition, the
  explicit finite sieve, and a numerical-remainder appendix.
- At publication, records the new tail and consolidated exposition as
  awaiting a separate model cross-check; its subsequent completion is
  recorded above. The prior v6 AI reviews are not relabeled as v7 review.
- Preserves all earlier version directories, release tags, and assets.
  The elementary and historical companions retain their separate series.

[Paper and reproduction](versions/v7/README.md) ·
[Consolidation record](versions/v7/CONSOLIDATION.md) ·
[Review scope](versions/v7/REVIEW.md) ·
[Fixed release](https://github.com/twinheterodox/tenth-discriminant/releases/tag/v0.7.0).

## Review documentation and external Lean formalization — 26 October 2026

- Adds prominent links to Peter W. Murphy's Lean adaptation of the
  elementary companion, its paper, and its reported Lean/nanoda checks.
  Records its scope separately from the numbered series and historical paper.
- Clarifies that the reviews reported by the repository owner were
  cross-checks by another AI model. Earlier descriptions of independent
  mathematical verification or a manual audit did not mean human peer review.
- Records the public second-model confirmation and Henric Larsson's
  separate AI-assisted audit of v0.6.0. His clarification reports no proof
  or certificate requiring repair; the repairs concerned the audit process.
- Replaces stale pending statuses in the current documentation and explains
  how the v6.0 review applies to the unchanged mathematics of v6.1.
- Distinguishes AI-model review, computational checks, and formal
  verification. No external Lean build or audit is rerun for this update.
- Updates documentation and its source manifests only. Paper versions,
  proofs, programs, numerical results, release downloads, and fixed tags
  are preserved. Earlier entries below retain the terminology recorded at
  the time; the current meanings and evidence are in [REVIEW.md](REVIEW.md).

See also the [elementary companion changelog](companions/elementary/CHANGELOG.md).

## v0.6.1 — revised exposition, 21 October 2026

**The analytic cutoff remains `q < 570`.**

- Reorganizes v6 around construction of the determinant, a lower bound
  for the smoothed prime sum, and its contradiction with a positive
  norm-series average.
- Adds a proof roadmap and explanations of the purpose of each technical
  estimate. Places citations beside the ideas used, moves numerical
  remainder bounds to an appendix, and explains the existing finite check.
- Preserves all 81 displayed mathematical blocks, the theorem and lemma,
  verification code, fixed parameters, exact outputs, and numerical table.
- Supplies a seventeen-page paper with a clean LaTeX build and checked
  layout. Records editorial preservation checks separately from the
  unchanged original review and reproduction records.
- Preserves the v0.6.0 directory, tag, paper, and download assets. The
  revised paper has its own v0.6.1 tag and release; audit status is unchanged.

Paper and reproduction files: [versions/v6.1](versions/v6.1/README.md).
Section mapping and checks: [EDITORIAL.md](versions/v6.1/EDITORIAL.md).
Fixed release: [v0.6.1](https://github.com/twinheterodox/tenth-discriminant/releases/tag/v0.6.1).

## v0.6.0 — 20 October 2026

**Analytic cutoff: `q < 570` (previously `q < 2,000`).**

- Retains the smoothed noninert-prime sum from the exact determinant
  floor valuation and feeds it into the row and column factorials through
  eight acyclic refinements.
- Combines compatible residual Frobenius factors with an additional
  derivative-order divisibility gain, joint derivative/radius bounds,
  and a further contribution from the second monomial exponent.
- Uses an auxiliary inert prime as the monomial width, a mixed ideal
  sieve to find it, and a positive squared-polynomial averaging kernel.
  Signed coefficients and the Poisson norm-series error are bounded
  explicitly.
- Fixes `t = 3/64`, `C = 27/64`, and `tau = 3/10`. Five band certificates
  exclude the whole interval `[570,2,000]`, using 184 auxiliary-prime
  parameter rows. The smallest certified gap exceeds `0.010389`.
- Passes 429 grouped exact rational checks, including 1,258 interval
  cells, and 101,524 finite structural cases. A complete isolated rerun
  reproduces the exact band outputs and refinement stages. The finite
  scan checks 70 candidates below 570 and verifies the nine survivors.
- Supplies a fifteen-page proof of the new interval relative to its
  stated classical inputs, with no dependency on intermediate unpublished
  drafts. The audited v5 implication supplies `q >= 2,000`.
- Uses no quasi-Riemann hypothesis, quadratic zero-free theorem,
  quartic-field determinant, or Masser theorem. Attributes the external
  ideas and records the alternatives explored and remaining possibilities.
- Records independent mathematical audit of v6 as pending. Preserves all
  earlier version files, tags, and downloadable assets.

Paper and reproduction files: [versions/v6](versions/v6/README.md).
Research and attribution: [RESEARCH.md](versions/v6/RESEARCH.md).
Fixed release: [v0.6.0](https://github.com/twinheterodox/tenth-discriminant/releases/tag/v0.6.0).

## v0.5.0 — wording correction and completed audit, 20 October 2026

**The bound remains `q < 2,000`.** V5 has passed a manual mathematical
audit with exact computational checks; this is not formal verification.

- Applies the audit's minor wording correction in §6.2. The proof
  explicitly uses `(log R)/S <= 110.001 log(R)/R` and the decrease
  of `(log R)/R`, with `S = floor(R/110)`.
- The certificate already uses this upper bound. Its calculations,
  numerical constants, and results are unchanged; only the final
  printed review-status sentence now points to the review record.
- Keeps version v0.5.0 for this minor correction and updates its existing
  release downloads. The original v0.5.0 tag and Git commit preserve the
  first publication, including its original paper and bundle.
- Withdraws the briefly published v0.5.1 release and tag. All commits
  remain in Git history.

Current paper and reproduction files: [versions/v5](versions/v5/README.md).
Audit finding: [AUDIT.md](versions/v5/AUDIT.md).
Release: [v0.5.0](https://github.com/twinheterodox/tenth-discriminant/releases/tag/v0.5.0).
Original snapshot: [7a883b7](https://github.com/twinheterodox/tenth-discriminant/tree/7a883b764213cc52c76c9849925b823861eefc38/versions/v5).

## v0.5.0 — 20 October 2026

**Analytic cutoff: `q < 2,000` (previously `q < 4,000`).**

- Averages Green's derivative determinant inequality over its size
  parameter to bound a convergent weighted sum of non-inert primes.
- Uses the Euler product of primitive quadratic norms for a competing
  upper bound, accounting for composite norms. Euler summation controls
  the norm series and its derivative with explicit errors.
- Chooses `S = floor(R/110)`, `J = floor(R/160)`, and Mellin exponent
  `sigma = 1 + 1/70`, with the determinant estimates valid for all
  `R >= 50,000,000`.
- Supplies 37 exact arithmetic checks certifying a contradiction gap
  greater than `0.017` uniformly on `2,000 <= q <= 4,000`, plus 62,880
  retained determinant sanity cases and 10,000 new comparisons of
  primitive-norm coefficients with Euler factors.
- Checks the 249 remaining candidate integers below 2,000 and verifies
  the nine surviving discriminants by reduced-form enumeration.
- Cites the independently verified v4 result for `q >= 4,000`. The
  eleven-page paper includes the rest of the argument in full relative
  to its stated classical inputs, including the determinant and resultant
  proofs and explicit numerical formulas with error bounds.
- Records independent mathematical review of v5 as pending. Preserves
  all earlier version snapshots, tags, papers, and downloadable assets.

Paper and reproduction files: [versions/v5](versions/v5/README.md).
Fixed release: [v0.5.0](https://github.com/twinheterodox/tenth-discriminant/releases/tag/v0.5.0).

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
