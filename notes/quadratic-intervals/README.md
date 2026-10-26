# A uniform interval bound for inert-prime mass

Research note prepared with Codex · **quadratic-intervals-v0.1.0** · 26 October 2026

**[Read the eleven-page paper](output/pdf/quadratic-intervals.pdf)** ·
[LaTeX source](intervals.tex) ·
[Paper and verification bundle](quadratic-intervals-v0.1.0.zip) ·
[Release and downloads](https://github.com/twinheterodox/tenth-discriminant/releases/tag/quadratic-intervals-v0.1.0)

For every primitive nonprincipal real character `chi` of conductor `q`,
and every `1 <= Y <= X`, the paper proves

```text
sum_{Y < p <= X, chi(p) = -1} log(p)/p
    <= (1/2) log(X/Y) + (1/4) log(q) + log(log(q)+33) + 18.
```

Here `p` runs over ordinary integer primes, `chi(p) = -1` means that
`p` is inert in the associated quadratic field, and all logarithms are
natural. Both real and imaginary quadratic fields, of every class number,
are included. For a fixed field and ratio `A > 1`, the allowance above
`(1/2) log(A)` is the same on every interval `(Y,AY]`, however large `Y`
becomes.

The proof combines divided derivatives with factorial divisibility at
split primes. The two contributions cancel a loss that would otherwise
grow with the interval ratio. The resulting explicit error depends only
on the conductor. The determinant estimates are proved in the paper;
earlier repository versions provide context and provenance rather than
prerequisite proofs.

## Consequences and scope

- The logarithmic derivative of the associated Dirichlet L-function
  satisfies `L'(sigma,chi)/L(sigma,chi) <= (1/2) log(q) + 3 log(log(q)+33) + 45`
  for every real `sigma >= 1`.
- For every `Y >= 1`, there is a split prime in
  `(Y, exp(53) sqrt(q) (log(q)+33)^4 Y]`.
- An explicit continuous model satisfies the leading interval inequalities
  and specified positivity and counting constraints while retaining a
  residue of order `1/log(q)`. Section 7 states precisely the relaxation
  to which this limitation applies.
- An optional residue estimate uses a separately cited ideal-count input
  from Cairn's manuscript. That input is not required for the interval
  theorem or the two corollaries above.

Endpoint independence for a fixed field is classical. The contribution
studied here is an explicit conductor-dependent estimate and its
elementary determinant mechanism. The introduction supplies classical
comparisons and derives an asymptotically stronger interval estimate
from QRH as an external input; QRH is not used in the determinant proof.
The source comparison does not establish priority for the exact bound.

## Review status

**A cross-check by another AI model found no substantive gap in the main
theorem or its two principal corollaries.** The report was supplied on
26 October 2026 and concerned the ten-page draft and its source.
The eleven-page publication incorporates the requested section-reference
corrections and explicit model counting constraints. The
[review record](REVIEW.md) separates that reviewed snapshot, subsequent
clarifications, and the author's exact computations. The
[supplied report](cross_check.txt) includes the reviewed artifact hashes.

This is a model cross-check, not human peer review or formal verification.
The additional eleven determinant norms reported by the checker are
distinct from the cases in the bundled verification program.

## Reproduction

Use Python 3 with its standard library, without `-O` or `-OO` because
assertions express the checks:

```sh
python3 verify_intervals.py
```

The output should match [checks.txt](checks.txt) exactly. The program checks
25 determinant minors and finite-field ranks, 136 prime valuations,
55,091 finite row-sum bounds, 2,286 independently expanded identities,
and rational constant inequalities. These finite computations exercise
the proof's algebraic mechanisms; the paper supplies the general argument.
The output's opening label describes the scope of that author-written
program, not the separate model review.

Build the paper with LaTeX:

```sh
mkdir -p output/pdf
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=output/pdf -jobname=quadratic-intervals intervals.tex
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=output/pdf -jobname=quadratic-intervals intervals.tex
```

[MANIFEST.json](MANIFEST.json) records the publication files' sizes and
SHA-256 hashes. The release supplies a ZIP containing the paper, source,
program, outputs, documentation, and license, with download checksums.

## Attribution and citation

The paper cites OpenAI's originating polynomial argument, Green's
derivative determinant, van Dijk's finite-field nonvanishing argument,
Kominers's broader Frobenius-class estimates, the v7 factorial refinement,
Cairn's quadratic L-value work, and the relevant classical analytic
comparisons beside the mathematics they inform. The work arose from
[Tao's challenge](https://terrytao.wordpress.com/2026/10/20/an-experimental-ai-math-challenge-using-tenth-discriminant-bounds-to-explore-arguments-ruling-out-siegel-zeroes/).
The derivation, exposition, and verification program were prepared with
OpenAI Codex in collaboration with the repository owner.

For citation:

> *A uniform interval bound for inert-prime mass*,
> quadratic-intervals-v0.1.0, 26 October 2026.
> Research note prepared with Codex.

[Fixed publication snapshot](https://github.com/twinheterodox/tenth-discriminant/tree/quadratic-intervals-v0.1.0/notes/quadratic-intervals) ·
[Release](https://github.com/twinheterodox/tenth-discriminant/releases/tag/quadratic-intervals-v0.1.0) ·
[Changelog](CHANGELOG.md)

This note has its own release series. The numbered tenth-discriminant
series retains [v0.7.0](https://github.com/twinheterodox/tenth-discriminant/releases/tag/v0.7.0)
as its current consolidated proof with `q < 570` and a complete finite
classification. This general-field note introduces no new classification
cutoff.

The paper, source, documentation, and verification material are licensed
under [Apache 2.0](LICENSE); see [NOTICE](NOTICE) for attribution.
