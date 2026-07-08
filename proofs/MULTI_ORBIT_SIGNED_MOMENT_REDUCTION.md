# Multi-Orbit Li Resonance as a Signed-Moment Problem

## Phase 4E

This phase algebraically reduces the fully aligned finite-orbit fourth-order Li response to a signed weighted sum over blind-scale values.

The purpose is to distinguish trivial cancellation by continuous weight tuning from rigid equal-weight or integer-multiplicity cancellation.

---

# 1. Fully aligned resonant family

Let

\[
k_1,\ldots,k_J
\]

be blind-scale indices.

Fix the common coordinate

\[
c_{k_1}
\]

and choose relative heights

\[
a_j
=
\frac{
c_{k_1}
}{
c_{k_j}
}.
\]

Then

\[
\frac{
c_{k_1}
}{
a_j
}
=
c_{k_j},
\]

so every orbit is individually blind at leading order.

For positive weights

\[
w_1,\ldots,w_J,
\]

the fourth-order aggregate coefficient is

\[
K_{\mathrm{agg}}
=
\sum_{j=1}^J
w_j
\left(
\frac{
c_{k_j}
}{
c_{k_1}
}
\right)^4
K_{\mathrm{Li}}(c_{k_j}).
\]

---

# 2. Sign-explicit reduction

The validated blind-scale correction is

\[
K_{\mathrm{Li}}(c_k)
=
(-1)^{k+1}
\frac{
c_k^2\sqrt{c_k^2+4}
}{
6
}.
\]

Define

\[
F(x)
=
x^6\sqrt{x^2+4}
\]

and

\[
A_k
=
F(c_k).
\]

Then

\[
\boxed{
6c_{k_1}^4K_{\mathrm{agg}}
=
\sum_{j=1}^J
w_j
(-1)^{k_j+1}
A_{k_j}.
}
\]

Thus the fully aligned fourth-order resonance problem is exactly a signed weighted-moment problem for the positive sequence

\[
A_k.
\]

---

# 3. Parity decomposition

Define

\[
M_+
=
\sum_{\substack{j\\k_j\ {\rm odd}}}
w_jA_{k_j}
\]

and

\[
M_-
=
\sum_{\substack{j\\k_j\ {\rm even}}}
w_jA_{k_j}.
\]

Then

\[
\boxed{
K_{\mathrm{agg}}
=
\frac{
M_+-M_-
}{
6c_{k_1}^4
}.
}
\]

Exact fourth-order cancellation is equivalent to

\[
\boxed{
M_+=M_-.
}
\]

---

# 4. Same-parity obstruction

Assume

\[
w_j>0
\]

for every orbit.

If every blind-scale index \(k_j\) has the same parity, then every signed contribution has the same sign.

Therefore

\[
\boxed{
K_{\mathrm{agg}}\ne0.
}
\]

Hence every positive-weight fully aligned resonant family supported on a single blind-scale parity has exact aggregate response exponent \(4\).

---

# 5. Mixed-parity positive real weights

Suppose at least one \(k_j\) is odd and at least one \(k_j\) is even.

Then there exist strictly positive real weights satisfying

\[
M_+=M_-.
\]

Indeed, assign arbitrary positive weights to all terms on one parity side and sufficiently small positive weights to all but one term on the other side.

The remaining weight is uniquely chosen to balance the two positive weighted sums and is strictly positive.

Therefore

\[
\boxed{
\text{every mixed-parity resonant index family admits positive real weights with exact fourth-order cancellation.}
}
\]

Accordingly, cancellation found by unconstrained continuous weight optimization is not by itself a rigid arithmetic phenomenon.

---

# 6. Codimension-one cancellation set

For fixed indices define

\[
v_j
=
(-1)^{k_j+1}A_{k_j}.
\]

Then

\[
K_{\mathrm{agg}}=0
\]

if and only if

\[
\boxed{
\mathbf v\cdot\mathbf w=0.
}
\]

In full real weight space this is a hyperplane of codimension one.

Under the normalization

\[
w_j>0,
\qquad
\sum_jw_j=1,
\]

the positive weight vectors lie in the interior of a simplex of dimension

\[
J-1.
\]

