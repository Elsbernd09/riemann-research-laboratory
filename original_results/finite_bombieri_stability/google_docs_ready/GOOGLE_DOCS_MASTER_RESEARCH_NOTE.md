# Explicit \(H\)-Kernel Support-Stability Certificates for Negative Eigenvalue Counts in Finite Bombieri-Style Matrix Models

## Abstract

We study finite normalized matrix models inspired by Bombieri/Weil-style positivity frameworks. Given finite support points \(\Gamma_{\mathrm{dist}}=\{\alpha_1,\ldots,\alpha_N\}\), multiplicities \(m_j>0\), and a finite symbolic \(H\)-kernel, define

\[
M(\Gamma,t)=D^{1/2}A(\Gamma,t)D^{1/2},
\qquad
A(\Gamma,t)_{jk}=H(\alpha_j,\alpha_k;t),
\]

where \(D=\operatorname{diag}(m_1,\ldots,m_N)\).

For support perturbations \(\widetilde \alpha_j\), let

\[
d_j=|\widetilde\alpha_j-\alpha_j|.
\]

We derive a computable compact-domain Lipschitz constant \(L_H(U,t)\) for the finite \(H\)-kernel and define

\[
\mathcal R_F(L_H)
=
L_H(U,t)
\left(
\sum_{j,k}m_jm_k(d_j+d_k)^2
\right)^{1/2},
\]

\[
\mathcal R_{\mathrm{row}}(L_H)
=
\max_j
\sum_k
\sqrt{m_jm_k}L_H(U,t)(d_j+d_k),
\]

and

\[
\mathcal R_{\min}(L_H)
=
\min\{\mathcal R_F(L_H),\mathcal R_{\mathrm{row}}(L_H)\}.
\]

The main finite certificate is

\[
\mathcal R_{\min}(L_H)<g_0(M(\Gamma,t))
\implies
n_-(M(\widetilde\Gamma,t))=
n_-(M(\Gamma,t)).
\]

We also give a certified algorithm that returns `CERTIFIED_STABLE` or `NOT_CERTIFIED`, with a proof that `CERTIFIED_STABLE` is theorem-backed.

This note is finite-dimensional and does not prove, disprove, or verify any claim about the Riemann Hypothesis.

---

## 1. Finite matrix model

Let

\[
\Gamma_{\mathrm{dist}}=\{\alpha_1,\ldots,\alpha_N\}
\]

be a finite support with positive multiplicities \(m_j\). Define

\[
D=\operatorname{diag}(m_1,\ldots,m_N).
\]

Given a finite kernel \(H(x,y;t)\), define

\[
A(\Gamma,t)_{jk}=H(\alpha_j,\alpha_k;t),
\]

and

\[
M(\Gamma,t)=D^{1/2}A(\Gamma,t)D^{1/2}.
\]

The theorem applies when both \(M(\Gamma,t)\) and \(M(\widetilde\Gamma,t)\) are Hermitian.

---

## 2. The finite symbolic \(H\)-kernel

Let

\[
K_t(z)=\frac{\sin(tz)}{tz},
\]

with removable value \(K_t(0)=1\). Let

\[
c_t=\frac{t}{\sinh t}.
\]

Define

\[
K^*(x,y;t)
=
K_t(x-y)
-
c_t\left(\frac12+iy\right)K_t(i/2-y)K_t(i/2+x)
-
c_t\left(\frac12-iy\right)K_t(i/2+y)K_t(i/2-x).
\]

Then

\[
H(x,y;t)
=
\frac{2t}{1/4+y^2}K^*(x,y;t).
\]

---

## 3. Compact-domain hypotheses

Let \(U\subset\mathbb C^2\) be a compact rectangular domain. Assume:

1. all shifted \(K_t\)-arguments lie in a box \(Z(R,S)\);
2. all \(y\)-values lie in \(Y(R_y,S_y)\);
3. the denominator avoids zero:
\[
\Delta_Y=\inf_{y\in Y(R_y,S_y)}|1/4+y^2|>0;
\]
4. \(r>0\) is a Cauchy buffer radius.

Let

\[
\rho_y=\sqrt{R_y^2+S_y^2}.
\]

---

## 4. Explicit \(H\)-kernel Lipschitz constant

Define

\[
A_0=e^{|t|S},
\]

\[
A_1=\frac{\exp(|t|(S+r))}{r},
\]

\[
B_0=\frac{1}{\Delta_Y},
\]

\[
B_1=\frac{2\rho_y}{\Delta_Y^2},
\]

\[
C_0=\frac12+\rho_y.
\]

Define

\[
M_0=A_0+2|c_t|C_0A_0^2,
\]

\[
M_x=A_1+2|c_t|C_0A_0A_1,
\]

\[
M_y=A_1+2|c_t|(A_0^2+C_0A_0A_1).
\]

