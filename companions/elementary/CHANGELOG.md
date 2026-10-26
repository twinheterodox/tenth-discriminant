# Elementary companion changelog

## External Lean adaptation and review terminology — 26 October 2026

- Links Peter W. Murphy's external Lean adaptation, paper, verification
  record, and archived release. Murphy reports acceptance by Lean and
  nanoda for the full classification using this companion's cutoff.
- Distinguishes his adapted formal proof from the original paper: some
  estimates and the converse use different arguments. This is not a
  formalization of the numbered series or historical reconstruction.
- Clarifies that the verification confirmed on 21 October was a
  cross-check by a second AI model, not human peer review or formal verification.
- Updates the current README, review record, and source manifest. The
  paper, programs, numerical results, published bundle, and release tag
  remain unchanged; no version increment is made.
- Records external verification reports without claiming to have rerun
  Murphy's build or established Mathlib acceptance.

Earlier entries retain their publication wording. See [REVIEW.md](REVIEW.md)
for the current terminology, source links, and scope.

## elementary-v0.1.0 - independent verification, 21 October 2026

- Records that the elementary companion passed independent mathematical
  verification, as confirmed on 21 October 2026.
- Updates the paper, documentation, and existing release downloads under
  the same version number. The mathematics, programs, and results are unchanged.
- Retains the original tag and Git history, including the status at publication.

## elementary-v0.1.0 - authorship correction, 21 October 2026

- Uses only `Research note prepared with Codex` as the paper's byline.
- Removes the account name from the suggested citation and release
  metadata, and from the citation to v6, which has the same unnamed byline.
- Leaves the mathematical argument, programs, and results unchanged.
- Updates the existing release downloads under the same version number.
  The original tag and Git history preserve the first publication.

## elementary-v0.1.0 - 21 October 2026

First publication of *An elementary determinant bound for the tenth
discriminant*, with analytic cutoff `q < 32,768 = 2^15`.

- Gives a self-contained specialization of the derivative determinant
  method, relative to the stated classical background.
- Proves the ordinary-prime estimates by factorial and binomial arguments.
- Finds an auxiliary inert prime through a weighted interval estimate,
  uses an ordinary rectangular grid, and concludes with one endpoint
  comparison.
- Includes exact rational checks and a complete sieve of 4,095 candidates,
  followed by reduced-form enumeration of the nine survivors.
- Places mathematical citations at their point of use and gives the
  authorship line `twinheterodox - Research note prepared with Codex`.
- Records independent mathematical review as pending.

This companion has its own release series. The numbered versions and
their bounds, including v6 with `q < 570`, are preserved.

[Fixed release](https://github.com/twinheterodox/tenth-discriminant/releases/tag/elementary-v0.1.0).
