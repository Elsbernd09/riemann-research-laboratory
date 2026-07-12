# Phase 10AP — Convergence Theorem Skeleton

## Purpose

Phase 10AO identified the central contribution bottleneck:

\[
|Q_N(P_N^W f)-Q_W(f)|\leq \varepsilon_N(f),
\qquad
\varepsilon_N(f)\to0.
\]

Phase 10AP builds the exact theorem skeleton needed to turn finite certified stability into a meaningful infinite-form statement.

This phase does not prove convergence.

This phase does not prove RH.

This phase does not claim novelty.

It identifies the exact theorem that would be needed for a serious contribution.

---

# 1. Infinite object

Let

\[
Q_W:\mathcal D_W\to\mathbb R
\]

be the true Weil/Bombieri quadratic form on an admissible test-function domain

\[
\mathcal D_W.
\]

At this stage, \(Q_W\) is still not fully imported.

Therefore this phase treats \(Q_W\) as the target classical object.

---

# 2. Finite objects

Let

\[
V_N^W
\]

be finite-dimensional approximation spaces.

Let

\[
M_N^W
\]

be Hermitian matrices representing finite Weil/Bombieri-style forms.

Define

\[
Q_N^W(v)=v^*M_N^Wv.
\]

Let

\[
P_N^W:\mathcal D_W\to V_N^W
\]

be approximation maps.

---

# 3. Pointwise convergence target

The weakest required convergence is:

\[
Q_N^W(P_N^Wf)\to Q_W(f)
\]

for every fixed

\[
f\in\mathcal D_W.
\]

This is enough for abstract positivity transfer and negative-direction detection, but it may not be enough for robust computation.

---

# 4. Quantitative convergence target

A stronger and more useful target is:

\[
|Q_N^W(P_N^Wf)-Q_W(f)|
\leq
\varepsilon_N(f),
\]

where

\[
\varepsilon_N(f)\to0.
\]

This is the minimum serious target for certified computation.

---

# 5. Uniform convergence target

For a bounded or controlled class

\[
\mathcal F\subset\mathcal D_W,
\]

one may seek

\[
\sup_{f\in\mathcal F}
|Q_N^W(P_N^Wf)-Q_W(f)|
\leq
\varepsilon_N(\mathcal F),
\]

with

\[
\varepsilon_N(\mathcal F)\to0.
\]

This would be much stronger and more useful for computational certification.

---

# 6. Form convergence target

If the forms can be represented on a Hilbert or pre-Hilbert space, one may seek convergence of quadratic forms:

\[
Q_N^W(P_N^Wf)\to Q_W(f)
\]

plus compatibility with polarization:

\[
B_N^W(P_N^Wf,P_N^Wg)\to B_W(f,g).
\]

This would connect the finite matrix framework more directly to operator-theoretic methods.

---

# 7. Operator-norm convergence target

In the strongest setting, suppose the finite forms correspond to finite-rank operators approximating an infinite operator \(A_W\).

Then one could seek

\[
\|A_N-A_W\|\to0
\]

in an appropriate operator topology.

This is likely too strong for the current project, but it gives a useful upper target.

---

# Theorem 10AP.1 — Pointwise convergence transfer skeleton

Assume:

1. \(Q_W:\mathcal D_W\to\mathbb R\) is the true Weil/Bombieri form;
2. \(Q_N^W(v)=v^*M_N^Wv\) are finite Hermitian forms;
3. \(P_N^W:\mathcal D_W\to V_N^W\);
4. for every \(f\in\mathcal D_W\),

\[
Q_N^W(P_N^Wf)\to Q_W(f).
\]

Then the abstract transfer theorems from Phase 10AK apply to \(Q_W\).

In particular:

If finite forms are eventually nonnegative, then \(Q_W\) is nonnegative.

If \(Q_W\) has a negative direction, finite forms eventually detect negativity.

## Proof

This is the direct specialization of Phase 10AK to the classical Weil/Bombieri objects.

\[
\square
\]

---

# Theorem 10AP.2 — Quantitative certified negativity skeleton

Assume:

1. \(Q_W(f)\leq-\eta\) for some \(f\in\mathcal D_W\) and \(\eta>0\);
2. the quantitative convergence bound holds:

\[
|Q_N^W(P_N^Wf)-Q_W(f)|\leq \varepsilon_N(f);
\]

3. for all sufficiently large \(N\),

\[
\varepsilon_N(f)<\eta/2.
\]

Then

\[
Q_N^W(P_N^Wf)<-\eta/2
\]

for all sufficiently large \(N\).

## Proof

By the quantitative bound,

\[
Q_N^W(P_N^Wf)
\leq
Q_W(f)+\varepsilon_N(f).
\]

Using

\[
Q_W(f)\leq-\eta
\]

and

\[
\varepsilon_N(f)<\eta/2,
\]

we get

\[
Q_N^W(P_N^Wf)<-\eta+\eta/2=-\eta/2.
\]

\[
\square
\]

---

# Theorem 10AP.3 — Certified computed detection skeleton

Assume:

1. \(\widetilde M_N^W\) is a computed approximation to \(M_N^W\);
2. \(\|M_N^W-\widetilde M_N^W\|_2<\mu_N\);
3. \(v_N\in V_N^W\) is a unit vector;
4. \(v_N^*\widetilde M_N^Wv_N<-\mu_N\).

Then

\[
v_N^*M_N^Wv_N<0.
\]

## Proof

This is the finite certified negativity theorem specialized to \(M_N^W\).

\[
\square
\]

---

# 8. Required future theorem

The theorem that would make the project meaningfully stronger is:

## Target Theorem 10AP-T

For a class of admissible Weil/Bombieri test functions \(\mathcal F\subset\mathcal D_W\), prove an explicit bound

\[
\sup_{f\in\mathcal F}
|Q_N^W(P_N^Wf)-Q_W(f)|
\leq
\varepsilon_N(\mathcal F),
\qquad
\varepsilon_N(\mathcal F)\to0.
\]

This is the main convergence target.

---

# 9. Contribution significance

If Target Theorem 10AP-T can be proven for a genuine classical \(Q_W\), then the project could contribute a rigorous bridge:

\[
\text{certified finite matrix computation}
\Rightarrow
\text{controlled statement about infinite Weil/Bombieri form}.
\]

That would still not automatically prove RH.

But it would be a real RH-adjacent computational contribution.

---

# 10. Current status

The convergence theorem is now precisely stated.

It is not proven.

The classical objects are still not fully imported.

The project is still not an RH contribution.

But the next theorem target is now mathematically explicit.

---

# Boundary

This phase does not prove RH.

This phase does not falsify RH.

This phase does not prove a new RH criterion.

This phase does not prove convergence.

This phase does not claim novelty.

Exact audit strings:

CONVERGENCE_THEOREM_SKELETON

POINTWISE_CONVERGENCE_TARGET

QUANTITATIVE_CONVERGENCE_TARGET

UNIFORM_CONVERGENCE_TARGET

FORM_CONVERGENCE_TARGET

OPERATOR_NORM_CONVERGENCE_TARGET

TARGET_THEOREM_10AP_T

CONVERGENCE_NOT_PROVEN

NOT_RH_CONTRIBUTION_YET

