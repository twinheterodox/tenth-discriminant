# Version 3, expanded: q < 1,000,000

**v0.3.1 · 20 October 2026 · AI-assisted research draft**

[Read the expanded ten-page proof](output/pdf/proof.pdf) ·
[LaTeX source](proof.tex) ·
[Download the proof and verification bundle](https://github.com/twinheterodox/tenth-discriminant/releases/download/v0.3.1/tenth-discriminant-v0.3.1.zip)

This is an expanded exposition of the v3 result for
[Terence Tao's tenth-discriminant challenge](https://terrytao.wordpress.com/2026/10/20/an-experimental-ai-math-challenge-using-tenth-discriminant-bounds-to-explore-arguments-ruling-out-siegel-zeroes/).
The paper now includes the background, the analytic proof, and the finite
classification in one document. Reading v1, v2, or the original v3 paper
is not required.

The bound and analytic constants are unchanged from
[v0.3.0](https://github.com/twinheterodox/tenth-discriminant/releases/tag/v0.3.0).
This patch adds explanations and a direct verifier for the remaining
range. The original v3 snapshot, PDF, bundle, and tag remain unchanged.

## Result and inputs

For a negative fundamental discriminant `D`, put `q = |D|`. Under the
specified determinant results of Banks, the paper proves

```text
h(Q(sqrt(D))) = 1  implies  q < 1,000,000.
```

An exhaustive integer check below the cutoff leaves exactly

```text
q = 3, 4, 7, 8, 11, 19, 43, 67, 163.
```

The paper also explains and carries out the reduced-form check that
each survivor has class number one.

The external inputs are Banks's determinant construction in Sections 3–4
and Lemmas 4.2, 5.1, and 6.2, including the preceding interpolation
results, in [arXiv:2610.15483v1](https://arxiv.org/html/2610.15483v1).
It also uses Theorems 6 and 9 of
[Rosser–Schoenfeld (1962)](https://doi.org/10.1215/ijm/1255631807)
and classical quadratic ideal theory and reduction of binary quadratic
forms. The needed statements and notation are included in the paper;
these external results are not independently reproved.

The argument counts primitive lattice points to bound split primes,
then compares the absolute size and prime-power divisibility of Banks's
determinant. It constructs no L-function zero and uses no Heegner method
or small-conductor zero computation.

## What the expanded paper contains

- Sections 1–2: the challenge, result, proof roadmap, discriminants,
  class number, prime splitting, and the norm lattice.
- Sections 3–5: the lattice count, primitivity sieve, partial summation,
  and explicit lower bound for the weighted sum of inert primes.
- Sections 6–8: the determinant, retained rows, degree sums, exact
  external estimates, parameter choices, and uniform contradiction.
- Section 9: the small-prime obstruction, complete finite search,
  reduction of binary quadratic forms, and the nine surviving fields.
- Section 10: reproduction commands, the exact arithmetic certificate,
  and the scope of verification.

## Reproduce the complete calculation

Run from this directory with Python 3.8 or newer. No third-party packages
or data files are needed:

```sh
python3 verify_direct_prime.py --sanity
python3 verify_finite_range.py
```

The first command reproduces the original 26 exact arithmetic checks and
22 finite sanity cases. Its output is [checks.txt](checks.txt). Omit
`--sanity` to run just the arithmetic certificate.

The second command directly checks all 124,999 integers with
`11 <= q < 1,000,000` and `q = 3 (mod 8)`. The proof shows why these
include every possible class-number-one field with `q > 8`.
For each eligible odd prime `p <= 109`, it rejects `q` when `-q` is
zero or a square modulo `p`. It then verifies fundamental discriminants
and reduced forms for the nine final survivors. Its deterministic
output is [finite_range_checks.txt](finite_range_checks.txt).

This direct finite check reads no earlier-version file and requires
neither the larger sieve nor a class-number table.

## Verification status

The arithmetic and finite checks pass. The new finite result agrees with
the retained C++ and Python computations covering `q < 10^10`.
The expanded PDF was compiled, rendered, and all ten pages visually inspected.

**Both v3.0 and this expanded paper passed cross-checks by another AI
model,** confirmed on 20 October 2026. These are not human peer review
or formal verification. The finite
sanity examples do not prove the general analytic lemmas, and the
programs do not verify Banks's interpolation theorem.

See [the publication-time review record for this release](REVIEW.md) and the
[current repository review record](https://github.com/twinheterodox/tenth-discriminant/blob/main/REVIEW.md).

Review terminology was clarified on 26 October 2026. The published
paper, bundle, and fixed tag remain unchanged.

## Optional larger finite computation

The original finite-verification programs and recorded outputs are
included unchanged. To rerun them:

```sh
g++ -O2 -std=c++17 -Wall -Wextra -pedantic verify_sieve.cpp -o verify_sieve
./verify_sieve
python3 verify_independent.py
```

Recorded outputs: [C++](sieve_cpp_output.txt) ·
[Python](sieve_python_output.txt). Their runtime lines are machine
dependent. The older Python script also contains checks for the earlier
theta argument; those are not inputs to the v3 proof.

## Rebuild the paper

With the LaTeX packages named in the source:

```sh
mkdir -p output/pdf
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=output/pdf proof.tex
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=output/pdf proof.tex
```

## Provenance and AI disclosure

Codex prepared the v3 derivation, this expanded exposition, and all
verification programs. Agreement between algorithms is a computational
check; it is not an independent mathematical review. No Lean formalization
is supplied.

[Source provenance](sources.json) records source URLs and snapshot
hashes. Third-party research snapshots are not redistributed.
[Artifact checksums](artifact-manifest.json) cover this version's files;
the [repository manifest](https://github.com/twinheterodox/tenth-discriminant/blob/v0.3.1/artifact-manifest.json)
also covers the bundle. The fixed release is
[v0.3.1](https://github.com/twinheterodox/tenth-discriminant/releases/tag/v0.3.1).
