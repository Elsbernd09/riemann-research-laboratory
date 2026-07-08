# Phase 4E Weight Tuning and Rigid Multi-Orbit Cancellation

## Main correction to the research question

With arbitrary positive real orbit weights, exact fourth-order cancellation in a mixed-parity fully resonant family is not difficult to engineer.

The cancellation equation is one linear constraint:

\[
\sum_{k_j\ {\rm odd}}w_jA_{k_j}
=
\sum_{k_j\ {\rm even}}w_jA_{k_j}.
\]

Thus an unconstrained continuous-weight optimizer would manufacture cancellation by tuning one degree of freedom.

The project will not treat such a result as a rigid resonance discovery.

## Meaningful restrictions

The important cases are:

- equal orbit weights;
- positive integer multiplicities.

For equal weights the problem becomes a signed relation in the fixed sequence

\[
A_k=c_k^6\sqrt{c_k^2+4}.
\]

For three orbits, exact cancellation requires

\[
A_r=A_p+A_q,
\]

where the unique-parity index \(r\) must satisfy

\[
r>\max(p,q).
\]

## Asymptotic search geometry

Since

\[
A_k\sim\pi^7(k+1/2)^7,
\]

candidate large-index triples should lie near

\[
(r+1/2)^7
\approx
(p+1/2)^7+(q+1/2)^7.
\]

This resemblance does not convert the problem into Fermat's Last Theorem.

## Next phase

Phase 4F should perform a mathematically targeted equal-weight three-orbit search.

The search should exploit:

- parity;
- strict monotonicity;
- the ordering condition \(r>\max(p,q)\);
- monotone two-sum search rather than cubic brute force;
- normalized defect rather than raw absolute residual.

Before interpreting any near-cancellation, the project must compare the observed defect against the natural local spacing scale of the sequence \(A_k\).
