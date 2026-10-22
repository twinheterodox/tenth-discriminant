# Historical companion: review and verification

## historical-v0.1.0 - Weber replacement, 22 October 2026

**No independent audit verdict is asserted for this reconstruction.**
The mathematical proof and the proposed historical cutoff `N ≤ 1891`
require separate review. Earlier checks of other papers do not cover
this modular argument or its historical admissibility.

The exact checker and recorded output are unchanged from the completed
local Weber draft. Its checks cover:

- Weber multiplier conversion for all 1,024 admissible matrix residues;
- the complete root-selection residue calculation and representative
  exact modular matrix identities;
- cubic resultants, coefficient substitution, and Euler descent identities;
- the rational exponential bound, finite discriminant exclusions, and
  reduced-form enumeration for the nine surviving discriminants.

An isolated extraction of the replacement release bundle reproduces
[verification.txt](verification.txt). Its file checksums were also checked.
The paper was rebuilt and its rendered layout checked. The date label is
the only manuscript change from the completed local Weber draft; the
mathematical text is unchanged.

These computations do not establish the analytic modular toolkit, the
infinite descent, or historical eligibility. The code, proof, and source
audit were prepared in the same Codex session; these checks are not an
independent mathematical audit or formal verification.

The main historical issue is whether the explicit root-control repair
and Heegner's problem-specific deduction are admissible applications of
the organizing methods already published by 1891. The paper gives the
construction and identifies Weber's corresponding passages so that this
judgment can be assessed. See Section 9, Appendix C, and the
[historical source audit](historical_sources.txt).

## Superseded 1830 reconstruction

The previous paper's computational checks concerned a different,
determinant-based argument. Its historical eligibility claim is withdrawn
under the revised criterion. The earlier files and review record are
preserved at the [original publication commit](https://github.com/twinheterodox/tenth-discriminant/tree/5d358722319d90f9458a7e95fb76c4044e24f486/companions/historical)
and in Git history. This replacement retains `historical-v0.1.0` and the
existing release URLs.
