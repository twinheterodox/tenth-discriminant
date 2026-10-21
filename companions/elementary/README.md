# An elementary determinant bound for the tenth discriminant

**Analytic cutoff: `q < 32,768 = 2^15`.**

Research note prepared with Codex

**[Read the eight-page paper](output/pdf/elementary-companion.pdf)** ·
[LaTeX source](proof.tex) ·
[Download the proof and verification bundle](elementary-v0.1.0.zip) ·
[Release and downloads](https://github.com/twinheterodox/tenth-discriminant/releases/tag/elementary-v0.1.0)

This companion to [Tao's tenth-discriminant challenge](https://terrytao.wordpress.com/2026/10/20/an-experimental-ai-math-challenge-using-tenth-discriminant-bounds-to-explore-arguments-ruling-out-siegel-zeroes/)
prioritizes a simple, self-contained proof with a comfortably enumerable
cutoff. It proves that an imaginary quadratic field of class number one
has absolute fundamental discriminant `q < 32,768`. An integer residue
sieve and reduced-form enumeration leave the nine absolute discriminants
`3, 4, 7, 8, 11, 19, 43, 67, 163`.

**The elementary companion has passed independent mathematical verification,**
confirmed on 21 October 2026. The exact constant checks and exhaustive
finite sieve also pass. The [review record](REVIEW.md) distinguishes the
reported independent verification from the computations performed in the
development session. No formal verification is supplied.

## The argument

Class number one makes split primes sparse: each is represented by the
quadratic norm form. A direct count of these representations supplies an
inert prime `R` in `(q^4, q^5]`. The proof then uses:

- A rectangular interpolation grid with at least `4R` points.
- Green's derivative determinant, with `S = floor(R/12)` and
  `J = ceil(R/48)`.
- Van Dijk's finite-field proof that the determinant is nonzero.
- The basic Frobenius relation at each inert prime, giving strong
  divisibility of the same determinant.
- An elementary size bound and one endpoint comparison at `q = 32,768`.

The ordinary-prime estimates are proved using factorials and binomial
coefficients. Reproduction requires no parameter search, special-function
evaluation, or construction of the determinant. Standard quadratic ideal
theory, finite fields, Hadamard's inequality, and elementary analysis are
the background inputs.

## Reproduction

Run with Python 3, using only its standard library:

```sh
python3 verify_constants.py
python3 verify_finite.py
```

Run without `-O` or `-OO`, since assertions express the checks.

- [verify_constants.py](verify_constants.py) checks the endpoint constants
  by rational arithmetic. The final comparison has exact margin
  `143/96 - 846/575 = 1009/55200`. Monotonicity arguments in the paper
  cover the whole infinite range above the cutoff.
- [verify_finite.py](verify_finite.py) tests all 4,095 candidate integers
  below the cutoff using primes at most 31, verifies its residue tables
  by Euler's criterion, and enumerates reduced forms for the nine survivors.
- [verification.txt](verification.txt) contains the reproduced outputs.
- [MANIFEST.json](MANIFEST.json) records the checksums of the publication
  files. The ZIP includes all of them and the manifest.

To build the PDF with LaTeX:

```sh
mkdir -p output/pdf
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=output/pdf -jobname=elementary-companion proof.tex
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=output/pdf -jobname=elementary-companion proof.tex
```

## Sources and AI disclosure

The paper cites each mathematical contribution where it is used:
Silberman's discussion of the classical inertness obstruction in Section 1;
Pratt's norm-counting suggestion in Section 3; Green's derivative determinant
and divisibility in Section 4; van Dijk's nonvanishing argument, including
Green's report of Pescador's unpublished related work, in Section 4.1;
and Pratt's residue sieve in Section 6.

The principal sources are [Green's paper](https://hexagonmath.org/2610.00311v2),
[van Dijk's paper](https://hexagonmath.org/2610.00409v1), and
[Pratt's suggestion to combine them with norm counts](https://terrytao.wordpress.com/2026/10/20/an-experimental-ai-math-challenge-using-tenth-discriminant-bounds-to-explore-arguments-ruling-out-siegel-zeroes/#comment-698476).
All determinant steps used here are proved in the note. Its derivation,
exposition, and programs were developed with OpenAI Codex. The paper's
acknowledgements also retain the source papers' own AI attributions.

## Versioning and citation

This is **`elementary-v0.1.0`**, the first release in a separate companion
series. The numbered series v1-v6 pursues progressively smaller cutoffs;
[v6](https://github.com/twinheterodox/tenth-discriminant/releases/tag/v0.6.0)
has the stronger bound `q < 570`. This paper gives a simpler argument that
is independent of all earlier versions. Each series has its own revisions
and review status.

For citation, use:

> *An elementary determinant bound for the tenth discriminant*,
> elementary-v0.1.0, 21 October 2026. Research note prepared with Codex.

[Original publication snapshot](https://github.com/twinheterodox/tenth-discriminant/tree/elementary-v0.1.0/companions/elementary) ·
[Release](https://github.com/twinheterodox/tenth-discriminant/releases/tag/elementary-v0.1.0) ·
[Companion changelog](CHANGELOG.md)

The current paper and release downloads include the authorship correction
and completed-verification status dated 21 October 2026: the byline is
solely "Research note prepared with Codex." The account name is also
omitted from the citation to v6, whose paper uses the same byline. The
mathematical argument, verification programs, and results are unchanged.
These updates retain
`elementary-v0.1.0`; the original publication tag and Git history preserve
the first files. Earlier local experiments are not inputs to this release
or part of its bundle.
