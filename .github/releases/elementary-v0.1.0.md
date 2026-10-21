**q < 32,768 = 2^15**, with a simpler, self-contained determinant proof.

[Read the eight-page paper](https://github.com/twinheterodox/tenth-discriminant/releases/download/elementary-v0.1.0/elementary-v0.1.0.pdf) · [Download the proof and verification bundle](https://github.com/twinheterodox/tenth-discriminant/releases/download/elementary-v0.1.0/elementary-v0.1.0.zip) · [Source and reproduction](https://github.com/twinheterodox/tenth-discriminant/tree/main/companions/elementary)

Research note prepared with Codex

This is the first release of the elementary companion series. It pursues
proof simplicity alongside the numbered series of improving bounds, whose
strongest cutoff remains v6's `q < 570`. The companion is independent of
v1-v6.

The proof counts quadratic norm representations to bound split primes,
finds an auxiliary inert prime in `(q^4, q^5]`, and uses an ordinary
rectangular interpolation grid. A finite-field root count proves the
derivative determinant is nonzero. Frobenius divisibility and a complex
size bound then contradict each other above the cutoff. All required
ordinary-prime estimates are proved by factorial and binomial arguments;
the numerical conclusion uses one endpoint comparison.

The paper cites Silberman, Pratt, Green, and van Dijk where their ideas
enter, and acknowledges Green's report of Pescador's related unpublished
argument. The acknowledgements retain the sources' AI attributions.

The exact constant checks pass, with final margin `1009/55200`. An
exhaustive integer sieve tests 4,095 candidates using primes through 31,
and reduced-form enumeration confirms the nine surviving discriminants.
At first publication, an isolated run of the release bundle reproduced
the recorded outputs. The computation files are unchanged.

**Independent mathematical review is pending.** The checks were performed
in the same Codex session that developed the note; they are not an
independent audit or formal verification. See the
[review record](https://github.com/twinheterodox/tenth-discriminant/blob/main/companions/elementary/REVIEW.md).

The PDF, source, verification programs, results, and checksums are included.
This is a research prerelease. Future companion revisions will retain
the `elementary-` prefix; the numbered version history remains intact.

The downloads include the authorship correction of 21 October 2026, under
the same version number: the byline now reads only "Research note prepared
with Codex." The mathematical argument, programs, and results are unchanged.
The [original publication tag](https://github.com/twinheterodox/tenth-discriminant/tree/elementary-v0.1.0/companions/elementary)
and Git history preserve the first files.
