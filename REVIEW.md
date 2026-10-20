# Review and verification by version

This log records the scope of available evidence. It does not certify
the external theorems or intermediate lemmas cited by each version.

## v0.1.0 — original argument

The repository owner reported on 20 October 2026 that the mathematical
argument was cross-checked with a different frontier model. A model name
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

**The v2 mathematical argument has been cross-checked with a different
frontier model. The independent check passed.** Completion was confirmed
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

**An independent mathematical cross-check of the new v3 argument is
pending.** Codex produced the new argument and checker. The completed v2
cross-check does not cover v3, and the finite checks do not establish the
general analytic lemmas. No independent human review or Lean formalization
of v3 is recorded here.

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
estimates. **Independent mathematical review of v3 remains pending.**
The completed v2 cross-check still applies to v2.

The [patch review record](versions/v3.1/REVIEW.md) gives the scope of
these checks. The original v0.3.0 publication and its review record
remain unchanged.

## Recording future reviews

Record the reviewed version or commit, date, reviewer/model when available,
claims checked, findings, and any corrective commit. Preserve earlier
records and add corrections explicitly when evidence changes.
