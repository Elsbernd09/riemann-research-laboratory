# Explicit H-Kernel Support-Stability Certificates for Negative Eigenvalue Counts in Finite Bombieri-Style Matrix Models

## Abstract

We study finite normalized matrix models inspired by Bombieri/Weil-style positivity frameworks. Given support points \(\Gamma_{\mathrm{dist}}=\{\alpha_1,\ldots,\alpha_N\}\), multiplicities \(m_j\), and the finite symbolic \(H\)-kernel, define

\[
M(\Gamma,t)=D^{1/2}A(\Gamma,t)D^{1/2},
\qquad
A(\Gamma,t)_{jk}=H(\alpha_j,\alpha_k;t).
\]

Earlier drafts assumed an abstract local Lipschitz constant \(L_t(U)\). This version replaces that assumption with a computable finite \(H\)-kernel constant

\[
L_H(U,t)=2|t|B_0M_x+2|t|(B_1M_0+B_0M_y).
\]

Using this constant, we define Frobenius and row-sum perturbation radii

\[
\mathcal R_F(L_H)
=
L_H(U,t)
\left(
\sum_{j,k}m_jm_k(d_j+d_k)^2
\right)^{1/2},
\]

and

\[
\mathcal R_{\mathrm{row}}(L_H)
=
\max_j
\sum_k
\sqrt{m_jm_k}L_H(U,t)(d_j+d_k).
\]

Let

\[
\mathcal R_{\min}(L_H)
=
\min\{\mathcal R_F(L_H),\mathcal R_{\mathrm{row}}(L_H)\}.
\]

The main finite certificate is:

\[
\mathcal R_{\min}(L_H)<g_0(M(\Gamma,t))
\implies
n_-(M(\widetilde\Gamma,t))=
n_-(M(\Gamma,t)).
\]

The result is finite-dimensional. It does not prove RH, falsify RH, use zeta zeros, verify the zeta case, or claim novelty.

---

# 1. Motivation

Finite eigenvalue computations near zero are unstable. If a finite Bombieri-style matrix model produces a negative eigenvalue count, that count should be interpreted only when protected by a spectral-gap certificate.

The goal of this note is to build such a certificate for finite support perturbations.

The project now has three layers:

1. finite spectral-gap stability;
2. combined-radius support perturbation bounds;
3. an explicit computable \(H\)-kernel Lipschitz constant.

---

# 2. Finite normalized matrix model

Let

\[
\Gamma_{\mathrm{dist}}=\{\alpha_1,\ldots,\alpha_N\}
\]

be a finite support with positive multiplicities

\[
m_1,\ldots,m_N.
\]

Let

\[
D=\operatorname{diag}(m_1,\ldots,m_N).
\]

Define

\[
A(\Gamma,t)_{jk}=H(\alpha_j,\alpha_k;t),
\]

and

\[
M(\Gamma,t)=D^{1/2}A(\Gamma,t)D^{1/2}.
\]

The theorem applies only when the original and perturbed matrices are Hermitian.

---

# 3. The finite \(H\)-kernel

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

# 4. Compact-domain hypotheses

Let \(U\subset\mathbb C^2\) be a compact rectangular domain for \((x,y)\). Assume:

1. all shifted \(K_t\)-arguments lie in \(Z(R,S)\);
2. all \(y\)-values lie in \(Y(R_y,S_y)\);
3. the rational denominator avoids zero:
\[
\Delta_Y=
\inf_{y\in Y(R_y,S_y)}
|1/4+y^2|
>0;
\]
4. \(r>0\) is a Cauchy buffer radius for the \(K_t\)-derivative estimate.

Define

\[
\rho_y=\sqrt{R_y^2+S_y^2}.
\]

---

# 5. Concrete majorants

The concrete compact-domain majorants are:

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

Then define

\[
M_0=A_0+2|c_t|C_0A_0^2,
\]

\[
M_x=A_1+2|c_t|C_0A_0A_1,
\]

and

\[
M_y=A_1+2|c_t|(A_0^2+C_0A_0A_1).
\]

Finally,

\[
L_H(U,t)=2|t|B_0M_x+2|t|(B_1M_0+B_0M_y).
\]

---

# 6. Explicit \(H\)-kernel Lipschitz theorem

## Theorem 6.1

Under the compact-domain hypotheses, for all

\[
(x,y),(x',y')\in U,
\]

the finite \(H\)-kernel satisfies

