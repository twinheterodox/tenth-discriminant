TENTH-DISCRIMINANT BOUNDS — VERSION INDEX
20 October 2026

Current research draft: v0.3.0, analytic cutoff q < 1,000,000.

v3: versions/v3/README.md
    Direct split-prime proof: versions/v3/output/pdf/proof.pdf
    26 exact arithmetic checks and 22 finite sanity cases pass.
    Independent mathematical cross-check pending.
    https://github.com/twinheterodox/tenth-discriminant/releases/tag/v0.3.0

v2: versions/v2/README.md
    Complete cumulative paper: versions/v2/output/pdf/proof.pdf
    Mathematical cross-check with a different frontier model passed.
    23 exact arithmetic checks pass. See REVIEW.md for the current record.
    https://github.com/twinheterodox/tenth-discriminant/releases/tag/v0.2.0

v1: versions/v1/README.md
    Original cutoff q < 10^10. Exact snapshot of commit b305496.
    Cross-check with a different frontier model reported by the owner.
    https://github.com/twinheterodox/tenth-discriminant/releases/tag/v0.1.0

See CHANGELOG.md for mathematical changes and REVIEW.md for review scope.
The v2 cross-check passed after publication, as confirmed on 20 October
2026; it applies to v2. The fixed release files retain their status at
publication. The original finite-verification files are included in v3
and cover its remaining range without changes to the nine survivors.
The original root proof, programs, outputs, and bundle remain unchanged.

ORIGINAL README — V1, AS PUBLISHED
The following text is a historical snapshot; consult REVIEW.md for later
review information and versions/v3/README.md for the current draft.

EXPLICIT TENTH-DISCRIMINANT BOUND
20 October 2026

Status: AI-assisted draft for mathematical review. The analytic argument
has not received an independent audit. See README.md for the repository
index, links, reproduction instructions, and full AI disclosure.

Result
------
Using Banks, arXiv:2610.15483v1, Theorem 1.1 for q >= 10^10:

    h(Q(sqrt(D))) = 1  ==>  |D| < 10^10,

where D < 0 is a fundamental discriminant. An exhaustive exact-integer
sieve then leaves only

    |D| = 3, 4, 7, 8, 11, 19, 43, 67, 163.

The squarefree radicands are 1, 2, 3, 7, 11, 19, 43, 67, 163.

The new work in this directory is an explicit theta-integral bridge
from Banks's stated zero-free theorem to the class-number-one problem,
plus a reproducible finite exclusion. It is not an independent proof
of Banks's theorem or a claim of novelty for the classical method.

Read
----
output/pdf/proof.pdf     Five-page proof and dependency statement.
proof.tex                Editable LaTeX source.
verify_sieve.cpp         CRT wheel; direct checks using quadratic residues.
verify_independent.py    Direct wheel scan; Euler criterion and periodic bitsets.
sieve_cpp_output.txt     Output of the C++ calculation.
sieve_python_output.txt  Output of the Python calculation and rational checks.
sources/manifest.json   Primary-source URLs and hashes of local snapshots.

Reproduce
---------
Requires a C++17 compiler and Python 3; no external number-theory package.

    g++ -O2 -std=c++17 -Wall -Wextra -pedantic verify_sieve.cpp -o verify_sieve
    ./verify_sieve
    python3 verify_independent.py

Rebuild the PDF with LaTeX:

    mkdir -p output/pdf
    pdflatex -interaction=nonstopmode -halt-on-error -output-directory=output/pdf proof.tex
    pdflatex -interaction=nonstopmode -halt-on-error -output-directory=output/pdf proof.tex

Verification performed
----------------------
Both algorithms check 7,051,769 candidates remaining after the initial
CRT filters and eliminate every q in [437, 10^10). Only primes <= 109
are used. For 11 <= q < 437, both find 11, 19, 43, 67, 163.

The Python script also enumerates reduced primitive forms for the nine
survivors and verifies the exact rational inequalities used in the
analytic argument. The C++ build completed without compiler warnings.
The PDF was rendered and all five pages visually inspected.

Scope
-----
The external analytic input is:

    (1-beta) log q >= 3/1000  for q >= 10^10.

The theta argument supplies:

    1-beta < 10/sqrt(q)

under the contradictory class-number-one assumption. At q >= 10^10
this yields (1-beta) log q < 3/1250 < 3/1000.

Banks's extension to small conductors by a separate computation is not
used. Heegner's solution, Heegner points, and a class-number database
are not used. No Lean formalization or independent human/model review
has been completed. The two algorithms were written by the same AI
assistant, so algorithmic agreement is not an independent proof audit.

The full third-party source snapshots are local research material and
are not included in the distributable archive. Their URLs are in the
manifest. Making the package available does not itself submit a comment
to the blog.
