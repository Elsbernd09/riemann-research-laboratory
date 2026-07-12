# Phase 10AW — Certified Numerics + Conditional Transfer Integration

## Purpose

Phase 10AT proved the conditional Gram-error transfer theorem:

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

Phase 10AU proved that interval arithmetic can certify

\[
|C_{ij}^{(N)}|\leq\chi_N^{(m)}.
\]

Phase 10AV implemented a prototype that computes \(\chi_N^{(m)}\).

Phase 10AW integrates these into one certified conditional transfer pipeline.

---

# 1. Inputs

The integrated pipeline requires:

1. \(R\): finite test-class radius;
2. \(m\): finite test-family size;
3. \(\tau_N^{(m)}\): truncation error bound;
4. \(\pi_N^{(m)}\): projection error bound;
5. \(\kappa_N^{(m)}\): kernel/model error bound;
6. \(\chi_N^{(m)}\): certified computational error bound.

The first three error terms remain classical or model-dependent.

The fourth is project-controllable through certified numerics.

---

# 2. Certified computational term

From interval arithmetic,

\[
\chi_N^{(m)}
=
\max_{i,j}r_{ij}^{(N)}.
\]

If all intervals enclose the exact finite Gram entries, then

\[
|C_{ij}^{(N)}|\leq \chi_N^{(m)}.
\]

This is the certified numerical component.

---

# 3. Integrated transfer bound

Define the total conditional error

\[
\mathcal E_N^{(m)}
=
\tau_N^{(m)}
+
\pi_N^{(m)}
+
\kappa_N^{(m)}
+
\chi_N^{(m)}.
\]

Then

\[
\sup_{f\in\mathcal F_R^{(m)}}
|Q_N^W(P_N^Wf)-Q_W(f)|
\leq
R^2m\mathcal E_N^{(m)}.
\]

---

# Theorem 10AW.1 — Certified numerics integrated transfer theorem

Assume:

1. the Gram error decomposes as

\[
G^{(N)}_{ij}-G^{(\infty)}_{ij}
=
T_{ij}^{(N)}
+
P_{ij}^{(N)}
+
K_{ij}^{(N)}
+
C_{ij}^{(N)};
\]

2. for all \(i,j\),

\[
|T_{ij}^{(N)}|\leq\tau_N^{(m)};
\]

3. for all \(i,j\),

\[
|P_{ij}^{(N)}|\leq\pi_N^{(m)};
\]

4. for all \(i,j\),

\[
|K_{ij}^{(N)}|\leq\kappa_N^{(m)};
\]

5. certified interval arithmetic gives

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

## Proof

By assumptions 2 through 5,

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

Apply the finite-class Gram convergence theorem.

\[
\square
\]

---

# Theorem 10AW.2 — Certified numerical negative-direction margin

Assume the hypotheses of Theorem 10AW.1.

Suppose

\[
Q_W(f)\leq-\eta
\]

for some

\[
f\in\mathcal F_R^{(m)}
\]

and \(\eta>0\).

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

## Proof

By Theorem 10AW.1,

\[
|Q_N^W(P_N^Wf)-Q_W(f)|
<
\eta/2.
\]

Since

\[
Q_W(f)\leq-\eta,
\]

we get

\[
Q_N^W(P_N^Wf)<-\eta/2.
\]

\[
\square
\]

---

# 4. Computable certificate format

A full integrated certificate should record:

1. \(R\);
2. \(m\);
3. \(\tau_N^{(m)}\);
4. \(\pi_N^{(m)}\);
5. \(\kappa_N^{(m)}\);
6. \(\chi_N^{(m)}\);
7. total error \(\mathcal E_N^{(m)}\);
8. transfer bound \(R^2m\mathcal E_N^{(m)}\);
9. optional negativity margin \(\eta\);
10. verdict: `TRANSFER_CERTIFIED` or `TRANSFER_NOT_CERTIFIED`.

---

# 5. Current meaning

This phase creates a theorem-backed integration layer.

It is still conditional because \(\tau_N^{(m)}\), \(\pi_N^{(m)}\), and \(\kappa_N^{(m)}\) are not yet proven for the classical Weil/Bombieri setting.

But the numerical term \(\chi_N^{(m)}\) is now integrated into the transfer theorem.

---

# 6. Next target

Phase 10AX should implement an integrated transfer-certificate calculator.

It should take:

\[
R,\ m,\ \tau,\ \pi,\ \kappa,\ \chi,\ \eta
\]

and output:

1. total error;
2. finite-class transfer bound;
3. certified status;
4. negative-direction transfer status.

---

# Boundary

This phase does not prove RH.

This phase does not falsify RH.

This phase does not prove a new RH criterion.

This phase does not prove unconditional classical convergence.

This phase does not import the true Weil form.

This phase does not claim novelty.

Exact audit strings:

CERTIFIED_NUMERICS_TRANSFER_INTEGRATION

INTEGRATED_TRANSFER_BOUND

CERTIFIED_NUMERICAL_NEGATIVE_DIRECTION_MARGIN

CHI_N_M_INTEGRATED

TRANSFER_CERTIFICATE_FORMAT

UNCONDITIONAL_CLASSICAL_CONVERGENCE_NOT_PROVEN

NOT_RH_CONTRIBUTION_YET

