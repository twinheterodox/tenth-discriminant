# Review and verification by version

This log records the scope of available evidence. It does not certify
Banks's external theorem or intermediate lemmas.

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

**The new refinement has not yet received a separate-model mathematical
cross-check.** The reported v1 cross-check does not cover the new estimates
or the new application of Banks's intermediate lemmas.

See the [v2 verification record](versions/v2/REVIEW.md) for component-level
scope. No independent human review or Lean formalization is recorded here.

## Recording future reviews

Record the reviewed version or commit, date, reviewer/model when available,
claims checked, findings, and any corrective commit. Preserve earlier
records and add corrections explicitly when evidence changes.