\[
|H(x',y';t)-H(x,y;t)|
\leq
L_H(U,t)(|x'-x|+|y'-y|).
\]

## Proof

The derivative majorant construction gives

\[
|\partial_xH(x,y;t)|\leq L_x
\]

and

\[
|\partial_yH(x,y;t)|\leq L_y.
\]

For the rectangular compact domain, connect \((x,y)\) to \((x',y')\) by the two-segment path

\[
(x,y)\to(x',y)\to(x',y').
\]

The first segment contributes at most

\[
L_x|x'-x|.
\]

The second contributes at most

\[
L_y|y'-y|.
\]

Thus

\[
|H(x',y';t)-H(x,y;t)|
\leq
L_x|x'-x|+L_y|y'-y|.
\]

Since

\[
L_H(U,t)=L_x+L_y,
\]

we get

\[
|H(x',y';t)-H(x,y;t)|
\leq
L_H(U,t)(|x'-x|+|y'-y|).
\]

\[
\square
\]

---

# 7. Spectral-gap principle

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

---

# 8. Explicit combined-radius certificate

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

and

\[
\mathcal R_{\mathrm{row}}(L_H)
=
\max_j
\sum_k
\sqrt{m_jm_k}L_H(U,t)(d_j+d_k).
\]

Let

\[
\mathcal R_{\min}(L_H)
=
\min\{\mathcal R_F(L_H),\mathcal R_{\mathrm{row}}(L_H)\}.
\]

## Theorem 8.1 — Explicit \(H\)-kernel support-stability certificate

Assume:

1. the compact-domain hypotheses for \(H\);
2. \(M(\Gamma,t)\) and \(M(\widetilde\Gamma,t)\) are Hermitian;
3. \(g_0(M(\Gamma,t))>0\);
4. the support displacements are \(d_j=|\widetilde\alpha_j-\alpha_j|\).

If

\[
\mathcal R_{\min}(L_H)<g_0(M(\Gamma,t)),
\]

then

\[
n_-(M(\widetilde\Gamma,t))=
n_-(M(\Gamma,t)).
\]

## Proof

The explicit Lipschitz theorem allows the abstract constant \(L_t(U)\) in the combined-radius theorem to be replaced by \(L_H(U,t)\). Therefore,

\[
\mathcal R_{\min}(L_H)
\]

is a valid spectral-norm perturbation upper bound. If this radius is smaller than \(g_0(M(\Gamma,t))\), the spectral-gap principle gives

\[
n_-(M(\widetilde\Gamma,t))=
n_-(M(\Gamma,t)).
\]

\[
\square
\]

---

# 9. Certified algorithm

The certified algorithm now computes:

1. the compact-domain majorants;
2. \(L_H(U,t)\);
3. \(\mathcal R_F(L_H)\);
4. \(\mathcal R_{\mathrm{row}}(L_H)\);
5. \(\mathcal R_{\min}(L_H)\).

It returns:

CERTIFIED_STABLE

if

\[
\mathcal R_{\min}(L_H)<g_0(M(\Gamma,t)).
\]

Otherwise it returns:

NOT_CERTIFIED

NOT_CERTIFIED does not imply instability.

---

# 10. Current strongest finite result

The strongest finite result in the project is now:

\[
\boxed{
\mathcal R_{\min}(L_H)<g_0(M(\Gamma,t))
\implies
n_-(M(\widetilde\Gamma,t))=
n_-(M(\Gamma,t)).
}
\]

This is more specialized than the earlier abstract stability result because \(L_H\) is built from the finite symbolic \(H\)-kernel.

---

# 11. Limitations

This note remains finite-dimensional.

The constants are safe but crude.

The result depends on compact-domain hypotheses.

It does not prove convergence to the infinite zeta setting.

It does not verify actual zeta zeros.

It does not prove RH.

It does not establish novelty relative to known matrix perturbation and kernel-stability literature.

---

# Boundary

This note does not prove RH.

This note does not falsify RH.

This note does not use zeta zeros.

This note does not verify the zeta case.

This note does not claim novelty.

Exact audit strings:

RESEARCH_NOTE_V5

EXPLICIT_H_KERNEL_LIPSCHITZ_THEOREM

H_KERNEL_STABILITY_INSERTION

EXPLICIT_H_KERNEL_SUPPORT_STABILITY_CERTIFICATE

CERTIFIED_STABLE

NOT_CERTIFIED

