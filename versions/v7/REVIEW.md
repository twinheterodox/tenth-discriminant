# Review and verification: v0.7.0

Recorded 26 October 2026.

## Mathematical review status

The new uniform exclusion for `q >= 2,000` and the consolidated paper
have **not yet received a separate AI-model cross-check**. They were
derived and checked by the same Codex assistant that prepared this release.
No independent human review or formal verification is claimed.

V6 has a reported successful second-model cross-check and an additional
AI-assisted audit coordinated by Henric Larsson. The owner's
[public confirmation](https://terrytao.wordpress.com/2026/10/20/an-experimental-ai-math-challenge-using-tenth-discriminant-bounds-to-explore-arguments-ruling-out-siegel-zeroes/comment-page-1/#comment-698514)
and Larsson's
[clarification](https://terrytao.wordpress.com/2026/10/20/an-experimental-ai-math-challenge-using-tenth-discriminant-bounds-to-explore-arguments-ruling-out-siegel-zeroes/comment-page-1/#comment-698595)
give the scope. His clarification says no mathematical error or certificate
correction was required; the repairs concerned the audit process.

Those reviews concerned the earlier proof, including its v5 dependency
above 2,000. They support the retained bounded calculation but do not
automatically review the new tail or the generalized common proposition.
The repository owner's earlier descriptions of independent verification
refer to model cross-checks, not human peer review.

## What changed mathematically

The common determinant estimates are now stated with explicit local
geometry and scale hypotheses, rather than under a standing bounded-band
assumption. The quadratic-tail subtraction can be zero, and the extra
inert-prime gains can use any fixed cutoff below `q/4`. A pointwise
factorial-refinement statement is included before its band-uniform form.

The new tail applies this proposition for `R >= q^2`, using one fixed set
of rational constants, and proves the required auxiliary-prime supply.
It then uses one previously established factorial refinement and a direct
upper bound for the same smoothed sum. Monotonicity supplies the infinite
range from an endpoint computation. The [consolidation record](CONSOLIDATION.md)
identifies these obligations for a reviewer.

## Development-session computational evidence

- `verify_tail.py`: 34 exact rational-interval checks passed. They cover
  the auxiliary-prime margin, geometry, determinant constants, one-step
  factorial refinement, and the normalized endpoint inequality. The latter
  has gap greater than `0.018345`. The general monotonicity and mathematical
  deductions are proved in the paper, not inferred from sampled values.
- `verify_v6.py`: all 429 grouped checks passed, including 1,258 cells for
  the dependence on `q`. All five band JSON files and the combined output
  reproduce v6.1 byte-for-byte. The minimum gap exceeds `0.010389`.
- `verify_structures.py`: all 101,524 finite exact cases passed. These
  exercise algebraic identities and inequalities and do not replace their
  general proofs.
- `verify_finite.py`: all 70 remaining candidate integers were checked;
  the nine survivors have one reduced form each.

[REPRODUCTION.json](REPRODUCTION.json) records the commands and preservation
checks, including a complete isolated replay of the packaged programs
and inputs with matching outputs. The [release validation](VALIDATION.json)
records the clean LaTeX build and visual inspection of all 23 pages. Earlier papers, programs, parameters,
certificates, PDFs, tags, and release assets have not been modified.

## External inputs and formalization scope

The ordinary-prime estimates, standard quadratic ideal and reduced-form
theory, and classical analytic identities remain stated background inputs.
No theorem from v4 or v5 is imported. All certificate utilities are local
to this version and use the Python standard library.

Peter W. Murphy's reported Lean/nanoda verification applies to an adaptation
of the elementary companion. It does not formalize v7, v6, or the new tail.
Numerical certification and agreement with an older output are distinct
from proof-assistant verification of the mathematical argument.
