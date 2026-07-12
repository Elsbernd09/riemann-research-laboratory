# Phase 12M — Concrete Basis Mellin Decay

## Purpose

Phase 12L proved that spectral truncation convergence on a finite test class follows if the basis functions satisfy sufficient Mellin decay.

Phase 12M chooses a concrete basis class and proves Mellin decay estimates.

---

# 1. Log-coordinate basis functions

Let

\[
x=e^u.
\]

Choose basis functions of the form

\[
\phi_j(x)=\psi_j(\log x),
\]

where

\[
\psi_j\in C_c^\infty(\mathbb R).
\]

Thus each \(\psi_j\) is smooth and compactly supported in a finite interval.

This gives a concrete finite test class:

\[
\mathcal F_R^{(m)}
=
\left\{
g(x)=\sum_{j=1}^{m}a_j\psi_j(\log x):\|a\|_2\le R
\right\}.
\]

---

# 2. Mellin transform in log coordinates

For

\[
\phi(x)=\psi(\log x),
\]

the Mellin transform is

\[
\widehat\phi(s)=\int_0^\infty \phi(x)x^{s-1}\,dx.
\]

Set

\[
x=e^u.
\]

Then

\[
dx=e^u\,du,
\]

and

\[
x^{s-1}dx=e^{(s-1)u}e^u\,du=e^{su}\,du.
\]

Therefore,

\[
\widehat\phi(s)=\int_{-\infty}^{\infty}\psi(u)e^{su}\,du.
\]

If

\[
s=\sigma+it,
\]

then

\[
\widehat\phi(\sigma+it)
=
\int_{-\infty}^{\infty}\psi(u)e^{\sigma u}e^{itu}\,du.
\]

This is the Fourier transform of the compactly supported smooth function

\[
\psi_\sigma(u)=\psi(u)e^{\sigma u}.
\]

---

# Theorem 12M.1 — Rapid Mellin decay for log-smooth compact support

Let

\[
\phi(x)=\psi(\log x)
\]

with

\[
\psi\in C_c^\infty(\mathbb R).
\]

Fix a compact vertical strip

\[
\sigma\in[\sigma_-,\sigma_+].
\]

Then for every integer

\[
A\ge0
\]

there exists a constant

\[
C_{\phi,A,\sigma_-,\sigma_+}
\]

such that

\[
|\widehat\phi(\sigma+it)|
\le
C_{\phi,A,\sigma_-,\sigma_+}(1+|t|)^{-A}
\]

for all

\[
\sigma\in[\sigma_-,\sigma_+]
\]

and all real \(t\).

## Proof

Write

\[
\widehat\phi(\sigma+it)
=
\int_{\mathbb R}\psi(u)e^{\sigma u}e^{itu}\,du.
\]

Let

\[
h_\sigma(u)=\psi(u)e^{\sigma u}.
\]

Since \(\psi\in C_c^\infty(\mathbb R)\), the support of \(h_\sigma\) is contained in the fixed compact support of \(\psi\), independent of \(\sigma\).

For \(\sigma\in[\sigma_-,\sigma_+]\), all derivatives

\[
h_\sigma^{(A)}(u)
\]

are uniformly bounded on the support.

For \(t\neq0\), integrate by parts \(A\) times:

\[
\int h_\sigma(u)e^{itu}\,du
=
(it)^{-A}
\int h_\sigma^{(A)}(u)e^{itu}\,du,
\]

with no boundary terms because \(h_\sigma\) is compactly supported and smooth.

Thus,

\[
|\widehat\phi(\sigma+it)|
\le
|t|^{-A}\int |h_\sigma^{(A)}(u)|\,du.
\]

The integral is uniformly bounded for

\[
\sigma\in[\sigma_-,\sigma_+].
\]

For bounded \(t\), enlarge the constant.

Therefore,

\[
|\widehat\phi(\sigma+it)|
\le
C_{\phi,A,\sigma_-,\sigma_+}(1+|t|)^{-A}.
\]

\[
\square
\]

---

