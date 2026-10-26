# Version 2: analytic cutoff q < 5 × 10⁷

**v0.2.0 · 20 October 2026 · AI-assisted draft for mathematical review**

[Read the complete cumulative proof](output/pdf/proof.pdf) ·
[LaTeX source](proof.tex) ·
[Download this version's proof and verification bundle](tenth-discriminant-v0.2.0.zip)

This version contains the original argument, the refinement, and the finite
classification in one paper. It can be read without opening the v1 paper.
The [original v1 snapshot](https://github.com/twinheterodox/tenth-discriminant/blob/v0.2.0/versions/v1/README.md) remains unchanged. The
[mathematical changelog](https://github.com/twinheterodox/tenth-discriminant/blob/v0.2.0/CHANGELOG.md) and [review record](REVIEW.md)
identify what changed and what has been checked.

## Result and dependencies

Let `D < 0` be a fundamental discriminant and `q = |D|`. Assuming the
intermediate results of Banks listed below, the paper derives

```text
h(Q(sqrt(D))) = 1  implies  q < 50,000,000.
```

The external inputs are Lemma 4.2, Lemma 5.1, and Corollary 6.3 of
[Banks, arXiv:2610.15483v1](https://arxiv.org/html/2610.15483v1),
including their preceding determinant construction, prime-bias input,
and hypotheses. This project does not independently establish those
results. The original argument, retained in the paper, instead takes
Banks's stated Theorem 1.1 for `q >= 10^10` as its external input.

The exact integer sieve leaves the same nine absolute fundamental
discriminants:

```text
3, 4, 7, 8, 11, 19, 43, 67, 163.
```

The 200-fold improvement concerns the analytic cutoff. The final finite
classification was already obtained in v1.

## What changed mathematically

- The refined theta argument proves `1 - beta < 2/sqrt(q)` for
  `q >= 49,000,000`, using the integer lattice points `±1, …, ±30`.
- Banks's intermediate estimates, with `H = 10^9` and `N = q^18`, give
  `(1 - beta) log q > 0.00509` for `q >= 50,000,000`.
- At that threshold the theta estimate gives
  `(1 - beta) log q < 0.00502`, a contradiction.
- A new arithmetic certificate checks the finite constants with exact
  rational arithmetic and rigorous exponential bounds.

The original sieve programs and recorded outputs are copied byte-for-byte
from v1. They cover the larger range `q < 10^10`, which includes the entire
remaining range for v2. No new claim about a rerun or a smaller sieve run
is made. No Heegner method, class-number database, or Banks small-conductor
zero computation is used.

## Verification status

**The v2 refinement passed a cross-check by a different frontier AI model,**
confirmed on 20 October 2026. This is not human peer review or formal
verification. Its 23 exact arithmetic checks pass. The cumulative PDF has
been rendered and visually inspected; that checks presentation.

The repository owner reports that the original v1 mathematical argument
was also cross-checked with a different frontier model. The
[current review record](../../REVIEW.md) documents the separate v1 and v2
checks and the terminology clarified on 26 October. The original
[publication-time record](REVIEW.md), PDF, and bundle are preserved.

## Reproduce

Run from this directory. The arithmetic certificate uses only Python's
standard library:

```sh
python3 verify_improved_bound.py
```

Its recorded output is [improved_bound_checks.txt](improved_bound_checks.txt).
To reproduce the inherited finite computation, use a C++17 compiler and
Python 3.8 or newer:

```sh
g++ -O2 -std=c++17 -Wall -Wextra -pedantic verify_sieve.cpp -o verify_sieve
./verify_sieve
python3 verify_independent.py
```

Recorded v1 outputs: [C++ sieve](sieve_cpp_output.txt) ·
[Python sieve and reduced forms](sieve_python_output.txt).

To rebuild the cumulative PDF with the LaTeX packages named in `proof.tex`:

```sh
mkdir -p output/pdf
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=output/pdf proof.tex
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=output/pdf proof.tex
```

## Provenance and AI disclosure

Codex produced the derivations, write-up, documentation, and all three
verification programs. The two original sieve algorithms were written by
the same assistant; their agreement is a computational check, not an
independent analytic review. No Lean formalization is supplied.

[Source provenance](sources/manifest.json) is inherited from v1. It also
records a Green manuscript consulted during the original research; that
manuscript is not a proof input here. Third-party source snapshots are not
redistributed.

[Artifact checksums](artifact-manifest.json) cover this version's individual
files. The [repository manifest](https://github.com/twinheterodox/tenth-discriminant/blob/v0.2.0/artifact-manifest.json) also covers
the downloadable bundle. The fixed release is
[v0.2.0](https://github.com/twinheterodox/tenth-discriminant/releases/tag/v0.2.0).
