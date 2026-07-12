# A Conditional Finite-to-Infinite Transfer Framework for Certified Gram-Matrix Approximations in Weil/Bombieri-Style Models

## Abstract

We develop a conditional finite-to-infinite transfer framework for finite Gram-matrix approximations associated with Weil/Bombieri-style quadratic forms. For a finite bounded test class

\[
\mathcal F_R^{(m)}
=
\left\{
f=\sum_{j=1}^{m}a_j\phi_j:\|a\|_2\leq R
\right\},
\]

we show that uniform transfer from finite approximating forms to an infinite form reduces to Gram-matrix convergence. We then decompose the Gram-entry error into truncation, projection, kernel/model, and computational components:

\[
G^{(N)}_{ij}-G^{(\infty)}_{ij}
=
T_{ij}^{(N)}
+
P_{ij}^{(N)}
+
K_{ij}^{(N)}
+
C_{ij}^{(N)}.
\]

If these four components have explicit bounds, then the finite-to-infinite transfer error is bounded by

\[
R^2m
\left(
\tau_N^{(m)}
+
\pi_N^{(m)}
+
\kappa_N^{(m)}
+
\chi_N^{(m)}
\right).
\]

We also include a certified numerical model for the computational term \(C_{ij}^{(N)}\), based on interval enclosures. The result is conditional: it does not import the true Weil/Bombieri form, does not prove unconditional convergence, and does not prove or advance the Riemann Hypothesis. Its intended use is as a reviewable framework for clarifying what would be required to make finite certified computations meaningful for infinite Weil/Bombieri positivity questions.

---

## 1. Motivation

Finite matrix computations can be misleading unless their relationship to the intended infinite mathematical object is controlled. In RH-adjacent Weil/Bombieri-style settings, a finite matrix may exhibit positivity, negativity, or stable eigenvalue counts, but such finite behavior is meaningful only if it transfers to a genuine infinite form.

This note asks a narrower question:

Given a finite test class, what error bounds are sufficient to transfer finite Gram-matrix information to an infinite quadratic form?

The answer is conditional but explicit.

---

## 2. Finite test class

Let

\[
\Phi_m=\{\phi_1,\ldots,\phi_m\}
\]

be a finite family of admissible test functions.

Define

\[
\mathcal F_R^{(m)}
=
\left\{
f=\sum_{j=1}^{m}a_j\phi_j:\|a\|_2\leq R
\right\}.
\]

The goal is to bound

\[
\sup_{f\in\mathcal F_R^{(m)}}
|Q_N^W(P_N^Wf)-Q_W(f)|.
\]

---

## 3. Infinite and finite Gram matrices

Let \(B_W\) be the Hermitian form associated to the infinite quadratic form \(Q_W\). Define

\[
G^{(\infty)}_{ij}=B_W(\phi_i,\phi_j).
\]

Let \(B_N^W\) be the finite Hermitian form associated to \(Q_N^W\), and let

\[
P_N^W:\mathcal D_W\to V_N^W
\]

be an approximation map. Define

\[
G^{(N)}_{ij}
=
B_N^W(P_N^W\phi_i,P_N^W\phi_j).
\]

For

\[
f=\sum_{j=1}^{m}a_j\phi_j,
\]

we have

\[
Q_W(f)=a^*G^{(\infty)}a
\]

and

\[
Q_N^W(P_N^Wf)=a^*G^{(N)}a.
\]

---

## 4. Gram convergence reduction

Let

\[
\Delta_N^{(m)}=G^{(N)}-G^{(\infty)}.
\]

Then

\[
|Q_N^W(P_N^Wf)-Q_W(f)|
=
|a^*\Delta_N^{(m)}a|.
\]

Using

\[
|a^*\Delta_N^{(m)}a|
\leq
\|\Delta_N^{(m)}\|_2\|a\|_2^2,
\]

and

\[
\|a\|_2\leq R,
\]

we obtain

\[
\sup_{f\in\mathcal F_R^{(m)}}
|Q_N^W(P_N^Wf)-Q_W(f)|
\leq
R^2\|G^{(N)}-G^{(\infty)}\|_2.
\]

If

\[
|G^{(N)}_{ij}-G^{(\infty)}_{ij}|
\leq
\delta_N^{(m)}
\]

for all \(i,j\), then

\[
\|G^{(N)}-G^{(\infty)}\|_2
\leq
m\delta_N^{(m)}.
\]

Thus

\[
\sup_{f\in\mathcal F_R^{(m)}}
|Q_N^W(P_N^Wf)-Q_W(f)|
\leq
R^2m\delta_N^{(m)}.
\]

---

## 5. Four-error decomposition

We decompose each Gram-entry error as

\[
G^{(N)}_{ij}-G^{(\infty)}_{ij}
=
T_{ij}^{(N)}
+
P_{ij}^{(N)}
+
K_{ij}^{(N)}
+
C_{ij}^{(N)}.
\]

The terms are:

\[
T_{ij}^{(N)}
\]

for truncation error,

\[
P_{ij}^{(N)}
\]

for projection error,

\[
K_{ij}^{(N)}
\]

for kernel/model mismatch, and

\[
C_{ij}^{(N)}
\]