# 3. Product decay for tail entries

The tail entry involves

\[
\widehat{\phi_i}(\rho)
\overline{\widehat{\phi_j}(1-\bar\rho)}.
\]

For nontrivial zeros,

\[
0<\operatorname{Re}\rho<1.
\]

Thus both arguments

\[
\rho
\]

and

\[
1-\bar\rho
\]

lie in the vertical strip

\[
0<\sigma<1.
\]

Use any compact strip slightly larger, for example

\[
\sigma\in[0,1].
\]

---

# Theorem 12M.2 — Product Mellin decay for basis pairs

Let

\[
\phi_i(x)=\psi_i(\log x),
\qquad
\phi_j(x)=\psi_j(\log x),
\]

with

\[
\psi_i,\psi_j\in C_c^\infty(\mathbb R).
\]

For every

\[
A>0
\]

there exists a constant

\[
C_{ij,A}
\]

such that for every nontrivial zero

\[
\rho=\beta+i\gamma,
\]

\[
\left|
\widehat{\phi_i}(\rho)
\overline{\widehat{\phi_j}(1-\bar\rho)}
\right|
\le
C_{ij,A}(1+|\gamma|)^{-A}.
\]

## Proof

By Theorem 12M.1, for any \(B>0\),

\[
|\widehat{\phi_i}(\rho)|
\le
C_{i,B}(1+|\gamma|)^{-B},
\]

uniformly for

\[
0\le\beta\le1.
\]

Also,

\[
1-\bar\rho=1-\beta+i\gamma,
\]

so

\[
|\operatorname{Im}(1-\bar\rho)|=|\gamma|
\]

and

\[
0\le1-\beta\le1.
\]

Again by Theorem 12M.1,

\[
|\widehat{\phi_j}(1-\bar\rho)|
\le
C_{j,B}(1+|\gamma|)^{-B}.
\]

Therefore,

\[
\left|
\widehat{\phi_i}(\rho)
\overline{\widehat{\phi_j}(1-\bar\rho)}
\right|
\le
C_{i,B}C_{j,B}(1+|\gamma|)^{-2B}.
\]

Choose \(B\) so that

\[
2B\ge A.
\]

Then

\[
\left|
\widehat{\phi_i}(\rho)
\overline{\widehat{\phi_j}(1-\bar\rho)}
\right|
\le
C_{ij,A}(1+|\gamma|)^{-A}.
\]

\[
\square
\]

---

# 4. Shell decay bound

For zeros in the shell

\[
k<|\gamma|\le k+1,
\]

Theorem 12M.2 gives

\[
A_{ij}(k)\le C_{ij,A}(1+k)^{-A}.
\]

Thus the Phase 12L shell-count bound applies.

---

# 5. Zero shell count input

A standard zero-count estimate gives shell growth of the form

\[
Z(k)\le C_Z(1+\log(k+2))
\]

for the number of nontrivial zeta zeros with

\[
k<|\operatorname{Im}\rho|\le k+1.
\]

This is treated here as a classical input still requiring primary-source citation.

---

# Theorem 12M.3 — Basis decay implies \(\delta_Y^{(m)}\to0\)

Assume the shell zero-count bound

\[
Z(k)\le C_Z(1+\log(k+2)).
\]

For log-smooth compactly supported basis functions

\[
\phi_j(x)=\psi_j(\log x),
\qquad
\psi_j\in C_c^\infty(\mathbb R),
\]

define

\[
\delta_Y^{(m)}
=
\max_{1\le i,j\le m}
\sum_{k>\lfloor Y\rfloor}Z(k)A_{ij}(k).
\]

Then

\[
\delta_Y^{(m)}\to0
\]

as

\[
Y\to\infty.
\]

## Proof

By Theorem 12M.2, choose \(A>2\) and constants \(C_{ij,A}\) such that

\[
A_{ij}(k)\le C_{ij,A}(1+k)^{-A}.
\]

Using the zero-count bound,

