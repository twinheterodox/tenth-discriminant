# Tenth-discriminant bounds

This is an AI-assisted contribution to
[Terence Tao's tenth-discriminant challenge](https://terrytao.wordpress.com/2026/10/20/an-experimental-ai-math-challenge-using-tenth-discriminant-bounds-to-explore-arguments-ruling-out-siegel-zeroes/).
The numbered series obtains explicit bounds for a hypothetical tenth
imaginary quadratic field of class number one using methods developed
in connection with Siegel zeroes, without using Heegner's solution. Companion papers explore
simpler proofs and the historical availability of methods; the historical
variant permits the modular approach later used by Heegner. The repository
records arguments, computations, and revisions for examination and citation.

**[Compare all papers and versions](#versions-and-improvements)**

**External Lean formalization:** Peter W. Murphy has published a
[Lean adaptation of the elementary companion](https://github.com/DrMurphyIsIn/tenth-discriminant/tree/f0995bf604056a98f0af0d182ed152c6bd996419/determinant),
with [reported Lean and nanoda kernel checks](https://github.com/DrMurphyIsIn/tenth-discriminant/blob/f0995bf604056a98f0af0d182ed152c6bd996419/determinant/formalization/VERIFICATION.md).
It proves the complete class-number-one classification using the cutoff
`q < 32,768`. Its scope and adaptations are recorded
[below](#companion-papers); it does not formalize the numbered series or
the historical reconstruction.

The work has three complementary aims, with separate publication series:

- **Sharper bounds:** the numbered versions, v1, v2, and so on, record
  improvements to analytic cutoffs and to the proofs of those bounds.
- **Simpler proofs:** [companion papers](#companion-papers) pursue objectives
  such as reducing the machinery or giving a self-contained exposition.
  Each companion has its own version history and release tags.
- **Historical reconstruction:** the [historical companion](#historical-companion)
  addresses how early the necessary results and concepts were available.
  It gives a complete proof and separately assesses the proposed date.

A companion can have a larger cutoff while offering a shorter or more
elementary proof. It is a separate contribution alongside the numbered
series. Review status is recorded for each paper and revision separately.

**Updated: [historical-v0.1.0](https://github.com/twinheterodox/tenth-discriminant/releases/tag/historical-v0.1.0)**
now develops the **Weber route with a proposed historical cutoff of 1891**,
`q < 196`, and a complete finite classification. It replaces the earlier
1830 determinant reconstruction under the same release name.
[Read the fourteen-page paper](companions/historical/output/pdf/historical-1891.pdf) ·
[Historical scope and reproduction](companions/historical/README.md).

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
proved in the papers. Version 7 brings the optimized proof into one
self-contained paper, using the same determinant for the bounded and
infinite ranges and retaining the cutoff `q < 570`.

Each approach gives an explicit analytic cutoff. Exact integer sieves and
reduced-form enumeration handle the remaining finite range, leaving the
nine absolute fundamental discriminants
`3, 4, 7, 8, 11, 19, 43, 67, 163`. Each paper states its external inputs.
Codex prepared the derivations, write-ups, and verification programs;
the review record identifies the checks completed for each version.

**Latest numbered paper: v0.7.0, a unified proof of `q < 570`.**

**[Read the self-contained v7 proof](versions/v7/output/pdf/proof.pdf)** ·
[Source and reproduction](versions/v7/README.md) ·
[v0.7.0 release and downloads](https://github.com/twinheterodox/tenth-discriminant/releases/tag/v0.7.0)

V7 keeps the strongest cutoff and replaces the inherited v4/v5 arguments
with a uniform application of the same determinant used near 570. One
common comparison proposition handles both ranges: a direct norm count
and one factorial refinement exclude every `q >= 2,000`; the retained
five-band certificate excludes `[570,2,000]`. The paper includes the
complete finite classification. No earlier version is a proof dependency.
See the [consolidation record](versions/v7/CONSOLIDATION.md).

**V7 has passed a cross-check by another AI model**, as reported by the
repository owner on 26 October 2026. Its 34 new exact arithmetic checks
pass, and the retained 429-check interval certificate reproduces byte-for-byte. The 101,524
finite structural cases and the finite classification also pass. These
computations are distinct from independent mathematical review or formal
verification; the [v7 review record](versions/v7/REVIEW.md) states their scope.

V6 previously received a reported second-model cross-check and a separate
AI-assisted audit coordinated by Henric Larsson. His
[clarification](https://terrytao.wordpress.com/2026/10/20/an-experimental-ai-math-challenge-using-tenth-discriminant-bounds-to-explore-arguments-ruling-out-siegel-zeroes/comment-page-1/#comment-698595)
reports no proof or certificate requiring correction. Those earlier reports
are separate from the subsequent v7 model cross-check. All earlier papers
and release assets remain available, including
[v0.6.1](https://github.com/twinheterodox/tenth-discriminant/releases/tag/v0.6.1).

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

**The elementary companion passed a cross-check by a second AI model,**
confirmed on 21 October 2026. Its exact constant checks and exhaustive
sieve of 4,095 candidate integers also pass; an isolated run of the release
bundle reproduces the recorded outputs.

**Peter W. Murphy subsequently formalized an adaptation of this argument
in Lean.** His [determinant proof and paper](https://github.com/DrMurphyIsIn/tenth-discriminant/tree/f0995bf604056a98f0af0d182ed152c6bd996419/determinant)
credit this companion, and his
[verification record](https://github.com/DrMurphyIsIn/tenth-discriminant/blob/f0995bf604056a98f0af0d182ed152c6bd996419/determinant/formalization/VERIFICATION.md)
reports acceptance by Lean and nanoda. Some estimates and the proof that
the nine surviving fields have class number one differ from this paper.
The [companion review record](companions/elementary/REVIEW.md) distinguishes
that external formalization from the earlier AI-model cross-check and our
computational checks. This documentation update does not rerun the Lean
build or assert Mathlib acceptance.

The first release is **`elementary-v0.1.0`**, with the paper, source,
and verification files under `companions/elementary/`. Subsequent revisions
will retain the `elementary-` prefix and their own citation snapshots;
the [companion changelog](companions/elementary/CHANGELOG.md) records that history.
The numbered series also records improvements to the optimized proof:
v7 is its self-contained consolidation, with the same analytic cutoff as
v6. Published release links and earlier snapshots in each series remain
available for citation.

### Historical companion

The **historical reconstruction** addresses
[Tao's variant, communicated by Ben Green](https://terrytao.wordpress.com/2026/10/20/an-experimental-ai-math-challenge-using-tenth-discriminant-bounds-to-explore-arguments-ruling-out-siegel-zeroes/#comment-698559):
how early one could prove there is no tenth discriminant using results
and concepts already in the literature. It develops
[Pratt's proposed cutoff of **1891**](https://terrytao.wordpress.com/2026/10/20/an-experimental-ai-math-challenge-using-tenth-discriminant-bounds-to-explore-arguments-ruling-out-siegel-zeroes/comment-page-1/#comment-698625)
using Weber's modular theory, gives **`q < 196`**, and completes the
finite classification.

**[Read the fourteen-page Weber reconstruction](companions/historical/output/pdf/historical-1891.pdf)** ·
[Source, historical scope, and reproduction](companions/historical/README.md) ·
[historical-v0.1.0 release and downloads](https://github.com/twinheterodox/tenth-discriminant/releases/tag/historical-v0.1.0)

The paper states its imported classical modular toolkit explicitly. It
supplies the special root-control repair of Weber's argument, Heegner's
cubic comparison, Euler's descent, and the finite finish. Weber's section
76 already describes the product construction used in the repair.
Historical and modern references are separated and placed in context.
The proposed date permits new applications of published methods; it does
not claim that the proof was known in 1891 or that 1891 is the earliest
possible year.

**Replacement dated 22 October 2026, retaining `historical-v0.1.0`.**
The earlier 1830 historical claim is superseded: the determinant method
does not meet the revised criterion merely because it can be developed
from older foundations. The current paper, source, and release downloads
contain the Weber reconstruction. The original tag and Git history retain
the earlier paper, and the [companion changelog](companions/historical/CHANGELOG.md)
records the replacement.

**No independent audit verdict is recorded for the Weber reconstruction.**
The exact algebra and finite checks pass and reproduce from the release
bundle. Those checks do not establish the analytic modular toolkit or
historical admissibility, and they are not formal verification. The
[review record](companions/historical/REVIEW.md) gives their scope.

## Versions and improvements

In the numbered series, improvements to bounds or their proofs are added
as new versions, each with its own proof and verification files. Published snapshots and
release links are preserved, so earlier comments can continue to cite the
exact argument they discussed. This README is the entry point to all
series and their histories; the changelog records mathematical changes
and editorial revisions in the numbered series. The original v1 README is retained
below as a historical snapshot.

The table includes all three series: the numbered bounds, the elementary
companion focused on proof simplicity, and the historical reconstruction
focused on the date of the available foundations. Each companion retains
its own version history and review status.

| Series and version | Analytic cutoff | Paper and files | Review status |
|---|---|---|---|
| **v7 · v0.7.0** | **`q < 570`** | [Unified self-contained proof](versions/v7/output/pdf/proof.pdf) · [Source and reproduction](versions/v7/README.md) · [Release](https://github.com/twinheterodox/tenth-discriminant/releases/tag/v0.7.0) | Second-AI-model cross-check reported passed; 34 new exact checks and the retained 429-check certificate pass; not formal verification ([review record](versions/v7/REVIEW.md)) |
| **Historical companion · historical-v0.1.0 (replaced 22 October 2026)** | **`q < 196`** | [Weber reconstruction: proposed historical cutoff 1891](companions/historical/output/pdf/historical-1891.pdf) · [Source and reproduction](companions/historical/README.md) · [Release](https://github.com/twinheterodox/tenth-discriminant/releases/tag/historical-v0.1.0) | No independent audit verdict recorded; mathematical proof and historical eligibility require separate review; exact algebra and finite checks pass ([review record](companions/historical/REVIEW.md)) |
| **Elementary companion · elementary-v0.1.0** | **`q < 32,768 = 2^15`** | [Elementary proof](companions/elementary/output/pdf/elementary-companion.pdf) · [Source and reproduction](companions/elementary/README.md) · [Release](https://github.com/twinheterodox/tenth-discriminant/releases/tag/elementary-v0.1.0) · [Murphy's Lean adaptation](https://github.com/DrMurphyIsIn/tenth-discriminant/tree/f0995bf604056a98f0af0d182ed152c6bd996419/determinant) | Second-AI-model cross-check passed; exact finite checks pass; Murphy reports Lean/nanoda acceptance of his adaptation ([scope and evidence](companions/elementary/REVIEW.md)) |
| **v6 revised · v0.6.1** | **`q < 570`** | [Revised proof](versions/v6.1/output/pdf/proof.pdf) · [Source and reproduction](versions/v6.1/README.md) · [Release](https://github.com/twinheterodox/tenth-discriminant/releases/tag/v0.6.1) | Same mathematics and certificates as AI-reviewed v0.6.0; no separate audit of the revised exposition or Lean formalization recorded |
| **v6 original · v0.6.0** | `q < 570` | [Original proof](versions/v6/output/pdf/proof.pdf) · [Source and reproduction](versions/v6/README.md) · [Release](https://github.com/twinheterodox/tenth-discriminant/releases/tag/v0.6.0) | Second-model cross-check and separate AI-assisted audit reported passed; exact checks pass; not formal verification ([review record](REVIEW.md)) |
| **v5 · v0.5.0** | **`q < 2,000`** | [Corrected proof](versions/v5/output/pdf/proof.pdf) · [Source and reproduction](versions/v5/README.md) · [Release](https://github.com/twinheterodox/tenth-discriminant/releases/tag/v0.5.0) | AI-model cross-check with exact computational checks passed; §6.2 wording corrected within v0.5.0; calculations unchanged; not formal verification |
| **v4 · v0.4.0** | **`q < 4,000`** | [Self-contained proof and finite classification](versions/v4/output/pdf/proof.pdf) · [Source and reproduction](versions/v4/README.md) · [Release](https://github.com/twinheterodox/tenth-discriminant/releases/tag/v0.4.0) | Second-AI-model cross-check passed; 39 exact arithmetic checks, 62,880 finite sanity cases, and an exhaustive check of 499 candidates pass |
| **v3 expanded · v0.3.1** | `q < 10^6` | [Expanded proof and finite classification](versions/v3.1/output/pdf/proof.pdf) · [Source and reproduction](versions/v3.1/README.md) · [Release](https://github.com/twinheterodox/tenth-discriminant/releases/tag/v0.3.1) | Second-AI-model cross-check passed; arithmetic and complete finite checks pass |
| **v3 original · v0.3.0** | `q < 10^6` | [Original v3 proof](versions/v3/output/pdf/proof.pdf) · [Source and reproduction](versions/v3/README.md) · [Release](https://github.com/twinheterodox/tenth-discriminant/releases/tag/v0.3.0) | Second-AI-model cross-check passed; 26 arithmetic checks and 22 finite sanity cases pass |
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

Version 5 cites the AI-cross-checked v4 result only for
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

Version 7 replaces both inherited range proofs with a uniform application
of the v6 determinant estimates above 2,000. It proves the auxiliary-prime
supply, a pointwise factorial refinement, a direct smoothed norm bound,
and the monotonic endpoint comparison. The five bounded-band certificates
are unchanged and reproduce exactly. The paper develops the complete
argument and finite finish relative to its stated classical inputs; no
v4 or v5 implication is imported. The cutoff remains 570.

The checks reported for v1-v5 and the elementary companion were
cross-checks by another AI model, as clarified on 26 October 2026; no
human peer review is implied. V5's minor wording correction remains
recorded in v0.5.0. V6 has its own subsequent AI-review reports, and
Murphy's Lean adaptation applies to the elementary route only. The
[current review record](REVIEW.md) distinguishes AI-model review,
computational checks, and formal verification. Original publication
snapshots retain their status at publication.
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
- [v0.7.0: unified proof and complete classification, q < 570](https://github.com/twinheterodox/tenth-discriminant/tree/v0.7.0/versions/v7)
- [elementary-v0.1.0: original elementary companion publication](https://github.com/twinheterodox/tenth-discriminant/tree/elementary-v0.1.0/companions/elementary)
- [historical-v0.1.0: original 1830 reconstruction, superseded by the Weber replacement](https://github.com/twinheterodox/tenth-discriminant/tree/historical-v0.1.0/companions/historical)

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

The historical companion's [current paper and source](companions/historical/README.md)
and [release downloads](https://github.com/twinheterodox/tenth-discriminant/releases/tag/historical-v0.1.0)
contain the Weber reconstruction, substituted on 22 October 2026 under
`historical-v0.1.0`. The original tag and GitHub's automatic source archives
retain the superseded 1830 reconstruction. Use the attached replacement
bundle or the replacement commit linked in the release notes to cite the
Weber paper. The previous PDF path also serves the replacement so older
links remain usable.

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
> documented in [v7](versions/v7/README.md).

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
