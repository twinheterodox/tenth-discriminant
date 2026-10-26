# Review and verification: elementary-v0.1.0

**The elementary companion passed a cross-check by a second AI model,**
confirmed on 21 October 2026. Peter W. Murphy subsequently published an
external Lean adaptation, with reported Lean and nanoda kernel checks.
These are separate kinds of evidence, described below.

## AI-model cross-check

The repository owner confirmed on 21 October 2026:

> elementary passed independent verification

At confirmation, the current publication was
[commit c46f45b](https://github.com/twinheterodox/tenth-discriminant/commit/c46f45b710e9887e4e19c0da66584d04792a77ad).
Its mathematical argument and verification programs are unchanged from
the original `elementary-v0.1.0` publication; the intervening revision
changed authorship attributions only. No reviewer/model identity or
detailed review report was supplied. On 26 October the repository owner
clarified that this was a model cross-check. The quoted phrase does not
indicate human peer review or formal verification, and the cross-check is
distinct from the development-session computations listed below.

## External Lean adaptation — recorded 26 October 2026

Peter W. Murphy's [determinant development](https://github.com/DrMurphyIsIn/tenth-discriminant/tree/f0995bf604056a98f0af0d182ed152c6bd996419/determinant)
explicitly credits this companion at commit `64694aae` for the constants
and assembly. Links here are pinned to his repository commit
`f0995bf604056a98f0af0d182ed152c6bd996419`. The first archived release
containing the determinant proof is
[v1.1.0, DOI 10.5281/zenodo.23563656](https://doi.org/10.5281/zenodo.23563656).

His [paper](https://github.com/DrMurphyIsIn/tenth-discriminant/blob/f0995bf604056a98f0af0d182ed152c6bd996419/determinant/paper/paper.pdf)
describes a Lean proof of the complete class-number-one classification,
using the same cutoff `q < 32,768` and finite sieve. The adaptations
include a Leibniz bound in place of Hadamard's inequality, a different
endpoint-monotonicity argument, and a Minkowski-based converse for the
nine surviving fields. It is not a verbatim formalization of this paper;
Murphy also distinguishes its analytic dependencies from the elementary
presentation here.

His [verification record](https://github.com/DrMurphyIsIn/tenth-discriminant/blob/f0995bf604056a98f0af0d182ed152c6bd996419/determinant/formalization/VERIFICATION.md)
and README report Comparator acceptance under Lean and nanoda, using
only `propext`, `Quot.sound`, and `Classical.choice`, plus a separate AI
review session's replay and a clean CI build. This entry records those
published checks; the external build was not rerun for this documentation
update. No Mathlib acceptance is asserted. The formalization covers the
adapted elementary route, not v1-v6 or the historical reconstruction.

## Mathematical scope

The theorem excludes `q >= 32,768` for negative fundamental discriminants
of class number one. The proof includes the necessary prime estimates,
norm count, auxiliary-inert-prime construction, derivative determinant,
finite-field nonvanishing argument, divisibility estimate, and uniform
endpoint comparison. Its background inputs are standard quadratic ideal
theory, finite fields, Hadamard's inequality, and elementary analysis.

The numerical bounds are consequences of the written uniform argument.
The code checks its constants; it does not prove the general lemmas by
testing examples or compute the determinant.

## Checks completed

- `verify_constants.py` reproduces all recorded rational inequalities,
  including the auxiliary-prime estimate, the boundary error `E < 1/500`,
  and the final margin `1009/55200`.
- `verify_finite.py` tests all 4,095 integers `q = 3 (mod 8)` in
  `8 < q < 32,768`. The sieve deliberately includes nonfundamental values.
  Primes through 31 leave exactly `11, 19, 43, 67, 163` above 8.
- The residue tables agree with Euler's criterion. Reduced-form enumeration
  gives class number one for each of the nine surviving fundamental
  discriminants, including `3, 4, 7, 8` below 9.
- At first publication, both programs were run from an isolated extraction
  of the release bundle, reproducing `verification.txt` exactly.
- The eight-page PDF was compiled without unresolved references or
  typesetting warnings and visually inspected. Its bibliography links
  were checked. The source author block reads
  `Research note prepared with Codex`.

The generating Codex assistant performed these checks in the development
session. They are not an independent mathematical audit.

## Publication integrity

The first publication copied the completed local paper, source, programs,
and results without changes. The authorship correction of 21 October 2026
removes the account name from the byline and the citation to v6, whose
paper also uses "Research note prepared with Codex." The mathematical
text, programs, and recorded results are unchanged. The PDF was rebuilt,
rendered, and visually inspected; the bundle and checksums were regenerated.
The unchanged computation files were checked against the original release;
the mathematical checks were not rerun for this authorship-only correction.

This correction retains `elementary-v0.1.0`. Its release downloads contain
the corrected files; the original tag and Git history preserve the first
publication. The bundle manifest covers its payload; the downloadable
release checksums identify the PDF and ZIP assets.

The subsequent review-status update of 21 October 2026 records the
completed AI-model cross-check in the paper and documentation under
the same version number. It changes no mathematics, programs, or numerical
results. The PDF was rebuilt and visually checked, and the bundle and
checksums were updated. The original tag retains the status at publication.

The documentation update of 26 October adds the external formalization
and clarifies terminology. The current source manifest reflects these
documentation changes; the published PDF and ZIP, with the ZIP's original
manifest, remain unchanged.

## Recording subsequent reviews

Record the reviewed tag or commit, date, reviewer/model when supplied,
scope, findings, and any correction. Preserve the first publication
snapshot and distinguish later review evidence from the status at release.