\[
Z(k)A_{ij}(k)
\le
C_ZC_{ij,A}(1+\log(k+2))(1+k)^{-A}.
\]

Since

\[
A>2,
\]

the series

\[
\sum_{k=1}^{\infty}(1+\log(k+2))(1+k)^{-A}
\]

converges.

Therefore its tail tends to zero:

\[
\sum_{k>\lfloor Y\rfloor}(1+\log(k+2))(1+k)^{-A}\to0.
\]

For fixed finite \(m\), the maximum over finitely many pairs \(i,j\) also tends to zero.

Thus

\[
\delta_Y^{(m)}\to0.
\]

\[
\square
\]

---

# Corollary 12M.4 — Spectral truncation convergence on the concrete finite class

For the concrete finite test class generated by

\[
\phi_j(x)=\psi_j(\log x),
\qquad
\psi_j\in C_c^\infty(\mathbb R),
\]

assuming the classical zero shell-count bound,

\[
\sup_{g\in\mathcal F_R^{(m)}}|Q_W(g)-Q_Y(g)|
\to0
\]

as

\[
Y\to\infty.
\]

## Proof

By Theorem 12M.3,

\[
\delta_Y^{(m)}\to0.
\]

By Phase 12L,

\[
\sup_{g\in\mathcal F_R^{(m)}}|Q_W(g)-Q_Y(g)|
\le
R^2m\delta_Y^{(m)}.
\]

Therefore the left-hand side tends to zero.

\[
\square
\]

---

# 6. Why this matters

This is a real finite-class convergence result for spectral truncation, conditional on:

1. the provisional \(Q_W\) conventions;
2. the classical zero-count shell bound;
3. the chosen log-smooth compactly supported basis.

It gives:

\[
\tau_Y(R,m)\to0.
\]

Combined with Phase 12K,

\[
\pi_m(R,m)=0.
\]

So under provisional conventions and certified computation,

\[
\sup_{g\in\mathcal F_R^{(m)}}|Q_Y(g)-Q_W(g)|
\to0.
\]

This is the closest the project has gotten to a serious Level 4 candidate pathway.

---

# 7. Still not solved

This is still not an RH breakthrough because:

1. primary-source confirmation is still required;
2. the zero-count shell estimate needs source citation;
3. \(Q_Y\) is a spectral zero truncation, not yet an arithmetic-only finite certificate;
4. finite computation would require certified zero data or an arithmetic-side replacement;
5. the full converse Weil criterion is not proved here;
6. no new result about RH itself is proved.

---

# 8. Next target

Phase 12N should synthesize the finite-class spectral convergence theorem:

\[
\sup_{g\in\mathcal F_R^{(m)}}|Q_Y(g)-Q_W(g)|\to0.
\]

Then it should combine with Phase 12H negative detection:

If

\[
Q_W(g)\le-\eta,
\]

then for large \(Y\),

\[
Q_Y(g)<-\eta/2.
\]

That would be a finite spectral negative-obstruction detection theorem.

It is still not an RH proof, but it is a real finite-to-infinite detection theorem under provisional conventions.

---

# Boundary

This phase does not prove RH.

This phase does not falsify RH.

This phase does not prove a new RH criterion.

This phase does not prove the full Weil positivity theorem.

This phase does not prove an arithmetic-only finite certificate.

This phase does not establish novelty.

Exact audit strings:

BASIS_MELLIN_DECAY_COMPLETE

LOG_SMOOTH_COMPACT_BASIS_DEFINED

MELLIN_RAPID_DECAY_PROVED

PRODUCT_MELLIN_DECAY_PROVED

BASIS_DECAY_IMPLIES_DELTA_Y_TO_ZERO

SPECTRAL_TRUNCATION_CONVERGENCE_PROVED_ON_FINITE_CLASS

ZERO_COUNT_BOUND_CLASSICAL_INPUT_REQUIRED

ARITHMETIC_ONLY_CERTIFICATE_NOT_YET_PROVED

LEVEL4_BREAKTHROUGH_CANDIDATE_NOT_YET_ACHIEVED

