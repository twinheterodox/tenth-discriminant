# Verification record — v0.2.0

Recorded on 20 October 2026. This record applies to the cumulative v2 paper
and separates inherited evidence from checks of the new refinement.

| Component | Evidence | Scope |
|---|---|---|
| New numerical constants | 23 exact rational checks pass; [output](improved_bound_checks.txt) | Finite inequalities and parameter checks; not the analytic proof |
| New analytic refinement | Written and checked by the generating Codex assistant | Separate-model mathematical review has not yet been completed |
| Original analytic argument | Repository owner reports a cross-check with a different frontier model | Applies to v1; no detailed review report is bundled here |
| Finite exclusion | Two algorithms agree; original code and outputs copied byte-for-byte from v1 | Full original range below `10^10`; reduced forms check the nine survivors |
| Banks's external results | Dependencies and their use are stated in the paper | No independent verification of Banks's full argument by this project |
| PDF | LaTeX compiled; all pages rendered and visually inspected | Presentation and cross-references |

The arithmetic certificate uses exact fractions and a justified Taylor-tail
bound for exponential comparisons. Its success is not an independent model
review or a formalization of the analytic proof.

Codex generated the proof text and all three programs. No independent human
review or Lean formalization is recorded in this repository.

Future reviews should identify the exact version or commit reviewed,
the reviewer or model when available, the claims examined, findings, and
resulting corrections. A review of v1 does not automatically extend to v2.
