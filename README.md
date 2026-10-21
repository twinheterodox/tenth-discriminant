# Tenth-discriminant bounds

This is an AI-assisted contribution to
[Terence Tao's tenth-discriminant challenge](https://terrytao.wordpress.com/2026/10/20/an-experimental-ai-math-challenge-using-tenth-discriminant-bounds-to-explore-arguments-ruling-out-siegel-zeroes/).
The aim is to obtain explicit bounds for a hypothetical tenth imaginary
quadratic field of class number one from arguments ruling out Siegel
zeroes, without using Heegner's solution. The repository records the
arguments, computations, and revisions so that they can be
examined and cited in the discussion.

The work has two complementary aims, with separate publication series:

- **Sharper bounds:** the numbered versions, v1, v2, and so on, record
  progressively smaller analytic cutoffs and revisions of those arguments.
- **Simpler proofs:** [companion papers](#companion-papers) pursue objectives
  such as reducing the machinery or giving a self-contained exposition.
  Each companion has its own version history and release tags.

A companion can have a larger cutoff while offering a shorter or more
elementary proof. It is a separate contribution alongside the numbered
series. Review status is recorded for each paper and revision separately.

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
for composite norms. Version 6 retains a smoothed prime sum, strengthens
the Frobenius divisibility and size estimates, and uses an auxiliary inert
prime with a positive averaging kernel. The determinant arguments are
proved in the papers.

Each approach gives an explicit analytic cutoff. Exact integer sieves and
reduced-form enumeration handle the remaining finite range, leaving the
nine absolute fundamental discriminants
`3, 4, 7, 8, 11, 19, 43, 67, 163`. Each paper states its external inputs.
Codex prepared the derivations, write-ups, and verification programs;
the review record identifies the checks completed for each version.

**Strongest bound in the numbered series: v0.6.1, with analytic cutoff `q < 570`
(previously `q < 2,000`).**

**[Read the revised v6 proof](versions/v6.1/output/pdf/proof.pdf)** ·
[Source and reproduction](versions/v6.1/README.md) ·
[v0.6.1 release and downloads](https://github.com/twinheterodox/tenth-discriminant/releases/tag/v0.6.1)

**V0.6.1 revises the exposition:** a proof roadmap, explanations before
the technical estimates, citations beside the ideas used, and an appendix
for numerical remainder bounds. The mathematics and certificate files are
unchanged. The [original v0.6.0 release](https://github.com/twinheterodox/tenth-discriminant/releases/tag/v0.6.0)
remains available for citation.

**Independent mathematical review of v6 is pending.** Its 429 grouped
exact rational checks and 101,524 finite structural cases pass; an isolated
rerun reproduced the exact certificate outputs. These computations are
not an independent mathematical audit or formal verification.

The seventeen-page paper treats the new interval `570 <= q <= 2,000`
in full relative to its stated classical inputs and cites v5 above that
range. **V5 has passed a manual mathematical audit with exact computational
checks**; its [corrected proof](versions/v5/output/pdf/proof.pdf) and
[audit record](versions/v5/AUDIT.md) remain available. The v6 argument
uses no quasi-Riemann hypothesis or quadratic zero-free theorem.

## Companion papers

The **elementary determinant companion**, with cutoff **`q < 32,768 = 2^15`**,
prioritizes a simple, self-contained proof. It proves its ordinary-prime
estimates using factorials and binomial coefficients, uses a rectangular
interpolation grid, and concludes with one endpoint comparison. Its proof
is independent of v1-v6. The remaining finite range is small enough for an
elementary residue sieve.

**[Read the eight-page elementary proof](companions/elementary/output/pdf/elementary-companion.pdf)** ·
[Source and reproduction](companions/elementary/README.md) ·
[elementary-v0.1.0 release and downloads](https://github.com/twinheterodox/tenth-discriminant/releases/tag/elementary-v0.1.0)

**The elementary companion has passed independent mathematical verification,**
confirmed on 21 October 2026. Its exact constant checks and exhaustive
sieve of 4,095 candidate integers also pass; an isolated run of the release
bundle reproduces the recorded outputs. The [review record](companions/elementary/REVIEW.md)
records the independent verification separately from those computations.
No formal verification is supplied.

The first release is **`elementary-v0.1.0`**, with the paper, source,
and verification files under `companions/elementary/`. Subsequent revisions
will retain the `elementary-` prefix and their own citation snapshots;
the [companion changelog](companions/elementary/CHANGELOG.md) records that history.
The next numbered version, v7, remains available for a further improvement
in the analytic cutoff. Published release links and earlier snapshots in
both series will remain available for citation.

## Versions and improvements

In the numbered series, improved bounds are added as new versions, each
with its own proof and verification files. Published snapshots and
release links are preserved, so earlier comments can continue to cite the
exact argument they discussed. This README is the entry point to both
series and their histories; the changelog records mathematical changes
and editorial revisions in the numbered series. The original v1 README is retained
below as a historical snapshot.

| Version | Analytic cutoff | Paper and files | Mathematical review status |
|---|---|---|---|
| **v6 revised · v0.6.1** | **`q < 570`** | [Revised proof](versions/v6.1/output/pdf/proof.pdf) · [Source and reproduction](versions/v6.1/README.md) · [Release](https://github.com/twinheterodox/tenth-discriminant/releases/tag/v0.6.1) | Review status unchanged; editorial revision preserves all displayed equations, certificate code, parameters, and results |
| **v6 original · v0.6.0** | `q < 570` | [Original proof](versions/v6/output/pdf/proof.pdf) · [Source and reproduction](versions/v6/README.md) · [Release](https://github.com/twinheterodox/tenth-discriminant/releases/tag/v0.6.0) | Independent mathematical audit pending; 429 grouped exact checks, 101,524 finite structural cases, and 70 finite discriminant candidates pass |
| **v5 · v0.5.0** | **`q < 2,000`** | [Corrected proof](versions/v5/output/pdf/proof.pdf) · [Source and reproduction](versions/v5/README.md) · [Release](https://github.com/twinheterodox/tenth-discriminant/releases/tag/v0.5.0) | Manual mathematical audit with exact computational checks passed; §6.2 wording corrected within v0.5.0; calculations unchanged; not formal verification |
| **v4 · v0.4.0** | **`q < 4,000`** | [Self-contained proof and finite classification](versions/v4/output/pdf/proof.pdf) · [Source and reproduction](versions/v4/README.md) · [Release](https://github.com/twinheterodox/tenth-discriminant/releases/tag/v0.4.0) | Independent mathematical verification passed; 39 exact arithmetic checks, 62,880 finite sanity cases, and an exhaustive check of 499 candidates pass |
| **v3 expanded · v0.3.1** | `q < 10^6` | [Expanded proof and finite classification](versions/v3.1/output/pdf/proof.pdf) · [Source and reproduction](versions/v3.1/README.md) · [Release](https://github.com/twinheterodox/tenth-discriminant/releases/tag/v0.3.1) | Independent mathematical cross-check passed; arithmetic and complete finite checks pass |
| **v3 original · v0.3.0** | `q < 10^6` | [Original v3 proof](versions/v3/output/pdf/proof.pdf) · [Source and reproduction](versions/v3/README.md) · [Release](https://github.com/twinheterodox/tenth-discriminant/releases/tag/v0.3.0) | Independent mathematical cross-check passed; 26 arithmetic checks and 22 finite sanity cases pass |
| **v2 · v0.2.0** | `q < 5 × 10^7` | [Complete cumulative proof](versions/v2/output/pdf/proof.pdf) · [Source and reproduction](versions/v2/README.md) · [Release](https://github.com/twinheterodox/tenth-discriminant/releases/tag/v0.2.0) | Mathematical cross-check with a different frontier model passed; 23 exact arithmetic checks pass |
| **v1 · v0.1.0** | `q < 10^10` | [Original proof](versions/v1/output/pdf/proof.pdf) · [Unchanged original snapshot](versions/v1/README.md) · [Release](https://github.com/twinheterodox/tenth-discriminant/releases/tag/v0.1.0) | Different-frontier-model cross-check reported by the repository owner; see the review record |

[Mathematical changelog](CHANGELOG.md) · [Review record by version](REVIEW.md)

Versions that revise the exposition retain the preceding analytic cutoff.
The finite classification
remains `3, 4, 7, 8, 11, 19, 43, 67, 163`. Version 6 includes a short
exhaustive verifier for the remaining 70 candidates below 570.
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

Version 6 cites v5 for `q >= 2,000`. It consolidates the full new interval
argument, including the auxiliary-prime sieve, residual Frobenius factors,
eight acyclic factorial refinements, joint derivative/radius estimates,
and positive-kernel comparison with an explicit Poisson error. Five exact
interval certificates cover `[570,2,000]`, with a smallest certified gap
greater than `0.010389`. No intermediate unpublished draft is needed.
The stated ordinary-prime estimates and classical quadratic and analytic
identities remain external inputs. The
[research and attribution record](versions/v6.1/RESEARCH.md) describes the
contributions from the challenge discussion and the alternatives tested.
The [v0.6.1 editorial record](versions/v6.1/EDITORIAL.md) maps the revised
sections to v0.6.0 and documents what was preserved.

The independent mathematical checks of both v3.0 and v3.1, and the
separate independent verification of v4, were confirmed on
20 October 2026 after publication. The completed manual audit of v5 and
its wording correction are recorded in v0.5.0. These checks do not cover
v6, whose independent mathematical audit is pending. The
[current review record](REVIEW.md) records subsequent checks; original
publication snapshots retain their status at publication.
All releases are research drafts.

## Fixed versions for citation

- [v0.1.0: original published commit](https://github.com/twinheterodox/tenth-discriminant/tree/v0.1.0)
- [v0.2.0: cumulative refined paper and files](https://github.com/twinheterodox/tenth-discriminant/tree/v0.2.0/versions/v2)
- [v0.3.0: direct split-prime proof and files](https://github.com/twinheterodox/tenth-discriminant/tree/v0.3.0/versions/v3)
- [v0.3.1: expanded v3 proof and complete finite verification](https://github.com/twinheterodox/tenth-discriminant/tree/v0.3.1/versions/v3.1)
- [v0.4.0: derivative determinant proof and verification](https://github.com/twinheterodox/tenth-discriminant/tree/v0.4.0/versions/v4)
- [v0.5.0: original publication snapshot](https://github.com/twinheterodox/tenth-discriminant/tree/v0.5.0/versions/v5)
- [v0.6.0: smoothed Frobenius determinant proof and verification](https://github.com/twinheterodox/tenth-discriminant/tree/v0.6.0/versions/v6)
- [v0.6.1: revised v6 exposition, with the same bound and certificates](https://github.com/twinheterodox/tenth-discriminant/tree/v0.6.1/versions/v6.1)
- [elementary-v0.1.0: original elementary companion publication](https://github.com/twinheterodox/tenth-discriminant/tree/elementary-v0.1.0/companions/elementary)

The v0.6.0 directory, tag, and downloadable assets retain the original
paper. V0.6.1 is a separate release containing the revised exposition;
both versions remain available at their own fixed links.

The v0.5.0 tag retains the original publication. Its
[release downloads](https://github.com/twinheterodox/tenth-discriminant/releases/tag/v0.5.0)
and [current source](versions/v5/README.md) include the minor wording
correction dated 20 October 2026, under the same version number. The
original files remain available through the tag and Git history.

The elementary companion's [current paper and source](companions/elementary/README.md)
and [release downloads](https://github.com/twinheterodox/tenth-discriminant/releases/tag/elementary-v0.1.0)
include the authorship correction and completed-verification status dated
21 October 2026, under the same version number. Its byline is
"Research note prepared with Codex."
The original publication tag preserves the first files; the mathematics
and verification programs are unchanged.

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
> documented in [v6.1](versions/v6.1/README.md).

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
