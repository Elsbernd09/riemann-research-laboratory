# Phase 10K — Support-Perturbation Model and Lipschitz Kernel Assumption

## Purpose

Phase 10J found that the Phase 10I theorem is correct but likely too close to standard perturbation theory to establish Level 3 significance.

Phase 10K begins the stronger target:

\[
\textbf{Support Perturbation Stability for Finite Bombieri-Style Matrices.}
\]

Instead of assuming entrywise matrix error directly, we now model perturbations of the finite support points themselves.

---

# 1. Locked finite matrix model

Recall the normalized finite matrix

\[
M(\Gamma,t)=D^{1/2}A(\Gamma,t)D^{1/2},
\]

where

\[
A_{jk}(\Gamma,t)=H_t(\alpha_j,\alpha_k),
\]

and

\[
D=\operatorname{diag}(m_1,\ldots,m_N).
\]

The distinct support is

\[
\Gamma_{\mathrm{dist}}=\{\alpha_1,\ldots,\alpha_N\}.
\]

---

# 2. Perturbed support

Let

\[
\widetilde\Gamma_{\mathrm{dist}}
=
\{\widetilde\alpha_1,\ldots,\widetilde\alpha_N\}
\]

be a perturbed support with the same indexing and the same multiplicities.

Assume

\[
|\widetilde\alpha_j-\alpha_j|\leq\delta
\]

for every \(j\).

The perturbed normalized matrix is

\[
\widetilde M
=
M(\widetilde\Gamma,t)
=
D^{1/2}A(\widetilde\Gamma,t)D^{1/2},
\]

where

\[
A_{jk}(\widetilde\Gamma,t)
=
H_t(\widetilde\alpha_j,\widetilde\alpha_k).
\]

---

# 3. Kernel Lipschitz assumption

Let

\[
U\subset\mathbb C
\]

be a neighborhood containing all original and perturbed support points.

Assume that the kernel

\[
H_t:U\times U\to\mathbb C
\]

is Lipschitz in both variables on \(U\times U\).

That is, there exists a finite constant

\[
L_t(U)
\]

such that for all \(x,y,x',y'\in U\),

\[
|H_t(x',y')-H_t(x,y)|
\leq
L_t(U)\left(|x'-x|+|y'-y|\right).
\]

---

# 4. Immediate support-to-kernel bound

If

\[
|\widetilde\alpha_j-\alpha_j|\leq\delta
\]

and

\[
|\widetilde\alpha_k-\alpha_k|\leq\delta,
\]

then the Lipschitz assumption gives

\[
|H_t(\widetilde\alpha_j,\widetilde\alpha_k)-H_t(\alpha_j,\alpha_k)|
\leq
L_t(U)(\delta+\delta)
=
2L_t(U)\delta.
\]

Thus the support perturbation implies a uniform kernel-entry perturbation bound

\[
\eta=2L_t(U)\delta.
\]

---

# 5. Immediate support-to-matrix bound

Since

\[
M_{jk}
=
\sqrt{m_j}H_t(\alpha_j,\alpha_k)\sqrt{m_k},
\]

and

\[
\widetilde M_{jk}
=
\sqrt{m_j}H_t(\widetilde\alpha_j,\widetilde\alpha_k)\sqrt{m_k},
\]

we get

\[
|\widetilde M_{jk}-M_{jk}|
\leq
\sqrt{m_jm_k}\,2L_t(U)\delta.
\]

Let

\[
m_{\max}=\max_jm_j.
\]

Then

\[
|\widetilde M_{jk}-M_{jk}|
\leq
2m_{\max}L_t(U)\delta.
\]

Therefore the normalized matrix-entry perturbation level is

\[
\varepsilon=2m_{\max}L_t(U)\delta.
\]

---

# 6. Expected stability certificate

By Theorem 10G, a sufficient stability certificate will be

\[
N\varepsilon<g_0(M).
\]

Substituting

\[
\varepsilon=2m_{\max}L_t(U)\delta
\]

gives the support-level certificate

\[
2Nm_{\max}L_t(U)\delta<g_0(M).
\]

When this holds, the expected conclusion is

\[
n_-(M(\widetilde\Gamma,t))=n_-(M(\Gamma,t)).
\]

---

# 7. Why this is stronger than Phase 10G

Phase 10G assumed entrywise matrix error.

Phase 10K derives entrywise matrix error from perturbations of the support points.

This is more specific to finite kernel models and therefore closer to the Level 3 target.

---

# 8. Boundary

This is a finite synthetic support-perturbation model.

This phase does not prove RH.

This phase does not falsify RH.

This phase does not use zeta zeros.

This phase does not verify the zeta case.

This phase does not claim novelty.

