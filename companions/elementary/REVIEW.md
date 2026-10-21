# Review and verification: elementary-v0.1.0

**Independent mathematical review is pending.** This companion is a
research draft; checks of other papers in the repository do not cover it.
No formal verification is supplied.

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
- Both programs have been run from an isolated extraction of the release
  bundle, reproducing `verification.txt` exactly.
- The eight-page PDF was compiled without unresolved references or
  typesetting warnings and visually inspected. Its bibliography links
  were checked. The source author block reads `twinheterodox` followed by
  `Research note prepared with Codex`.

The generating Codex assistant performed these checks in the development
session. They are not an independent mathematical audit.

## Publication integrity

The paper, LaTeX source, both verification programs, and recorded results
are byte-identical to the completed local draft. Publication adds the
companion README, review record, changelog, and checksum manifest. The
bundle manifest covers its payload; the downloadable release checksums
identify the PDF and ZIP assets.

## Recording subsequent reviews

Record the reviewed tag or commit, date, reviewer/model when supplied,
scope, findings, and any correction. Preserve the first publication
snapshot and distinguish later review evidence from the status at release.
