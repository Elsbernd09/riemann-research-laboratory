# Phase 4F Equal-Weight Three-Orbit Search Protocol

## Equation

Search for candidate relations

\[
A_r=A_p+A_q,
\]

with

\[
A_k=c_k^6\sqrt{c_k^2+4}.
\]

## Admissibility constraints

The equal-weight three-orbit parity reduction requires

\[
p\equiv q\pmod2,
\]

\[
r\not\equiv p\pmod2,
\]

and

\[
r>\max(p,q).
\]

The search assumes

\[
p\le q
\]

without loss of generality.

## Search architecture

1. Precompute and cache all blind scales \(c_k\).
2. Precompute all moments \(A_k\).
3. Split the moment sequence into even-index and odd-index subsequences.
4. For each same-parity pair \((p,q)\), compute
   \[
   T=A_p+A_q.
   \]
5. Binary-search T in the opposite-parity moment subsequence.
6. Inspect only the adjacent admissible moments around the insertion point.
7. Enforce \(r>q\).
8. Record global and parity-local normalized defects.

## Global defect

\[
D
=
\frac{|A_r-A_p-A_q|}
{A_r+A_p+A_q}.
\]

## Parity-local defect

If

\[
A_{r_-}<A_p+A_q<A_{r_+}
\]

for consecutive admissible indices of the required parity, define

\[
E
=
\frac{
|A_{r^\star}-A_p-A_q|
}{
A_{r_+}-A_{r_-}
}.
\]

The parity-local denominator uses spacing in the admissible parity subsequence.

Using \(A_{r+1}-A_r\) would be the wrong local scale because \(r+1\) has the forbidden parity.

## Numerical interpretation

A floating-point residual equal to zero is not accepted as proof of an exact mathematical identity.

The search generates candidates and finite-range observations.

Any exceptionally small candidate must undergo separate higher-precision and interval-style validation.
