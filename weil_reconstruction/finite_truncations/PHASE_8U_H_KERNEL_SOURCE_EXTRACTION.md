# Phase 8U — Source-Fill H(gamma,gamma';t) Kernel Formula

## Purpose

Phase 8T created the H-matrix extraction worksheet.

Phase 8U source-fills the first formula-level kernel data for

\[
H(\gamma,\gamma';t).
\]

This phase does not implement the matrix.

This phase does not compute eigenvalues.

This phase does not prove RH.

This phase does not claim novelty.

---

# 1. Source

Enrico Bombieri, **Remarks on Weil's quadratic functional in the theory of prime numbers, I**.

Relevant source region:

Section 7/8 transition, where Bombieri defines \(K\), \(K^*\), \(H\), and then uses \(H(\gamma,\gamma';t)\) in the finite approximation/eigenvalue framework.

---

# 2. Source-extracted base kernel

Bombieri abbreviates

\[
K(x)=\frac{\sin x}{x}.
\]

The source uses the scaled notation

\[
K_t(x)=K(tx)=\frac{\sin(tx)}{tx}.
\]

Status: LOCKED.

---

# 3. Source-extracted corrected kernel

Bombieri introduces a corrected kernel \(K^*(x,y;t)\).

The source-extracted expression is recorded as

\[
K^*(x,y;t)
=
K_t(x-y)
-
\frac{t}{\sinh t}
\left(\frac12+iy\right)
K_t\left(\frac i2-y\right)
K_t\left(\frac i2+x\right)
-
\frac{t}{\sinh t}
\left(\frac12-iy\right)
K_t\left(\frac i2+y\right)
K_t\left(\frac i2-x\right).
\]

This kernel incorporates boundary corrections associated with the finite interval.

Status: SOURCE-EXTRACTED.

---

# 4. Source-extracted H kernel

Bombieri then defines the matrix kernel by

\[
H(x,y;t)
=
\frac{2t\,K^*(x,y;t)}{\frac14+y^2}.
\]

Thus the finite/infinite coefficient system uses

\[
H(\gamma,\gamma';t)
=
\frac{2t\,K^*(\gamma,\gamma';t)}{\frac14+(\gamma')^2}.
\]

Status: SOURCE-EXTRACTED.

---

# 5. Equivalent closed form

The source also displays an equivalent closed form:

\[
H(x,y;t)
=
\frac{
\cosh(t)\cos(t(x-y))-\cos(t(x+y))
}{
2t\sinh(t)
}.
\]

This form must be treated carefully together with the surrounding normalization conventions.

Status: PARTIAL.

Reason:

The OCR/source text around the displayed formulas is visually compressed, so the project records the \(K^*\)-definition and the \(2tK^*/(1/4+y^2)\) definition as the primary implementation target.

---

# 6. Eigenvalue system

Bombieri's transformed system has the form

\[
w_\gamma
=
\Lambda
\sum_{\gamma'\in\Gamma}
H(\gamma,\gamma';t)w_{\gamma'}.
\]

This is the source-level coefficient/eigenvalue equation.

Status: SOURCE-EXTRACTED.

---

# 7. Current lock status

## LOCKED

1. \(K(x)=\sin(x)/x\);
2. \(K_t(x)=K(tx)\);
3. corrected kernel \(K^*(x,y;t)\);
4. \(H(x,y;t)=2tK^*(x,y;t)/(1/4+y^2)\);
5. coefficient equation \(w_\gamma=\Lambda\sum_{\gamma'}H(\gamma,\gamma';t)w_{\gamma'}\).

## PARTIAL

1. closed-form expression for \(H(x,y;t)\);
2. exact Hermitian/self-adjoint convention;
3. how Section 8 finite matrices use \(H\) after boundary constraints;
4. exact Theorem 8 statement.

## STILL BLOCKED

1. finite matrix implementation;
2. eigenvalue computation;
3. negative eigenvalue count claims;
4. Theorem 8 implementation.

---

# 8. Boundary

This is a source formula extraction phase.

No matrix implementation.

No eigenvalue computation.

No RH proof.

No novelty claim.

