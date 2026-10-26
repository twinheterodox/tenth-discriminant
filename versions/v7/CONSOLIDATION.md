# What v7 consolidates

V0.7.0 keeps the analytic cutoff `q < 570` and gives a single paper whose
proof does not depend on another numbered version. It is a mathematical
reorganization with a new large-discriminant application, not an editorial
relabeling of v6.1 or a concatenation of v4, v5, and v6.1.

## Proof map

| Part of v7 | Role and origin |
|---|---|
| Sections 1–2 | Result, proof roadmap, arithmetic obstruction, lattice geometry, and explicit ordinary-prime inputs |
| Section 3 | One derivative matrix and one finite-field nonvanishing proof, as in v6 |
| Sections 4–5 | Compatible divisibility and size estimates, stated under general local hypotheses |
| Section 6 | A common comparison proposition for the smoothed noninert-prime sum |
| Section 7 | New uniform exclusion of all `q >= 2,000`; one factorial refinement and a direct primitive-norm upper bound |
| Sections 8–10.1 | The retained five-band argument on `[570,2,000]`, with its full mathematical justification |
| Section 10.2 | Complete finite sieve and reduced-form converse below 570 |
| Section 10.3 and Appendix A | Reproduction commands and explicit numerical remainder bounds |

The direct primitive norm count in Section 7 is the elementary estimate
used earlier in v4, now proved in place. The v4 resultant interpolation
argument and Gram determinant are unnecessary. V5's separate all-scale
Mellin argument and Euler–Maclaurin norm estimate are also unnecessary.
Its final implication is replaced, not cited as a premise.

## Generalizing the determinant estimates

These are the points where simply removing v6.1's range restriction would
not have been justified. V7 makes their hypotheses explicit:

1. **Geometry:** require `e >= rho/sqrt(C R v/pi)` for the actual `q,R`.
   On a bounded band the previous worst-endpoint choice at `M` implies
   this. In the tail, `R >= q^2` implies the fixed bound `e = 0.0033`
   uniformly for unbounded `q`. The fixed value `M = 4,000,000` alone
   would not imply that geometric bound for arbitrarily large `q`.
2. **Known noninert primes:** define `K_2` as any certified lower bound
   for their quadratic prime sum. The tail uses zero; the bounded bands
   use the same norm-prime list as before.
3. **Extra inert-prime gains:** use primes `p < P_* <= q/4`. The tail
   uses the fixed set `p < 500`; the bands use `P_* = Q_0/4`.
4. **Factorials:** prove the pointwise gain at scales `zR` and `hR` first.
   Taking lower scale endpoints recovers the previous band-uniform gain.
   In the tail, an already proved zero-feedback bound supplies one further
   refinement. There is no limiting or fixed-point assertion.
5. **Auxiliary primes:** prove their existence in the scale intervals
   needed by each application. In the tail these are
   `q^2 <= U <= (3/2)q^3`, with an inert prime in `(U,(3/2)U]`.
6. **Upper comparison:** both applications bound the same smoothed sum.
   The tail uses `f(s) <= 1 - (4/5)s` and a direct primitive-norm count;
   the bands use the retained positive average and Poisson norm estimate.

## What is preserved exactly

The seven existing Python certificate/support/table-builder files,
`parameters.json`, and `numerical_table.tex` are copied byte-for-byte
from v6.1. A complete run in this version reproduces the five band JSON
files and `certificate_results.json` byte-for-byte. The bands remain
`[570,580]`, `[580,600]`, `[600,700]`, `[700,1050]`, and `[1050,2000]`;
there are still 184 auxiliary-prime rows and eight finite refinements.

The source references and mathematical explanations are integrated into
the new argument; preserving the numerical certificate does not imply
that the revised general presentation has been independently reviewed.
The new tail has its own checker and output. [REVIEW.md](REVIEW.md)
separates the earlier AI-review evidence from v7's current status.

## Attribution and version history

The paper credits OpenAI's originating proof, Green's derivative variant,
van Dijk's auxiliary-prime rank argument, and the discussion contributions
beside the relevant mathematics. The original manuscript's date, 1 October
2026, is distinguished from its public release on 6 October.

All earlier papers and releases remain citation snapshots. The root README
now describes numbered versions as recording improvements to bounds or
to their proofs; a lower numerical cutoff is not required for a new
numbered version. The elementary and historical companions retain their
separate series.