for computational error.

---

## 6. Main conditional theorem

### Theorem

Assume that for all \(1\leq i,j\leq m\),

\[
|T_{ij}^{(N)}|\leq\tau_N^{(m)},
\]

\[
|P_{ij}^{(N)}|\leq\pi_N^{(m)},
\]

\[
|K_{ij}^{(N)}|\leq\kappa_N^{(m)},
\]

and

\[
|C_{ij}^{(N)}|\leq\chi_N^{(m)}.
\]

Then

\[
\sup_{f\in\mathcal F_R^{(m)}}
|Q_N^W(P_N^Wf)-Q_W(f)|
\leq
R^2m
\left(
\tau_N^{(m)}
+
\pi_N^{(m)}
+
\kappa_N^{(m)}
+
\chi_N^{(m)}
\right).
\]

### Proof

By the decomposition,

\[
G^{(N)}_{ij}-G^{(\infty)}_{ij}
=
T_{ij}^{(N)}
+
P_{ij}^{(N)}
+
K_{ij}^{(N)}
+
C_{ij}^{(N)}.
\]

Therefore, by the triangle inequality,

\[
|G^{(N)}_{ij}-G^{(\infty)}_{ij}|
\leq
|T_{ij}^{(N)}|
+
|P_{ij}^{(N)}|
+
|K_{ij}^{(N)}|
+
|C_{ij}^{(N)}|.
\]

Using the assumed bounds gives

\[
|G^{(N)}_{ij}-G^{(\infty)}_{ij}|
\leq
\tau_N^{(m)}
+
\pi_N^{(m)}
+
\kappa_N^{(m)}
+
\chi_N^{(m)}.
\]

Apply the entrywise Gram convergence reduction with

\[
\delta_N^{(m)}
=
\tau_N^{(m)}
+
\pi_N^{(m)}
+
\kappa_N^{(m)}
+
\chi_N^{(m)}.
\]

This gives the claimed result.

\[
\square
\]

---

## 7. Negative-direction transfer corollary

Suppose

\[
Q_W(f)\leq-\eta
\]

for some

\[
f\in\mathcal F_R^{(m)}
\]

and some

\[
\eta>0.
\]

If

\[
R^2m
\left(
\tau_N^{(m)}
+
\pi_N^{(m)}
+
\kappa_N^{(m)}
+
\chi_N^{(m)}
\right)
<
\eta/2,
\]

then

\[
Q_N^W(P_N^Wf)<-\eta/2.
\]

This follows directly from the main theorem and the triangle inequality.

---

## 8. Certified numerical component

The computational error term can be controlled conditionally by interval arithmetic.

Let

\[
G^{(N),exact}_{ij}
\]

be the exact finite Gram entry and

\[
\widetilde G^{(N)}_{ij}
\]

the computed entry.

If an interval

\[
[\ell_{ij}^{(N)},u_{ij}^{(N)}]
\]

certifies

\[
G^{(N),exact}_{ij}\in[\ell_{ij}^{(N)},u_{ij}^{(N)}],
\]

then the midpoint

\[
\widetilde G^{(N)}_{ij}
=
\frac{\ell_{ij}^{(N)}+u_{ij}^{(N)}}{2}
\]

satisfies

\[
|\widetilde G^{(N)}_{ij}-G^{(N),exact}_{ij}|
\leq
\frac{u_{ij}^{(N)}-\ell_{ij}^{(N)}}{2}.
\]

Define

\[
\chi_N^{(m)}
=
\max_{i,j}
\frac{u_{ij}^{(N)}-\ell_{ij}^{(N)}}{2}.
\]

Then

\[
|C_{ij}^{(N)}|\leq\chi_N^{(m)}.
\]

---

## 9. Certificate calculator

The project implements a certificate calculator that takes

\[
R,\quad m,\quad \tau,\quad \pi,\quad \kappa,\quad \chi,\quad \eta
\]

and computes

\[
\mathcal E_N^{(m)}
=
\tau+\pi+\kappa+\chi,
\]

\[
R^2m\mathcal E_N^{(m)}.
\]

If a margin \(\eta\) is provided, it checks

\[
R^2m\mathcal E_N^{(m)}<\eta/2.
\]

The calculator does not prove the supplied error bounds. It only combines them according to the theorem.

---

## 10. Limitations

This framework is conditional.

It does not yet provide:

1. the true imported Weil/Bombieri form \(Q_W\);
2. the true test-function space \(\mathcal D_W\);
3. the exact RH positivity theorem;
4. the exact classical projection maps \(P_N^W\);
5. unconditional truncation bounds;
6. unconditional projection bounds;
7. classical validation of the finite \(H\)-kernel;
8. kernel/model mismatch bounds;
9. novelty verification.

Therefore, it is not an RH proof, not an RH breakthrough, and not an established RH contribution.

---

## 11. Review purpose

The intended review questions are:

1. Are the conditional theorems correct?
2. Is the Gram reduction too standard to be useful?
3. Is the four-error decomposition mathematically natural?
4. Is the certified numerical component meaningful?
5. What classical Weil/Bombieri objects should replace the placeholders?
6. Is there a known framework that already contains this?
7. What should be cited?

