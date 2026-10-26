# Review and verification by paper and version

This log records the scope of available evidence. It does not certify
the external theorems or intermediate lemmas cited by each version.

## How to read the review labels — clarified 26 October 2026

The repository owner clarified that the checks they reported were
**cross-checks by a second AI model**. Earlier wording such as
"independent mathematical verification" and the v5 report's "manual
mathematical audit" should be understood in that sense. No human peer
review is recorded.

- **AI-model cross-check:** a separate model or review session examines
  the mathematical argument. Details and available reports are identified below.
- **Computational checks:** programs check numerical inequalities,
  certificates, or finite cases; these do not establish the general
  mathematical argument on their own.
- **Formal verification:** a proof assistant checks an encoded theorem
  and its dependencies. Peter W. Murphy reports this for an adaptation
  of the elementary companion, with Lean and nanoda. That formalization
  does not cover the numbered versions, historical paper, or
  quadratic-interval note.

The records below identify the available reports and checks for each
paper. External Lean checks have not been rerun here. Published PDFs, release
bundles, and fixed tags retain their publication records; this file gives
the current scope and terminology.

## quadratic-intervals-v0.1.0 — general quadratic fields

**A cross-check by another AI model found no substantive gap in the
interval theorem, logarithmic-derivative bound, or split-prime corollary.**
The repository owner supplied the report on 26 October 2026. It covers
the ten-page draft and its source; the eleven-page publication incorporates
the requested section-reference corrections and explicit counting
constraints. Those subsequent clarifications are distinguished from the
reviewed snapshot in the [note's review record](notes/quadratic-intervals/REVIEW.md).

The checker reported reproducing the supplied exact computations and
checking another eleven determinant norms with a separate implementation.
The bundled program checks 25 determinant minors, 136 prime valuations,
55,091 row-sum bounds, and 2,286 identities, together with rational
constant bounds. Its output is separate from the model's report.
The optional residue consequence retains its external ideal-count input.

The [supplied report](notes/quadratic-intervals/cross_check.txt) identifies
the reviewed artifacts by SHA-256. No reviewer model name was supplied.
No human peer review, formal verification, or determination of priority
is claimed.

## v0.7.0 — unified proof, current review status

**The v0.7.0 paper passed a cross-check by another AI model.** Completion
was reported by the repository owner on 26 October 2026: "The paper has
been independently verified by another model." A model name and detailed
review report were not supplied. This is a report of a separate model
check of v7, not an extension of the earlier v6 review record.

The development-session checks pass: 34 new exact rational checks, all
429 retained interval checks, 101,524 structural cases, and the complete
finite classification.
The five band JSON files and their combined output reproduce v6.1
byte-for-byte. The [v7 review record](versions/v7/REVIEW.md) and
[consolidation record](versions/v7/CONSOLIDATION.md) identify the new
mathematical obligations and the preserved calculation.

No human peer review or proof-assistant formalization of v7 is claimed.
The paper includes its own large-range proof and imports no v4/v5 theorem.
At publication, the new tail and consolidated exposition were awaiting
this check. The fixed paper, bundle, tag, and original validation record
retain that publication-time status; the current documentation and release
notes record the completed check. The mathematical argument, programs,
and numerical outputs have not changed.

## v0.1.0 — original argument

The repository owner reported on 20 October 2026 that the mathematical
argument passed a cross-check by a different frontier AI model. A model name
and detailed review report are not bundled in this repository.

The original finite computation was run with two algorithms, both written
by the same Codex assistant. Their results agree. The Python verifier also
enumerates reduced forms for the nine survivors and checks the original
rational inequalities. The original five-page PDF was rendered and
visually inspected.

The v1 archive is preserved exactly as published, so its original text
still describes the review and publication status at the time that snapshot
was prepared. This log records the subsequent review information.

## v0.2.0 — refined argument

The new exact arithmetic certificate passes all 23 checks. The original
sieve programs and outputs are reused byte-for-byte and cover the entire
remaining range. The cumulative PDF has been compiled, rendered, and
visually inspected.

**The v2 mathematical argument passed a cross-check by a different
frontier AI model.** Completion was confirmed
by the repository owner on 20 October 2026. A model name and detailed
review report are not bundled in this repository.

This is a subsequent review update for
[v0.2.0](https://github.com/twinheterodox/tenth-discriminant/releases/tag/v0.2.0),
published at commit
[`e54a64e`](https://github.com/twinheterodox/tenth-discriminant/commit/e54a64e8212f1e4bc1acfcb1aa0657dc98a18e67).
At publication, the refinement was awaiting this check. The fixed paper,
bundle, and [v2 verification record at publication](versions/v2/REVIEW.md)
retain that historical status; this log records the completed check.
The mathematical result and proof files have not changed in this update.

Banks's cited results remain external inputs. No independent human review
or Lean formalization is recorded here.

## v0.3.0 — direct split-prime argument

The new argument gives an analytic cutoff of `q < 1,000,000` using primitive
lattice counts and Banks's determinant estimates. All 26 exact arithmetic
checks and 22 finite sanity cases pass. The latter comprise 15 lattice
counting cases and prime-norm multiplicity checks through 2,000 in seven
known fields. The five-page PDF was compiled, rendered, and visually
inspected.

The original finite-sieve code and recorded outputs are included
byte-for-byte. Their existing coverage below `10^10` includes the new
remaining interval; the finite sieve was not rerun for v3.

**The v0.3.0 mathematical argument passed a cross-check by a second AI model.**
Completion was confirmed on 20 October 2026 together with the
expanded v0.3.1 paper. The reviewer/model and detailed
review reports were not supplied for inclusion in this repository.
The proof, bundle, fixed tag, and publication-time review record are
preserved unchanged. The finite checks alone do not establish the general
analytic lemmas, and no Lean formalization is recorded here.

The [v3 review record at publication](versions/v3/REVIEW.md) gives the
scope of each check. Banks's determinant construction and cited lemmas,
and Rosser–Schoenfeld's prime estimates, remain external inputs.

## v0.3.1 — expanded v3 exposition

The ten-page paper now includes the background, determinant definitions
and input estimates, intermediate deductions, and complete finite
classification. The analytic bound and constants are unchanged.

The original arithmetic checker and output are preserved byte-for-byte;
all 26 arithmetic checks and 22 finite sanity cases reproduce successfully.
A new direct verifier checks all 124,999 remaining candidate integers
below `10^6` and verifies the nine survivors by reduced-form enumeration.
Both retained larger-range programs were also rerun and reproduce their
original outputs apart from machine-dependent runtime.

The PDF has a clean LaTeX build, and all ten pages were rendered and
visually inspected. The generating assistant checked the expanded
exposition against the original v3 deductions and the cited determinant
estimates. **The expanded v0.3.1 paper also passed a cross-check by a
second AI model.** Completion for both v3 versions was confirmed
on 20 October 2026. The reviewer/model and detailed reports were not
supplied for inclusion in this repository. This subsequent review update
does not change either fixed paper or its publication-time review record.

The [patch review record](versions/v3.1/REVIEW.md) gives the scope of
these checks. The original v0.3.0 publication and its review record
remain unchanged.

## v0.4.0 — derivative determinant argument

The new argument gives the analytic cutoff `q < 4,000`, a factor of 250
below v3. It retains the split-prime count but replaces Banks's determinant
with Green's derivative determinant. The paper includes the determinant
argument, a sharpened resultant nonsingularity criterion, the adapted
quadratic-integer lattice rectangle, and tighter derivative estimates.

All 39 exact arithmetic checks pass. The optional finite checks exercise
the valuation identities in 2,880 cases and the derivative row
transformations in 60,000 cases, including inert `p = 2`. A direct
verifier checks all 499 remaining candidate integers below 4,000 and
enumerates the reduced forms of the nine surviving fields. Both programs
use only the Python standard library and reproduce the recorded outputs.
The ten-page PDF has been compiled, rendered, and visually inspected.

**The v4 mathematical argument passed a cross-check by a second AI model.**
Completion was confirmed on 20 October 2026. The reviewer/model and
detailed report were not supplied for inclusion in this repository.
This is a separate check of v4, subsequent to the checks of v3.0 and v3.1.
The fixed proof, tag, bundle, and publication-time review record remain
unchanged. Codex developed the proof and verification programs; their
arithmetic and finite sanity checks alone do not establish the general
mathematical lemmas.

The [v4 review record at publication](versions/v4/REVIEW.md) identifies
the scope of each check. The two stated Rosser–Schoenfeld estimates,
quadratic ideal theory, and classical reduction of binary quadratic
forms remain external inputs. No Lean formalization is supplied.

## v0.5.0 — Mellin-averaged determinant argument

The analytic cutoff is `q < 2,000`. The new argument averages Green's
derivative determinant inequality over its size parameter and compares
the resulting prime sum with the Euler product of primitive quadratic
norms. Euler summation controls the norm series and its derivative.
The AI-cross-checked v4 result is cited for `q >= 4,000`; the
new interval, including its determinant and resultant arguments, is
treated in full relative to the stated classical inputs.

All 37 exact arithmetic checks pass, certifying a gap greater than
`0.017` uniformly on `2,000 <= q <= 4,000`. The finite checks pass
2,880 valuation cases, 60,000 derivative row-transformation cases, and
10,000 comparisons of primitive-norm coefficients with Euler factors.
An exhaustive verifier checks the 249 remaining candidate integers
below 2,000 and confirms the nine survivors by reduced-form enumeration.
The programs use only the Python standard library. The eleven-page PDF
has a clean LaTeX build and has been rendered and visually inspected.

**V5 passed a cross-check by a second AI model, with exact computational
checks**, as confirmed on 20 October 2026. The original description
"manual mathematical audit" referred to that AI review, not to a human
reviewer. This is not formal verification.
The audit reported one minor wording correction in §6.2: `(log R)/S`,
where `S = floor(R/110)`, is not itself decreasing between floor jumps.
The justification should explicitly use the upper bound
`110.001 log(R)/R`, which decreases for `R >= M > e`. The certificate
already uses this bound, so the conclusion is unaffected.

The reviewed release is v0.5.0, commit
[7a883b7](https://github.com/twinheterodox/tenth-discriminant/commit/7a883b764213cc52c76c9849925b823861eefc38).
The [supplied audit comment](versions/v5/AUDIT.md) is retained with the
correction. No reviewer identity or longer report was supplied. Codex
developed the argument and programs and applied the reported wording
correction within v0.5.0. The original publication tag and Git commit
preserve the first paper, bundle, and publication-time review record.
The release downloads now contain the corrected files.

The [v5 review record at publication](https://github.com/twinheterodox/tenth-discriminant/blob/7a883b764213cc52c76c9849925b823861eefc38/versions/v5/REVIEW.md) specifies
the checks. The stated Rosser–Schoenfeld estimates and classical
quadratic and analytic identities remain external inputs. No Lean
formalization is supplied.

## v0.5.0 — wording correction following the audit

The corrected §6.2 explicitly gives the chain
`(log R)/S <= 110.001 log(R)/R <= 110.001 log(M)/M < 0.00004`
and applies monotonicity to `(log R)/R`. The bound remains `q < 2,000`.
The generating assistant checked that the rest of the mathematical text
is unchanged and confirmed the two relevant exact certificate checks.
All certificate calculations and numerical results are retained; only
the final printed review-status sentence changes. The full suite was
not rerun for this wording correction. The PDF was rebuilt, rendered, and
visually inspected.

The [current v5 audit record](versions/v5/AUDIT.md) records
the AI-model cross-check and the implementation of its finding.
This minor correction retains version v0.5.0. The existing release and
download links serve the corrected paper and bundle; the original files
remain available from the original publication tag and Git commit.

## v0.6.0 — smoothed Frobenius determinant argument

The analytic cutoff is `q < 570`. The new paper excludes the entire real
interval `[570,2,000]` through a smoothed prime-sum comparison, stronger
Frobenius divisibility, eight acyclic factorial refinements, joint
derivative/radius bounds, and a positive squared-polynomial kernel.
The AI-cross-checked v5 result supplies `q >= 2,000`. The new interval proof is
self-contained relative to its stated classical inputs; it does not
depend on intermediate unpublished drafts.

All 429 grouped exact rational checks pass, including 1,258 interval
cells. Five band certificates use 184 auxiliary-prime parameter rows;
the smallest contradiction margin exceeds `0.010389` after the stated
error allowances. A complete run from an isolated ZIP extraction
reproduces all exact band outputs and refinement stages. The structural
checker passes 101,524 finite cases, and the finite discriminant scan
checks 70 candidates below 570 and verifies the nine surviving fields.

The publication copy changes only documentation and title-page labels
from the fully reproduced consolidated draft. Mathematical inputs,
programs, numerical outputs, and the numerical table are byte-identical;
the mathematical body of the paper is unchanged. The fifteen-page PDF
was rebuilt, rendered, and visually inspected. The lengthy certificate
was not rerun for these publication-only changes.

**V6 has a reported successful second-model cross-check and a separate
AI-assisted audit coordinated by Henric Larsson.** These subsequent
reviews are distinct from the development-session computations above.
They are not human peer review or formal verification. No optimality
claim is made for the cutoff.

### Subsequent AI reviews — recorded 26 October 2026

The repository owner
[confirmed a second-model check on 21 October](https://terrytao.wordpress.com/2026/10/20/an-experimental-ai-math-challenge-using-tenth-discriminant-bounds-to-explore-arguments-ruling-out-siegel-zeroes/comment-page-1/#comment-698514).
Separately, Henric Larsson
[reported a GPT-Pro audit of v0.6.0](https://terrytao.wordpress.com/2026/10/20/an-experimental-ai-math-challenge-using-tenth-discriminant-bounds-to-explore-arguments-ruling-out-siegel-zeroes/comment-page-1/#comment-698516)
and then
[clarified its verdict](https://terrytao.wordpress.com/2026/10/20/an-experimental-ai-math-challenge-using-tenth-discriminant-bounds-to-explore-arguments-ruling-out-siegel-zeroes/comment-page-1/#comment-698595).
He reports that the completed audit found no mathematical error or
numerical certificate requiring correction. The initial phrase
"VERIFIED WITH REPAIR" concerned completion and strengthening of his
audit process, not a repair to this proof.

His report covers 1,258 derivative interval cells, 368 auxiliary-prime
endpoints, 1,472 feedback updates, five signed-kernel comparisons, and
explicit Stirling remainder checks. Its conclusion is relative to the
stated classical inputs, the inherited v5 result, and correct outward
interval arithmetic. The external audit reports and scripts are not
bundled here; this entry records the public report and clarification,
not a reproduction of that audit.

The [v6 review record](versions/v6/REVIEW.md) gives the per-band margins
and mathematical audit targets. The
[research record](versions/v6/RESEARCH.md) and
[source record](versions/v6/sources.json) document attribution,
tested alternatives, and remaining possibilities.

## v0.6.1 — revised exposition

The displayed mathematics, parameters, certificate programs, and results
are unchanged from v0.6.0. The AI-review evidence above therefore concerns
the mathematical argument retained in v0.6.1. No separate AI audit of the
revised prose or Lean formalization is recorded. The
[editorial record](versions/v6.1/EDITORIAL.md) documents the preservation
checks and presentation changes.

## elementary-v0.1.0 — elementary companion

The companion gives a self-contained determinant proof of `q < 32,768`,
independent of v1-v6. Its ordinary-prime estimates are proved by elementary
factorial and binomial arguments. Standard quadratic ideal theory, finite
fields, Hadamard's inequality, and elementary analysis are background inputs.

The exact constant checks pass, with final margin `1009/55200`. The finite
sieve checks 4,095 candidate integers using primes through 31; reduced-form
enumeration confirms the nine surviving discriminants. At first
publication, a run from an isolated extraction of the release bundle
reproduced both programs' recorded outputs exactly. The first publication
copied the paper, source, programs, and results from the completed local
draft and added documentation and checksums.

**The elementary companion passed a cross-check by a second AI model,**
as confirmed by the repository owner on 21 October 2026. No reviewer/model
identity or detailed report was supplied. The computations above were
performed in the development session and are separate from the reported
AI-model cross-check. Murphy subsequently published an external Lean
adaptation, as described below.
The [companion review record](companions/elementary/REVIEW.md) gives its
scope and publication checks. It has its own version history, starting at
[elementary-v0.1.0](https://github.com/twinheterodox/tenth-discriminant/releases/tag/elementary-v0.1.0).

The authorship correction dated 21 October 2026 retains the same version
number and the byline "Research note prepared with Codex." Only the
byline and the account-name attribution in the citation to v6 change in
the source; the mathematics, programs, and results are unchanged. The PDF
was rebuilt, rendered, and visually inspected, and the bundle checksums
were updated. The unchanged computation files were compared with the
original release; the mathematical checks were not rerun. The release
downloads contain the corrected files, while the original tag and Git
history preserve the first publication.

The subsequent review-status update records the AI-model cross-check
in the paper and documentation, with no change to the mathematical
argument, programs, or results. At confirmation, the current publication
was [c46f45b](https://github.com/twinheterodox/tenth-discriminant/commit/c46f45b710e9887e4e19c0da66584d04792a77ad).
The original tag retains the status at first publication; the release
downloads include the completed-verification status under the same version.

### Peter W. Murphy's external Lean adaptation — recorded 26 October 2026

Murphy's [determinant development](https://github.com/DrMurphyIsIn/tenth-discriminant/tree/f0995bf604056a98f0af0d182ed152c6bd996419/determinant)
credits this companion at commit `64694aae` as the source of its explicit
constants and assembly. It proves the full class-number-one classification
using `q < 32,768`, with some changes to the estimates and the converse.
Its [verification record](https://github.com/DrMurphyIsIn/tenth-discriminant/blob/f0995bf604056a98f0af0d182ed152c6bd996419/determinant/formalization/VERIFICATION.md)
reports acceptance by Lean and nanoda, with only `propext`, `Quot.sound`,
and `Classical.choice`. See the
[companion review record](companions/elementary/REVIEW.md) for the adaptations,
archive, and verification scope. This is a formalization of the adapted
elementary route, not of v1-v6 or the historical reconstruction; this
documentation update has not rerun the external build or checked Mathlib
submission status.

## historical-v0.1.0 - Weber replacement, 22 October 2026

The replacement develops Weber's modular route with proposed historical
cutoff `N ≤ 1891`, gives `q < 196`, and completes the finite classification.
**No independent mathematical audit verdict is asserted.** Mathematical
correctness and historical admissibility require separate review.

The exact checker passes the multiplier conversion in 1,024 admissible
matrix residue classes, complete root-selection residue calculations,
representative modular matrix identities, cubic resultants, descent
identities, the rational exponential bound, finite exclusions, and all
nine reduced-form lists. An isolated extraction of the replacement bundle
reproduces the recorded output. These checks do not establish the analytic
modular toolkit, the infinite descent, or the historical criterion.

The manuscript's date label is the only change from the completed local
Weber draft; the mathematical text and checker are unchanged. The
fourteen-page PDF was rebuilt, rendered, and visually checked. No formal
verification is supplied. See the [companion review record](companions/historical/REVIEW.md)
and [source audit](companions/historical/historical_sources.txt).

The earlier 1830 determinant reconstruction is superseded because its
historical claim does not meet the revised criterion. Its original
computational checks and review status remain in the
[original publication snapshot](https://github.com/twinheterodox/tenth-discriminant/tree/5d358722319d90f9458a7e95fb76c4044e24f486/companions/historical).
The current release downloads contain the Weber reconstruction under the
same version number; the original tag and Git history are preserved.

## Recording future reviews

Record the reviewed version or commit, date, reviewer/model when available,
claims checked, findings, and any corrective commit. Preserve earlier
records and add corrections explicitly when evidence changes.
