# Phase 4D Two-Orbit Resonance Validation Report

## Objective

Validate the finite two-orbit Li blind-scale aggregation theory and resolve whether opposite-parity resonances admit exact fourth-order cancellation.

---

# 1. Closed blind-scale correction formula

At a Li response blind scale,

\[
\tan c_k=-c_k/2.
\]

Therefore

\[
\cos c_k
=
(-1)^{k+1}
\frac{2}{\sqrt{c_k^2+4}}.
\]

The blind-scale fourth-order correction simplifies to

\[
\boxed{
K_{\mathrm{Li}}(c_k)
=
(-1)^{k+1}
\frac{
c_k^2\sqrt{c_k^2+4}
}{
6
}.
}
\]

Independent symbolic and arbitrary-precision validation reproduced this identity.

Status:

VALIDATED.

---

# 2. No exact two-orbit fourth-order cancellation

Define

\[
F(x)
=
x^6\sqrt{x^2+4}.
\]

Then

\[
F'(x)
=
\frac{
x^5(7x^2+24)
}{
\sqrt{x^2+4}
}
>0
\]

for all \(x>0\).

The resonant fourth-order coefficient satisfies

\[
6c_k^4K_{k,m}^{(2)}
=
(-1)^{k+1}F(c_k)
+
(-1)^{m+1}F(c_m).
\]

For same-parity indices the terms have the same sign.

For opposite-parity indices, exact cancellation would require

\[
F(c_k)=F(c_m).
\]

Strict monotonicity implies \(c_k=c_m\), hence \(k=m\), contradicting opposite parity.

Therefore

\[
\boxed{
K_{k,m}^{(2)}\ne0
}
\]

for every pair \(k,m\ge0\).

Status:

PROVED IN PROJECT AND NUMERICALLY STRESS-TESTED.

---

# 3. Adversarial pair scan

The project scanned 40,000 ordered resonant pairs with blind-scale indices from 0 through 199.

Of these, 20,000 were opposite-parity ordered pairs.

No exact fourth-order cancellation occurred.

The smallest normalized cancellation ratio observed was approximately

\[
0.0175859577499984
\]

at the ordered pair

\[
(k,m)=(199,198).
\]

The scan used cached blind scales and correction coefficients.

The scan is implementation validation and adversarial evidence.

The mathematical noncancellation theorem is analytic and does not depend on the finite scan.

---

# 4. Relative near-cancellation

For opposite-parity resonant pairs define

\[
R_{k,m}
=
\frac{
|K_{k,m}^{(2)}|
}{
|K(c_k)|
+
(c_m/c_k)^4|K(c_m)|
}.
\]

For adjacent blind scales,

\[
\boxed{
R_{k,k+1}
\sim
\frac{7\pi}{2c_k}
\sim
\frac{7}{2(k+1/2)}.
}
\]

Therefore

\[
R_{k,k+1}\to0.
\]

Direct arbitrary-precision validation produced scaled ratios converging toward \(1\) in the asymptotic relation

\[
\frac{
R_{k,k+1}
}{
7\pi/(2c_k)
}
\to1.
\]

Thus arbitrarily strong relative fourth-order cancellation occurs along the adjacent resonance family.

Status:

VALIDATED.

---

# 5. Absolute coefficient behavior

The adjacent resonant coefficient satisfies

\[
\boxed{
|K_{k,k+1}^{(2)}|
\sim
\frac{7\pi}{6}c_k^2.
}
\]

Direct validation produced scaled values converging toward \(1\) in

\[
\frac{
|K_{k,k+1}^{(2)}|
}{
7\pi c_k^2/6
}
\to1.
\]

Therefore the absolute coefficient does not tend to zero.

It grows quadratically in the blind-scale coordinate.

The project must distinguish:

- relative cancellation strength;
- absolute aggregate response magnitude.

Status:

VALIDATED.

---

# 6. Nonresonant restoration

For two equal-weight orbits with relative heights

\[
1
\]

and

\[
a=2,
\]

the common coordinate \(c_0\) blinds the first orbit but not the second.

Numerical scaling reproduced

\[
\Gamma^2\mathcal X_n^{(2)}(\Gamma)
\to
\Psi_2^{(2)}(c_0).
\]

The validated numerical target was approximately

\[
-1.312845603305298279577184250788436221517.
\]

The scaled error decreased from approximately

\[
1.31\times10^{-5}
\]

to approximately

\[
5.22\times10^{-11}
\]

across the tested sequence.

Thus a nonresonant second orbit restores generic second-order aggregate response.

Status:

VALIDATED.

---

# 7. Resonant fourth-order survival

For

\[
a=c_0/c_1,
\]

with

\[
a
\approx
0.44995801752144606542353589290124850402613646120746,
\]

the two orbits are simultaneously blind at leading order under the common path

\[
n/\Gamma=c_0.
\]

Numerical scaling reproduced

\[
\Gamma^4\mathcal X_n^{(2)}(\Gamma)
\to
K_{0,1}^{(2)}.
\]

The validated target was approximately

\[
572.4588746065095864148524426130545849372.
\]

The scaled error decreased to approximately

\[
3.87\times10^{-8}
\]

across the tested sequence.

Thus finite aggregation can preserve fourth-order suppression under exact blind-scale ratio resonance.

Status:

VALIDATED.

---

# 8. Full test suite

The complete automated test suite was executed after the Phase 4D additions.

Result:

\[
\boxed{
107\text{ passed},\quad 0\text{ failed}.
}
\]

Status:

PASS.

---

# 9. Resolution of Phase 4C frontier

Question:

Do opposite-parity resonances admit exact or asymptotically arbitrarily strong fourth-order cancellation?

Answer:

Exact cancellation:

NO.

Arbitrarily strong normalized relative cancellation:

YES.

Absolute adjacent resonant coefficient tending to zero:

NO.

---

# 10. Interpretation boundary

The theorem concerns finite synthetic orbit families.

No arithmetic statement about actual zeta zero-height ratios has been established.

No infinite Li zero sum has been controlled.

No RH implication has been established.

---

# 11. Originality status

Unresolved.

No novelty claim is made from the absence of identified prior art.
