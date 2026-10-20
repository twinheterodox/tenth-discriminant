# V5 audit finding and correction

Completion of the v5 audit was confirmed on 20 October 2026. The
reported review was a **manual mathematical audit with exact computational
checks**, not formal verification. The reviewed release was
[original v0.5.0 snapshot](https://github.com/twinheterodox/tenth-discriminant/tree/7a883b764213cc52c76c9849925b823861eefc38/versions/v5),
commit
[7a883b7](https://github.com/twinheterodox/tenth-discriminant/commit/7a883b764213cc52c76c9849925b823861eefc38).
No reviewer identity or longer report was supplied.

## Reported finding

The following is the supplied comment, with its displayed fraction
transcribed into LaTeX:

> There is one minor wording correction in §6.2: $\log R/\lfloor R/110\rfloor$
> is not itself decreasing between floor jumps. The justification should
> explicitly use
>
> $\displaystyle \frac{\log R}{S}\le 110.001\,\frac{\log R}{R},$
>
> whose right side decreases. The certificate already uses this correct
> bound, so the conclusion is unaffected.
>
> This is a manual mathematical audit with exact computational checks,
> not formal verification.

## Correction within v0.5.0

The corrected paper writes the complete chain

$$
\frac{I_R}{2S}<\frac{\log R}{S}
\le 110.001\,\frac{\log R}{R}
\le 110.001\,\frac{\log M}{M}<0.00004,
\qquad R\ge M=50{,}000{,}000.
$$

Here $S=\lfloor R/110\rfloor$ and $R/S\le110.001$. The function
$(\log R)/R$ has derivative $(1-\log R)/R^2<0$ for $R\ge M>e$.
Thus the desired bound holds uniformly even though $(\log R)/S$
increases between the jumps of $S$.

The existing certificate already checks both `R/S <= 110.001` and
`110.001 log(M)/M < 0.00004`. Those exact checks were confirmed when
applying the patch. All certificate calculations and numerical results
are unchanged; the only program-output change is the final sentence,
which now points to the review record.

The generating assistant applied this correction and checked its scope
against the original files. This records the completed audit of v5 and
the implementation of its finding. The bound remains `q < 2,000`.
The minor wording correction retains version v0.5.0. The release PDF
and bundle were updated on 20 October 2026; the original publication tag
and commit above preserve the original paper, programs, outputs, and
bundle in Git history.
