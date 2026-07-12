# Theorem Map

## A. Provisional Weil-form construction

### A1. Star and convolution

\[
g^*(x)=x^{-1}\overline{g(1/x)}
\]

\[
F_g=g*g^*
\]

### A2. Mellin identities proved

\[
\widehat{g^*}(s)=\overline{\widehat g(1-\bar s)}
\]

\[
\widehat{g*g^*}(s)=\widehat g(s)\overline{\widehat g(1-\bar s)}
\]

### A3. Provisional spectral form

\[
Q_W(g)=\sum_\rho \widehat g(\rho)\overline{\widehat g(1-\bar\rho)}.
\]

---

## B. Finite spectral detection

### B1. Projection on finite class

For

\[
g\in\mathcal F_R^{(m)},
\]

identity projection gives

\[
\pi_m(R,m)=0.
\]

### B2. Tail Gram bound

\[
\sup_{g\in\mathcal F_R^{(m)}}|Q_W(g)-Q_Y(g)|
\le R^2m\delta_Y^{(m)}.
\]

### B3. Mellin decay

For log-smooth compact basis functions,

\[
|\widehat\phi(\sigma+it)|\le C_A(1+|t|)^{-A}.
\]

### B4. Truncation convergence

Assuming a classical zero-count shell bound,

\[
\delta_Y^{(m)}\to0.
\]

### B5. Negative detection

If

\[
Q_W(g)\le-\eta,
\]

then for sufficiently large \(Y\),

\[
Q_Y(g)<-\eta/2.
\]

---

## C. Arithmetic-side reductions

### C1. Compact-support support bound

If

\[
\operatorname{supp}(g)\subset[e^{-B},e^B],
\]

then

\[
\operatorname{supp}(F_g)\subset[e^{-2B},e^{2B}].
\]

### C2. Prime-tail vanishing

The prime sum has no terms above

\[
e^{2B}.
\]

### C3. Archimedean tail

\[
\int_M^\infty
\left(-\frac{2F_g(1)}x\right)
\frac{x\,dx}{x^2-1}
=
-F_g(1)\log\left(\frac{M+1}{M-1}\right).
\]

### C4. Value at one

\[
F_g(1)=\int_0^\infty |g(y)|^2dy.
\]

### C5. Arithmetic matrix entries

\[
M_{ij}^{arith}=T[\phi_j*\phi_i^*].
\]

\[
M_{ij}^{arith}
=
I_{ij}^{0}
+
I_{ij}^{*,0}
-
P_{ij}
-
C_{ij}
-
A_{ij}.
\]

---

## D. Conditional Hermitian gate

If

\[
T[F^*]=\overline{T[F]},
\]

then

\[
M^{arith}
\]

is Hermitian.

This remains a gate requiring source validation or direct proof.

