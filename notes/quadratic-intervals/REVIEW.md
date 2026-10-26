# Review and verification: quadratic-intervals-v0.1.0

Recorded 26 October 2026.

## Independent model cross-check

The repository owner supplied a report from another AI model finding
no substantive gap in the interval theorem, the logarithmic-derivative
bound, or the split-prime corollary. No model name was supplied. The
[report](cross_check.txt) preserves the assessment and identifies the
reviewed ten-page PDF and LaTeX source by SHA-256.

The report explicitly checks the cancellation between the split-prime
factorial contribution and the determinant height loss, the retained
divided-derivative factorial cost, the small-interval cases, and the
argument for positivity of `L(1,chi)` before passage to `sigma = 1`.
It confirms the constant margin `C_32 + 1/2 = 17.7880528601... < 18`.

The checker reports reproducing the bundled exact calculations and
verifying eleven additional determinant norms through a separate
implementation with ordinary integer block matrices, in real and
imaginary quadratic fields. That separate implementation was not supplied
with the report and is not part of `verify_intervals.py`.

The optional residue estimate was checked as a substitution into Cairn's
equation (C13), retaining the stated external ideal-count input.
This is a model cross-check, not human peer review, formal verification,
or a determination of priority.

## Incorporated clarifications and publication scope

The report requested two presentation corrections:

- Both references to v7's factorial-divisibility section now correctly
  identify Section 4.3.
- Section 7 now explicitly states the limiting positivity, tail-density,
  and regular-part/head-mass constraints at the half-power and quarter-power
  thresholds. It displays their first-moment consequence and the model's
  values.

The second clarification expanded the paper to eleven pages. The
development assistant checked the references and displayed identities;
this expanded formulation was written after the reported model review.
Subsequent editorial changes and the release label do not change the
interval theorem, its constants, or its two principal corollaries.
The release copy preserves the completed local draft's mathematical body.

## Exact computations supplied with the note

[verify_intervals.py](verify_intervals.py) uses only Python's standard
library. Its output is recorded in [checks.txt](checks.txt):

- Rational bounds for the arithmetic error and final constant.
- 55,091 finite row-sum lower bounds and 2,286 separately expanded
  row-sum identities.
- 25 exact quadratic-ring determinant minors with full finite-field ranks.
- 85 inert-prime and 51 split-prime valuation checks.
- 13 cases where omission of the column-factorial cost would give a
  false divisibility claim; the corrected bound passes.

The largest tested minor is 52 by 52. These are exact finite checks,
not a replacement for the proof over the infinite range. The program's
opening author-check label refers only to these computations and does
not include the separate model review above.

Publication validation reproduces the recorded output from an isolated
extraction of the release bundle, verifies the manifest hashes, and
checks the clean LaTeX build and rendered eleven-page PDF.

## External inputs

The interval proof supplies its prime estimates and determinant arguments,
using elementary quadratic arithmetic, finite fields, linear algebra,
and real analysis. The L-function consequence additionally uses the Euler
product and convergence at the real point 1. The comparison with QRH and
the optional residue deduction have the distinct external inputs stated
in the paper. No formalization of this note is supplied.
