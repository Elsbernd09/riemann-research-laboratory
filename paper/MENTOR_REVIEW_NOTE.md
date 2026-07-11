# Mentor Review Note

Dear Professor / Reviewer,

I am sharing a research draft titled:

**Matched-Scale Li Susceptibility and Centered-Primitive Transfer of Zero-Counting Discrepancy**

The paper studies a response functional associated with the Li kernel

\[
f_n(z)=1-\left(1-\frac1z\right)^n
\]

through the horizontal zero-coordinate susceptibility

\[
\chi_n^{Li}(\gamma)
=
2\Re f_n''\left(\frac12+i\gamma\right).
\]

The main theorem is an unconditional response estimate. For fixed

\[
\eta>0
\]

and compact

\[
K\Subset(0,\infty),
\]

the paper proves, uniformly for

\[
n/H\in K,
\]

that

\[
R_{\mathrm{int}}(n;H,\eta)
=
O_{K,\eta}
\left(
\frac{\log H}{H^3}
\right),
\]

where

\[
R_{\mathrm{int}}(n;H,\eta)
=
-\int_H^{(1+\eta)H}
E(t)\chi_n'(t)\,dt
\]

and

\[
E(t)=N(t)-M(t).
\]

No assumption of the Riemann Hypothesis is used.

Under RH, the classical sharper bound for \(S_1(t)\) gives the refinement

\[
R_{\mathrm{int}}(n;H,\eta)
=
O_{K,\eta}
\left(
\frac{\log H}
{H^3(\log\log H)^2}
\right).
\]

The paper does not claim to prove RH, does not introduce a new Li criterion, and does not introduce a new Weil positivity criterion.

The main proof combines:

1. the classical estimate \(S_1(t)=O(\log t)\);
2. the matched-scale derivative hierarchy for \(\chi_n^{Li}\);
3. a centered primitive of the zero-counting discrepancy;
4. ordinary integration by parts.

I would especially appreciate review of the following points:

1. Is the use of the classical \(S_1(t)=O(\log t)\) bound correctly normalized?
2. Is the ordinary integration-by-parts step valid with \(E(t)=N(t)-M(t)\)?
3. Are the compact-uniform matched-scale estimates for \(\chi_n\), \(\chi_n'\), and \(\chi_n''\) stated correctly?
4. Is the theorem already present in known literature, perhaps under another formulation?
5. Is the result best described as a short specialization of classical \(S_1\)-theory once the Li susceptibility hierarchy is known?

Thank you for any feedback.