For a mixed-parity family, the cancellation set is a nonempty affine slice of dimension

\[
J-2.
\]

Therefore exact cancellation has simplex Lebesgue measure zero and is non-generic under continuous weight perturbation.

---

# 7. Transverse weight instability

Let

\[
\mathbf w^\star
\]

be an exact cancelling weight vector.

Perturb

\[
\mathbf w
=
\mathbf w^\star
+
\varepsilon\mathbf u.
\]

Then

\[
\mathbf v\cdot\mathbf w
=
\varepsilon
\mathbf v\cdot\mathbf u.
\]

Hence

\[
\boxed{
K_{\mathrm{agg}}
=
\frac{
\varepsilon\mathbf v\cdot\mathbf u
}{
6c_{k_1}^4
}.
}
\]

For a perturbation direction transverse to the cancellation hyperplane,

\[
\mathbf v\cdot\mathbf u\ne0,
\]

the fourth-order coefficient reappears linearly in the weight perturbation.

---

# 8. Equal-weight reduction

For equal weights

\[
w_j=1,
\]

exact fourth-order cancellation becomes

\[
\boxed{
\sum_{j=1}^J
(-1)^{k_j+1}
A_{k_j}
=
0.
}
\]

This is a rigid signed-sum question for the blind-scale sequence

\[
A_k
=
c_k^6\sqrt{c_k^2+4}.
\]

Continuous weight tuning is no longer available.

---

# 9. Three equal-weight orbits

For three equal-weight orbits, all indices cannot have the same parity.

Let \(r\) denote the unique index on one parity side and let \(p,q\) denote the two indices on the opposite parity side.

Exact cancellation requires

\[
\boxed{
A_r=A_p+A_q.
}
\]

Since \(A_k\) is strictly increasing,

\[
A_r>A_p
\]

and

\[
A_r>A_q.
\]

Therefore

\[
\boxed{
r>\max(p,q).
}
\]

This is a necessary ordering condition for every equal-weight three-orbit exact cancellation.

---

# 10. Large-index balance shape

The blind scales satisfy

\[
c_k
=
\left(
k+\frac12
\right)\pi
+
O(k^{-1}).
\]

Also,

\[
A_k
=
c_k^6\sqrt{c_k^2+4}
\sim
c_k^7.
\]

Thus a hypothetical large-index three-orbit balance

\[
A_r=A_p+A_q
\]

must satisfy the asymptotic shape

\[
\boxed{
\left(
r+\frac12
\right)^7
\approx
\left(
p+\frac12
\right)^7
+
\left(
q+\frac12
\right)^7.
}
\]

This is only an asymptotic necessary shape.

It is not an exact Fermat equation.

Fermat's Last Theorem does not resolve the blind-scale balance problem.

---

# 11. Normalized equal-weight defect

For an equal-weight finite blind-scale index family

\[
\mathbf k
=
(k_1,\ldots,k_J),
\]

define

\[
\boxed{
D(\mathbf k)
=
\frac{
\left|
\sum_j
(-1)^{k_j+1}
A_{k_j}
\right|
}{
\sum_jA_{k_j}
}.
}
\]

Then

\[
0\le D(\mathbf k)\le1.
\]

Exact equal-weight fourth-order cancellation occurs if and only if

\[
D(\mathbf k)=0.
\]

For an admissibly ordered three-orbit candidate,

\[
\boxed{
D(p,q,r)
=
\frac{
|A_r-A_p-A_q|
}{
A_r+A_p+A_q
}.
}
\]

---

# 12. Research frontier

The continuous positive-weight cancellation problem is solved by linear algebra.

The rigid unresolved problems are:

1. equal-weight signed relations among blind-scale moments;
2. positive-integer multiplicity signed relations among blind-scale moments.

In particular, the first three-orbit question is:

\[
\boxed{
A_r
\stackrel{?}{=}
A_p+A_q
}
\]

under the required parity and ordering constraints.

No claim of existence or nonexistence is made in Phase 4E.

---

# 13. Interpretation boundary

All blind-scale heights remain synthetic finite-orbit parameters.

No relation to actual Riemann zeta zero-height multiplicities or ratios is established.

No infinite Li zero sum is controlled.

No RH implication is established.