Finally, define

\[
L_H(U,t)=2|t|B_0M_x+2|t|(B_1M_0+B_0M_y).
\]

---

## 5. Explicit \(H\)-kernel Lipschitz theorem

### Theorem 1

Under the compact-domain hypotheses, for all \((x,y),(x',y')\in U\),

\[
|H(x',y';t)-H(x,y;t)|
\leq
L_H(U,t)(|x'-x|+|y'-y|).
\]

### Proof

The derivative-majorant construction gives

\[
|\partial_xH(x,y;t)|\leq L_x,
\qquad
|\partial_yH(x,y;t)|\leq L_y,
\]

where

\[
L_H(U,t)=L_x+L_y.
\]

Connect \((x,y)\) to \((x',y')\) by the two-segment path

\[
(x,y)\to(x',y)\to(x',y').
\]

The first segment contributes at most \(L_x|x'-x|\), and the second contributes at most \(L_y|y'-y|\). Hence

\[
|H(x',y';t)-H(x,y;t)|
\leq
L_x|x'-x|+L_y|y'-y|
\leq
L_H(U,t)(|x'-x|+|y'-y|).
\]

\[
\square
\]

---

## 6. Spectral-gap stability

For Hermitian \(M\), define

\[
n_-(M)=\#\{j:\lambda_j(M)<0\},
\]

and

\[
g_0(M)=\min_j|\lambda_j(M)|.
\]

If \(E\) is Hermitian and

\[
\|E\|_2<g_0(M),
\]

then

\[
n_-(M+E)=n_-(M).
\]

This follows from the standard Hermitian eigenvalue perturbation bound.

---

## 7. Explicit support-stability certificate

Let

\[
d_j=|\widetilde\alpha_j-\alpha_j|.
\]

Define

\[
\mathcal R_F(L_H)
=
L_H(U,t)
\left(
\sum_{j,k}m_jm_k(d_j+d_k)^2
\right)^{1/2},
\]

\[
\mathcal R_{\mathrm{row}}(L_H)
=
\max_j
\sum_k
\sqrt{m_jm_k}L_H(U,t)(d_j+d_k),
\]

and

\[
\mathcal R_{\min}(L_H)
=
\min\{\mathcal R_F(L_H),\mathcal R_{\mathrm{row}}(L_H)\}.
\]

### Theorem 2

Assume:

1. the compact-domain hypotheses hold;
2. \(M(\Gamma,t)\) and \(M(\widetilde\Gamma,t)\) are Hermitian;
3. \(g_0(M(\Gamma,t))>0\);
4. \(d_j=|\widetilde\alpha_j-\alpha_j|\).

If

\[
\mathcal R_{\min}(L_H)<g_0(M(\Gamma,t)),
\]

then

\[
n_-(M(\widetilde\Gamma,t))=
n_-(M(\Gamma,t)).
\]

### Proof

The explicit Lipschitz theorem shows that \(L_H(U,t)\) is a valid support perturbation Lipschitz constant for \(H\). Therefore the Frobenius and row-sum radii above are valid spectral-norm perturbation upper bounds. Hence

\[
\|M(\widetilde\Gamma,t)-M(\Gamma,t)\|_2
\leq
\mathcal R_{\min}(L_H).
\]

If

\[
\mathcal R_{\min}(L_H)<g_0(M(\Gamma,t)),
\]

then no eigenvalue crosses zero. Thus

\[
n_-(M(\widetilde\Gamma,t))=
n_-(M(\Gamma,t)).
\]

\[
\square
\]

---

## 8. Certified algorithm

The algorithm computes:

1. \(L_H(U,t)\);
2. \(\mathcal R_F(L_H)\);
3. \(\mathcal R_{\mathrm{row}}(L_H)\);
4. \(\mathcal R_{\min}(L_H)\).

It returns:

`CERTIFIED_STABLE`

if

\[
\mathcal R_{\min}(L_H)<g_0(M(\Gamma,t)).
\]

Otherwise it returns:

`NOT_CERTIFIED`.

The output `NOT_CERTIFIED` means only that this certificate did not prove stability. It does not imply instability.

---

## 9. Current status and limitations

The result is a finite-dimensional stability certificate with explicit constants for the finite symbolic \(H\)-kernel.

It does not prove RH.

It does not falsify RH.

It does not verify the zeta case.

It does not establish novelty.

The constants are safe but crude, and the result should be compared with existing literature in matrix perturbation theory, numerical linear algebra, matrix inertia stability, kernel matrix stability, and finite Weil/Bombieri positivity frameworks.


---

# Exact audit strings

GOOGLE_DOCS_MASTER_RESEARCH_NOTE

POLISHED_RESEARCH_NOTE

This note does not prove RH.

This note does not falsify RH.

This note does not use zeta zeros.

This note does not claim novelty.

