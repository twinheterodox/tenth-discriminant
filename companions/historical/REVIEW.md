# Historical companion: review and verification

## historical-v0.1.0 - 21 October 2026

No independent audit verdict is asserted for this historical
reconstruction. The mathematical argument and the proposed historical
cutoff of 1830 require separate review. The independent verification of
the elementary companion does not automatically cover the adaptations
or historical interpretation in this paper.

The development-session checks establish the following computational
facts:

- All exact rational constant checks pass, including the final positive
  margin `1009/55200`.
- The checker reads the tables directly from `proof.tex` and validates
  all 30 CRT rows, 104 large-range witnesses, and 15 small-range witnesses.
- A separate Euler-criterion sieve of all 4,095 candidates gives the same
  survivors, and reduced-form enumeration verifies all nine final lists.
- An isolated extraction of the release bundle reproduces both programs'
  recorded outputs using the Python standard library.

The fourteen-page PDF was compiled, rendered, and visually inspected.
Its printed modular certificate matches the source. The citation revision
preserved the mathematical displays and certificate data; publication
retains that revised manuscript and PDF unchanged.

These computations support the paper's proof. They do not verify its
general mathematical steps or establish the historical eligibility of
its concepts. They are not formal verification. The code and exposition
were prepared with Codex; no separate reviewer or review report is
claimed for this release.

The paper's Section 1.1 and [historical source documentation](historical_sources.txt)
state the scope of the date claim. The [recorded checks](checks.txt) give
the computational output.
