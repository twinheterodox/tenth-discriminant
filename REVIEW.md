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

**The v0.3.0 mathematical argument has passed an independent cross-check.**
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
estimates. **The expanded v0.3.1 paper has also passed an independent
mathematical cross-check.** Completion for both v3 versions was confirmed
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

**The v4 mathematical argument has passed independent verification.**
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
The independently verified v4 result is cited for `q >= 4,000`; the
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

**Independent mathematical review of v5 is pending.** Codex developed
the new derivation, paper, and verification programs. The exact
arithmetic certificate and finite examples do not establish the general
v5 proof. V4's completed independent verification applies to the cited
earlier result, not to the new v5 argument.

The [v5 review record at publication](versions/v5/REVIEW.md) specifies
the checks. The stated Rosser–Schoenfeld estimates and classical
quadratic and analytic identities remain external inputs. No Lean
formalization is supplied.

## Recording future reviews

Record the reviewed version or commit, date, reviewer/model when available,
claims checked, findings, and any corrective commit. Preserve earlier
records and add corrections explicitly when evidence changes.
