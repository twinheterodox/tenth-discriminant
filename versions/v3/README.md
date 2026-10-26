# Version 3: analytic cutoff q < 1,000,000

**v0.3.0 · 20 October 2026 · AI-assisted draft for mathematical review**

[Read the five-page proof of the new cutoff](output/pdf/proof.pdf) ·
[LaTeX source](proof.tex) ·
[Download this version's proof and verification bundle](https://github.com/twinheterodox/tenth-discriminant/releases/download/v0.3.0/tenth-discriminant-v0.3.0.zip)

This version improves the v2 analytic cutoff `q < 50,000,000` by a factor
of 50. It supplies a complete proof of the new cutoff using a direct
split-prime estimate. The earlier finite classification is reused, with
its original programs and outputs included here. The
[v1](https://github.com/twinheterodox/tenth-discriminant/releases/tag/v0.1.0)
and [v2](https://github.com/twinheterodox/tenth-discriminant/releases/tag/v0.2.0)
releases remain unchanged.

## Result and dependencies

Let `D < 0` be a fundamental discriminant and `q = |D|`. Assuming the
intermediate results of Banks specified below, the paper derives

```text
h(Q(sqrt(D))) = 1  implies  q < 1,000,000.
```

The external inputs are Banks's determinant construction and Lemmas 4.2,
5.1, and 6.2, including the preceding interpolation results, in
[arXiv:2610.15483v1](https://arxiv.org/html/2610.15483v1). The proof also
uses the explicit prime estimates in Theorems 6 and 9 of
[Rosser–Schoenfeld (1962)](https://doi.org/10.1215/ijm/1255631807).
These results are not independently proved here.

The original exact finite computation already covers `q < 10^10`, so it
covers the entire remaining range. The nine surviving absolute fundamental
discriminants are unchanged:

```text
3, 4, 7, 8, 11, 19, 43, 67, 163.
```

## What changed mathematically

Class number one makes every split-prime ideal principal. Each split prime
therefore supplies two primitive lattice points with positive imaginary
part and with that prime as norm. Counting these points, and removing
coordinate pairs that share a factor among `2, 3, 5, 7`, bounds the weighted
sum of split primes directly. An explicit estimate for the total prime sum
then supplies the inert-prime mass needed in Banks's determinant argument.

With `H = 10^9`, `N = q^13`, and `M = N^(4/3)`, the determinant estimates
would require a quantity greater than `4.238` to be less than `4.216`
whenever `q >= 1,000,000`. The exact rational contradiction has a gap
greater than `0.022`.

This replaces the theta-integral zero construction and the zero-dependent
prime-bias estimate used in v2. It uses Banks's Lemma 6.2 directly, without
his Theorem 1.1, Lemma 2.1, or Corollary 6.3. No Heegner method,
class-number database, or small-conductor zero computation is used.

## Verification status

**The v3 argument passed a cross-check by a second AI model,** confirmed
on 20 October 2026. This is not human peer review or formal verification.
All 26 exact arithmetic checks and 22 finite sanity cases also pass.

The finite sanity cases compare direct lattice enumeration with the
counting formulas and check prime-norm multiplicities in known fields.
They do not prove the general counting lemmas or verify Banks's
interpolation argument. All arithmetic decisions in the new checker use
integers or exact fractions. The five-page PDF was compiled, rendered,
and visually inspected.

The original finite-sieve programs and recorded outputs are copied
byte-for-byte. Their existing results cover the larger range below
`10^10`; they were not rerun for this release.

See [this version's publication-time review record](REVIEW.md) and the
[current review record](https://github.com/twinheterodox/tenth-discriminant/blob/main/REVIEW.md)
for the scope of completed checks and the terminology clarified on
26 October 2026. The published paper and bundle remain unchanged.

## Reproduce

Run from this directory. The new certificate uses Python's standard
library:

```sh
python3 verify_direct_prime.py --sanity
```

Omit `--sanity` to run only the 26 exact arithmetic checks. The recorded
full output is [checks.txt](checks.txt).

To reproduce the inherited finite computation, use a C++17 compiler and
Python 3.8 or newer:

```sh
g++ -O2 -std=c++17 -Wall -Wextra -pedantic verify_sieve.cpp -o verify_sieve
./verify_sieve
python3 verify_independent.py
```

Recorded original outputs: [C++ sieve](sieve_cpp_output.txt) ·
[Python sieve and reduced forms](sieve_python_output.txt). The justification
of this inherited finite calculation is in the
[v2 paper](https://github.com/twinheterodox/tenth-discriminant/blob/v0.2.0/versions/v2/output/pdf/proof.pdf).

To rebuild the new PDF with the LaTeX packages named in `proof.tex`:

```sh
mkdir -p output/pdf
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=output/pdf proof.tex
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=output/pdf proof.tex
```

## Provenance and AI disclosure

Codex prepared the new derivation, paper, checker, and documentation. The
two inherited finite-sieve algorithms were also written by the same
assistant. Computational agreement is not an independent analytic review.
No Lean formalization is supplied.

[Source provenance](sources.json) records primary-source URLs and hashes
of the research snapshots. Third-party snapshots are not redistributed.
[Artifact checksums](artifact-manifest.json) identify this version's
individual files; the
[repository manifest](https://github.com/twinheterodox/tenth-discriminant/blob/v0.3.0/artifact-manifest.json)
also covers the downloadable bundle. The fixed release is
[v0.3.0](https://github.com/twinheterodox/tenth-discriminant/releases/tag/v0.3.0).
