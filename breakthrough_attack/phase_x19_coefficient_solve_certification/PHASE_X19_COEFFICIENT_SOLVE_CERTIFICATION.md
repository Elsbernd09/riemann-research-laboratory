# Phase X19 — Coefficient-Solve Certification

## Purpose

Phase X19 attacks a critical gate in the pole-cancelled basis construction.

The corrected basis is:

\[
\Phi=b-\alpha u_0-\beta u_1.
\]

The goal is:

\[
\widehat\Phi(0)=0,
\qquad
\widehat\Phi(1)=0.
\]

This matters because all later \(M_{00}\) term certificates depend on \(\Phi\) being pole-cancelled.

---

# 1. Moment system

Let:

\[
m_s(f)=\widehat f(s).
\]

The correction coefficients \(\alpha,\beta\) solve:

\[
\begin{pmatrix}
m_0(u_0) & m_0(u_1)\\
m_1(u_0) & m_1(u_1)
\end{pmatrix}
\begin{pmatrix}
\alpha\\
\beta
\end{pmatrix}
=
\begin{pmatrix}
m_0(b)\\
m_1(b)
\end{pmatrix}.
\]

Then:

\[
m_0(\Phi)=m_0(b)-\alpha m_0(u_0)-\beta m_0(u_1),
\]

\[
m_1(\Phi)=m_1(b)-\alpha m_1(u_0)-\beta m_1(u_1).
\]

---

# 2. Interval residual certificate

If intervals enclose all moments and coefficient values, then interval arithmetic encloses:

\[
m_0(\Phi),
\qquad
m_1(\Phi).
\]

If both residual intervals contain \(0\) and are very small, the coefficient solve is numerically certified to the chosen interval scale.

---

# 3. Honest blocker

This phase certifies the residual algebra using interval arithmetic.

However, the moment intervals are still wrappers around numerical quadrature values.

Therefore the status is:

\[
\boxed{
\texttt{COEFFICIENT_SOLVE_RESIDUAL_CERTIFIED_MOMENT_INTEGRALS_NOT_CERTIFIED}
}
\]

This is stronger than the previous state, but not yet a fully rigorous moment-integral certificate.

---

# Theorem X19.1 — residual interval enclosure

Assume intervals enclose:

\[
m_s(b),\quad m_s(u_0),\quad m_s(u_1),\quad \alpha,\quad \beta
\]

for \(s\in\{0,1\}\).

Then interval arithmetic applied to:

\[
m_s(b)-\alpha m_s(u_0)-\beta m_s(u_1)
\]

encloses:

\[
m_s(\Phi).
\]

## Proof

The corrected basis is linear:

\[
\Phi=b-\alpha u_0-\beta u_1.
\]

The Mellin moment is linear:

\[
m_s(\Phi)=m_s(b)-\alpha m_s(u_0)-\beta m_s(u_1).
\]

Interval addition, multiplication, and subtraction preserve containment.

\[
\square
\]

---

# Theorem X19.2 — residual certification is incomplete without certified moment integrals

If the input moment intervals are wrappers around uncertified floating quadrature, then residual containment is conditional on those wrappers being valid.

Therefore the coefficient-solve certificate is not fully rigorous until the raw moment integrals are certified.

## Proof

The residual theorem assumes valid interval enclosures of the raw moments.

If those enclosures are not independently certified, the hypothesis is not fully established.

Thus the residual algebra is certified, but the moment-integral layer remains incomplete.

\[
\square
\]

---

# 4. Breakthrough relevance

This phase directly attacks one of the main blockers listed in X18.

After this phase, the coefficient gate becomes more precise:

Old blocker:

\[
\text{coefficient-solve certification missing}
\]

New blocker:

\[
\text{raw Mellin moment integral certification missing}
\]

That is real progress.

---

# 5. Next phase

Phase X20 should harden the numerical/interval layer:

1. outward rounding review;
2. interval arithmetic audit;
3. moment-integral certification plan;
4. exact blocker list for professor review.

---

# Boundary

This phase does not prove RH.

This phase does not prove a breakthrough.

This phase does not establish novelty.

This phase does not compute a fully certified arithmetic entry.

It certifies the coefficient residual algebra and identifies raw Mellin moment certification as the remaining coefficient-layer blocker.

Exact audit strings:

PHASE_X19_COEFFICIENT_SOLVE_CERTIFICATION_COMPLETE

MELLIN_MOMENT_SYSTEM_RECONSTRUCTED

COEFFICIENT_INTERVALS_CREATED

MOMENT_INTERVALS_CREATED

POLE_RESIDUAL_INTERVALS_CREATED

RESIDUAL_INTERVAL_ENCLOSURE_PROVED

COEFFICIENT_SOLVE_RESIDUAL_CERTIFIED_MOMENT_INTEGRALS_NOT_CERTIFIED

RAW_MELLIN_MOMENT_CERTIFICATION_BLOCKER_IDENTIFIED

CERTIFIED_ARITHMETIC_ENTRY_NOT_COMPUTED

READY_FOR_PHASE_X20_OUTWARD_ROUNDING_AND_INTERVAL_AUDIT

