# Tenth-discriminant bounds

This is an AI-assisted contribution to
[Terence Tao's tenth-discriminant challenge](https://terrytao.wordpress.com/2026/10/20/an-experimental-ai-math-challenge-using-tenth-discriminant-bounds-to-explore-arguments-ruling-out-siegel-zeroes/).
The aim is to obtain explicit bounds for a hypothetical tenth imaginary
quadratic field of class number one from arguments ruling out Siegel
zeroes, without using Heegner's solution. The repository records the
arguments, computations, and successive improvements so that they can be
examined and cited in the discussion.

For a negative fundamental discriminant `D`, write `q = |D|`. The versions
develop different ways to combine the class-number-one assumption with
results from [Banks, arXiv:2610.15483v1](https://arxiv.org/abs/2610.15483v1).
Versions 1 and 2 construct a real zero using a classical theta integral
and contradict a zero-free estimate. Version 3 instead counts primitive
lattice points to bound split primes directly, then uses Banks's
determinant argument to rule out large `q`. Each approach gives an explicit
analytic cutoff. Exact integer sieves and reduced-form enumeration handle
the remaining finite range, leaving the nine absolute fundamental
discriminants `3, 4, 7, 8, 11, 19, 43, 67, 163`.

The cited results from Banks are external inputs, with the precise
dependencies stated in each version. Codex prepared the derivations,
write-ups, and verification programs; the review record identifies the
checks completed for each version.

**Current research draft: v0.3.0, with analytic cutoff `q < 1,000,000`.**

## Versions and improvements

As bounds improve, new results are added as numbered versions, each with
its own proof and verification files. Published snapshots and
release links are preserved, so earlier comments can continue to cite the
exact argument they discussed. This README is the entry point to the
latest result and the version history; the changelog records what changed
mathematically. The original v1 README is retained below as a historical
snapshot.

| Version | Analytic cutoff | Paper and files | Mathematical review status |
|---|---|---|---|
| **v3 · v0.3.0** | **`q < 10^6`** | [Proof of the new cutoff](versions/v3/output/pdf/proof.pdf) · [Source and reproduction](versions/v3/README.md) · [Release](https://github.com/twinheterodox/tenth-discriminant/releases/tag/v0.3.0) | 26 exact arithmetic checks and 22 finite sanity cases pass; independent mathematical cross-check pending |
| **v2 · v0.2.0** | `q < 5 × 10^7` | [Complete cumulative proof](versions/v2/output/pdf/proof.pdf) · [Source and reproduction](versions/v2/README.md) · [Release](https://github.com/twinheterodox/tenth-discriminant/releases/tag/v0.2.0) | Mathematical cross-check with a different frontier model passed; 23 exact arithmetic checks pass |
| **v1 · v0.1.0** | `q < 10^10` | [Original proof](versions/v1/output/pdf/proof.pdf) · [Unchanged original snapshot](versions/v1/README.md) · [Release](https://github.com/twinheterodox/tenth-discriminant/releases/tag/v0.1.0) | Different-frontier-model cross-check reported by the repository owner; see the review record |

[Mathematical changelog](CHANGELOG.md) · [Review record by version](REVIEW.md)

The improvements change the analytic cutoff. The finite classification
remains `3, 4, 7, 8, 11, 19, 43, 67, 163`, using the original finite
verification. Version 1 takes Banks's Theorem 1.1 as an external input.
Version 2 uses Lemma 4.2, Lemma 5.1, and Corollary 6.3. Version 3 uses
Lemma 4.2, Lemma 5.1, and Lemma 6.2 directly, together with explicit prime
estimates from Rosser–Schoenfeld. Each use includes the preceding
construction and hypotheses stated in the corresponding paper. These
external results are not independently proved here.

The v3 paper proves the new analytic cutoff and reuses the earlier finite
classification; its bundle includes the original finite-verification
programs and outputs. Its independent mathematical cross-check is pending.
The completed different-frontier-model cross-check of v2, confirmed on
20 October 2026 after publication, applies to v2. The
[current review record](REVIEW.md) records later checks; fixed release
files retain their status at publication. All releases are research drafts.

## Fixed versions for citation

- [v0.1.0: original published commit](https://github.com/twinheterodox/tenth-discriminant/tree/v0.1.0)
- [v0.2.0: cumulative refined paper and files](https://github.com/twinheterodox/tenth-discriminant/tree/v0.2.0/versions/v2)
- [v0.3.0: direct split-prime proof and files](https://github.com/twinheterodox/tenth-discriminant/tree/v0.3.0/versions/v3)

The original proof, programs, outputs, and bundle remain at their existing
root paths. The `versions/v1/` directory is an exact copy of all tracked
files in the original commit `b30549663b6d2660b2df3c916822802774e2486d`.
The [current repository manifest](artifact-manifest.json) records file
checksums; each version also retains its own manifest.

---

## Original README — v1, as published

> The following text is retained verbatim as a historical snapshot.
> Its review and publication statements describe that snapshot. Subsequent
> review information is recorded in [REVIEW.md](REVIEW.md); current work is
> documented in [v3](versions/v3/README.md).

# An explicit tenth-discriminant bound from Banks's zero-free theorem

**Draft for mathematical review · 20 October 2026**

This is an AI-assisted candidate contribution to
[Terence Tao's tenth-discriminant challenge](https://terrytao.wordpress.com/2026/10/20/an-experimental-ai-math-challenge-using-tenth-discriminant-bounds-to-explore-arguments-ruling-out-siegel-zeroes/).
It takes the large-conductor assertion in Banks,
[arXiv:2610.15483v1, Theorem 1.1](https://arxiv.org/html/2610.15483v1),
as an external theorem. Neither that theorem nor the analytic argument in
this note has received an independent mathematical audit as part of this
project.

**[Read the five-page proof (PDF)](output/pdf/proof.pdf)** ·
[LaTeX source](proof.tex) ·
[Download the proof and verification bundle](tenth-discriminant-banks.zip)

## Claimed result and dependency

Let `D < 0` be a fundamental discriminant and `q = |D|`. Using Banks's stated
bound

```text
q >= 10^10 and L(beta, chi) = 0 with 0 < beta < 1
    imply (1 - beta) log q >= 3/1000
```

for primitive real characters of conductor `q`, the note derives

```text
h(Q(sqrt(D))) = 1  implies  |D| < 10^10.
```

An exhaustive integer sieve below this threshold leaves exactly

```text
|D| = 3, 4, 7, 8, 11, 19, 43, 67, 163.
```

These are absolute fundamental discriminants. The corresponding positive
squarefree radicands are `1, 2, 3, 7, 11, 19, 43, 67, 163`.

The analytic bridge uses Poisson summation and a theta integral to show that
class number one with `q >= 10^10` would produce a real zero satisfying
`1 - beta < 10/sqrt(q)`. This contradicts the quoted theorem.

The finite calculation uses the necessary condition that every prime
`p < q/4` is inert. Two algorithms, using primes at most `109`, check all
remaining candidates. Reduced-form enumeration verifies class number one
for each surviving field.

## Reproduce the finite calculation

Requirements: a C++17 compiler and Python 3.8 or newer. The Python program
uses only the standard library.

```sh
g++ -O2 -std=c++17 -Wall -Wextra -pedantic verify_sieve.cpp -o verify_sieve
./verify_sieve
python3 verify_independent.py
```

Both programs report:

- wheel modulus `2042040`, with `1440` permitted residue classes;
- `7,051,769` candidates checked in `[437, 10^10)` and no survivors;
- small survivors `11, 19, 43, 67, 163`.

The C++ program builds a CRT wheel and tests individual integers against
tables of quadratic residues. The Python program scans the initial wheel
directly, uses Euler's criterion, and intersects periodic bitsets. It also
checks the reduced forms of the nine fields and the rational inequalities
used in the analytic argument.

Recorded outputs:
[C++](sieve_cpp_output.txt) · [Python](sieve_python_output.txt).
Elapsed times vary by machine.

## Rebuild the proof

With a LaTeX installation containing the packages named in `proof.tex`:

```sh
mkdir -p output/pdf
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=output/pdf proof.tex
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=output/pdf proof.tex
```

The distributed PDF was rendered and its five pages visually inspected.

## Scope, verification, and AI disclosure

The note, both programs, and this repository documentation were prepared
with OpenAI Codex. The programs use different algorithms but were written
by the same assistant. Their agreement checks the computation; it is not
an independent review of the analytic proof.

The project does not reprove Banks's theorem. Banks's small-conductor
extension by a separate computation is not used. The deduction does not
use Heegner's solution, Heegner points, or a class-number database.
No novelty or optimality claim is made for the classical theta method.
No Lean formalization or independent human/model review has been completed.

The [proof](output/pdf/proof.pdf) identifies the mathematical dependencies.
[Source provenance](sources/manifest.json) records primary-source URLs and
hashes of local research snapshots; third-party snapshots are not
redistributed. [Artifact checksums](artifact-manifest.json) identify the
distributed files. This repository makes the draft available for review;
it does not itself submit a comment to Tao's blog.
