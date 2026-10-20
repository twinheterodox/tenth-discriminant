# Tenth-discriminant bounds

This is an AI-assisted contribution to
[Terence Tao's tenth-discriminant challenge](https://terrytao.wordpress.com/2026/10/20/an-experimental-ai-math-challenge-using-tenth-discriminant-bounds-to-explore-arguments-ruling-out-siegel-zeroes/).
The aim is to obtain explicit bounds for a hypothetical tenth imaginary
quadratic field of class number one from arguments ruling out Siegel
zeroes, without using Heegner's solution. The repository records the
arguments, computations, and successive improvements so that they can be
examined and cited in the discussion.

For a negative fundamental discriminant `D`, write `q = |D|`. Versions 1
and 2 combine a classical theta integral with results from
[Banks, arXiv:2610.15483v1](https://arxiv.org/abs/2610.15483v1) to construct
a real zero and contradict a zero-free estimate. Version 3 counts
primitive lattice points to bound split primes directly, then uses
Banks's determinant argument. Version 4 retains that split-prime count
and uses Green's derivative determinant, with a sharper nonsingularity
lemma and tighter size estimates. Version 5 averages the derivative
determinant inequality over its size parameter and compares the resulting
prime sum with the Euler product of primitive quadratic norms, accounting
for composite norms. The determinant arguments are proved in the papers.

Each approach gives an explicit analytic cutoff. Exact integer sieves and
reduced-form enumeration handle the remaining finite range, leaving the
nine absolute fundamental discriminants
`3, 4, 7, 8, 11, 19, 43, 67, 163`. Each paper states its external inputs.
Codex prepared the derivations, write-ups, and verification programs;
the review record identifies the checks completed for each version.

**Current research draft: v0.5.0, with analytic cutoff `q < 2,000` — half
the v4 cutoff.**

**[Read the v5 proof](versions/v5/output/pdf/proof.pdf)** ·
[Source and reproduction](versions/v5/README.md) ·
[v5 release and downloads](https://github.com/twinheterodox/tenth-discriminant/releases/tag/v0.5.0)

**Independent mathematical review of v5 is pending.** V4 has passed
independent mathematical verification, and both v3 papers have passed
independent mathematical cross-checks. V5 cites v4 for `q >= 4,000`;
the new interval is treated in full, relative to the stated classical inputs.

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
| **v5 · v0.5.0** | **`q < 2,000`** | [Mellin-averaged proof and finite classification](versions/v5/output/pdf/proof.pdf) · [Source and reproduction](versions/v5/README.md) · [Release](https://github.com/twinheterodox/tenth-discriminant/releases/tag/v0.5.0) | Independent mathematical review pending; 37 exact arithmetic checks, 62,880 retained determinant cases, 10,000 primitive-norm coefficient comparisons, and an exhaustive check of 249 candidates pass |
| **v4 · v0.4.0** | **`q < 4,000`** | [Self-contained proof and finite classification](versions/v4/output/pdf/proof.pdf) · [Source and reproduction](versions/v4/README.md) · [Release](https://github.com/twinheterodox/tenth-discriminant/releases/tag/v0.4.0) | Independent mathematical verification passed; 39 exact arithmetic checks, 62,880 finite sanity cases, and an exhaustive check of 499 candidates pass |
| **v3 expanded · v0.3.1** | `q < 10^6` | [Expanded proof and finite classification](versions/v3.1/output/pdf/proof.pdf) · [Source and reproduction](versions/v3.1/README.md) · [Release](https://github.com/twinheterodox/tenth-discriminant/releases/tag/v0.3.1) | Independent mathematical cross-check passed; arithmetic and complete finite checks pass |
| **v3 original · v0.3.0** | `q < 10^6` | [Original v3 proof](versions/v3/output/pdf/proof.pdf) · [Source and reproduction](versions/v3/README.md) · [Release](https://github.com/twinheterodox/tenth-discriminant/releases/tag/v0.3.0) | Independent mathematical cross-check passed; 26 arithmetic checks and 22 finite sanity cases pass |
| **v2 · v0.2.0** | `q < 5 × 10^7` | [Complete cumulative proof](versions/v2/output/pdf/proof.pdf) · [Source and reproduction](versions/v2/README.md) · [Release](https://github.com/twinheterodox/tenth-discriminant/releases/tag/v0.2.0) | Mathematical cross-check with a different frontier model passed; 23 exact arithmetic checks pass |
| **v1 · v0.1.0** | `q < 10^10` | [Original proof](versions/v1/output/pdf/proof.pdf) · [Unchanged original snapshot](versions/v1/README.md) · [Release](https://github.com/twinheterodox/tenth-discriminant/releases/tag/v0.1.0) | Different-frontier-model cross-check reported by the repository owner; see the review record |

[Mathematical changelog](CHANGELOG.md) · [Review record by version](REVIEW.md)

The improvements change the analytic cutoff. The finite classification
remains `3, 4, 7, 8, 11, 19, 43, 67, 163`. Version 5 includes a short
exhaustive verifier for the remaining 249 candidates below 2,000.
Version 1 takes Banks's Theorem 1.1 as an external input.
Version 2 uses Lemma 4.2, Lemma 5.1, and Corollary 6.3. Version 3 uses
Lemma 4.2, Lemma 5.1, and Lemma 6.2 directly, together with explicit prime
estimates from Rosser–Schoenfeld. Each use includes the preceding
construction and hypotheses stated in the corresponding paper. These
external results are not independently proved in those versions.

Version 4 includes the derivative determinant, its resultant proof of
nonsingularity, and the full finite classification. It uses no Banks
determinant theorem as an external input. The stated Rosser–Schoenfeld
prime estimates, classical quadratic ideal theory, and reduction of
binary quadratic forms remain external inputs. No earlier paper is
needed to read v4.

Version 5 cites the independently verified v4 result only for
`q >= 4,000`. It includes the determinant and resultant proofs needed for
the new interval, the averaging argument, the primitive-norm Euler
product, and explicit error bounds for the numerical formulas. Its 37
exact arithmetic checks certify a gap greater than `0.017` throughout
`2,000 <= q <= 4,000`. The stated classical quadratic and analytic
identities and Rosser–Schoenfeld estimates remain external inputs.

The independent mathematical checks of both v3.0 and v3.1, and the
separate independent verification of v4, were confirmed on
20 October 2026 after publication. The [current review record](REVIEW.md) records subsequent
checks; fixed release files retain their status at publication.
All releases are research drafts.

## Fixed versions for citation

- [v0.1.0: original published commit](https://github.com/twinheterodox/tenth-discriminant/tree/v0.1.0)
- [v0.2.0: cumulative refined paper and files](https://github.com/twinheterodox/tenth-discriminant/tree/v0.2.0/versions/v2)
- [v0.3.0: direct split-prime proof and files](https://github.com/twinheterodox/tenth-discriminant/tree/v0.3.0/versions/v3)
- [v0.3.1: expanded v3 proof and complete finite verification](https://github.com/twinheterodox/tenth-discriminant/tree/v0.3.1/versions/v3.1)
- [v0.4.0: derivative determinant proof and verification](https://github.com/twinheterodox/tenth-discriminant/tree/v0.4.0/versions/v4)
- [v0.5.0: Mellin-averaged determinant proof and verification](https://github.com/twinheterodox/tenth-discriminant/tree/v0.5.0/versions/v5)

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
> documented in [v5](versions/v5/README.md).

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
