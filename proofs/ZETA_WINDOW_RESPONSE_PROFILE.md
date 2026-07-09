# Smooth-Density Zeta-Window Li Response Profile

## Phase 5A

This phase constructs a bridge from the individual Li zero-kernel quadratic susceptibility to finite windows of numerically computed Riemann zeta zero ordinates.

The continuum window profile is a smooth-density approximation.

It is not asserted as an exact identity for the discrete zeta zero sum.

---

# 1. Truncated zero-window susceptibility

For a finite set of numerically computed critical-line zero ordinates

\[
\gamma_j,
\]

define

\[
\mathcal W_n(H,\eta)
=
\sum_{\substack{\gamma_j\\
H\le\gamma_j\le(1+\eta)H}}
\chi_n^{\mathrm{Li}}(\gamma_j),
\]

where

\[
\eta>0.
\]

This is a finite discrete sum.

Using critical-line zero data in a verified finite range does not assume that every nontrivial zeta zero lies on the critical line.

---

# 2. Similarity-coordinate smearing

Suppose

\[
n/H\to c>0.
\]

For a zero ordinate

\[
\gamma=uH,
\qquad
1\le u\le1+\eta,
\]

one has

\[
n/\gamma\to c/u.
\]

Therefore a positive-width zero window samples the individual response profile over

\[
[c/(1+\eta),c].
\]

An individual blind scale

\[
\Psi_{\mathrm{Li}}(c_k)=0
\]

does not generally blind every zero contribution in the window.

---

# 3. Smooth zero-density approximation

Using the leading smooth zero-density model

\[
dN(t)
\approx
\frac{1}{2\pi}
\log\left(
\frac{t}{2\pi}
\right)dt,
\]

the discrete window susceptibility is heuristically modeled by

\[
\int_H^{(1+\eta)H}
t^{-2}
\Psi_{\mathrm{Li}}
\left(
\frac nt
\right)
\frac{1}{2\pi}
\log\left(
\frac{t}{2\pi}
\right)dt.
\]

Set

\[
n=cH
\]

and

\[
t=uH.
\]

At leading logarithmic scale,

\[
\boxed{
\frac H{\log H}
\mathcal W_n(H,\eta)
\approx
\Phi_\eta(c),
}
\]

where

\[
\boxed{
\Phi_\eta(c)
=
\frac{1}{2\pi}
\int_1^{1+\eta}
u^{-2}
\Psi_{\mathrm{Li}}
\left(
\frac cu
\right)du.
}
\]

This is a smooth-density continuum prediction.

---

# 4. Closed window-profile formula

The individual Li response profile is

\[
\Psi_{\mathrm{Li}}(v)
=
-2v(v\cos v+2\sin v).
\]

It satisfies

\[
\boxed{
\frac d{dv}
\left(
-2v^2\sin v
\right)
=
\Psi_{\mathrm{Li}}(v).
}
\]

Using

\[
v=c/u,
\]

one obtains

\[
\int_1^{1+\eta}
u^{-2}
\Psi_{\mathrm{Li}}
\left(
\frac cu
\right)du
=
\frac1c
\int_{c/(1+\eta)}^c
\Psi_{\mathrm{Li}}(v)dv.
\]

Therefore

\[
\boxed{
\Phi_\eta(c)
=
\frac{c}{\pi}
\left[
\frac{1}{(1+\eta)^2}
\sin\left(
\frac c{1+\eta}
\right)
-
\sin c
\right].
}
\]

---

# 5. Window-profile zeros

For

\[
c>0,
\]

the smooth-density window-profile zero equation is

\[
\boxed{
\sin c
=
\frac{1}{(1+\eta)^2}
\sin\left(
\frac c{1+\eta}
\right).
}
\]

This differs from the individual-kernel blind-scale equation

\[
\tan c=-c/2.
\]

Thus a positive-width window has a distinct predicted response-zero structure.

---

# 6. Narrow-window consistency

The integral representation implies

\[
\boxed{
\lim_{\eta\to0^+}
\frac{
\Phi_\eta(c)
}{
\eta
}
=
\frac{
\Psi_{\mathrm{Li}}(c)
}{
2\pi
}.
}
\]

Thus the individual susceptibility profile is recovered as the infinitesimal-width density of the smooth window profile.

---

# 7. Prediction boundary

The smooth-density profile does not include discrete zero fluctuations.

It does not prove convergence of the actual truncated zeta-zero window susceptibility.

It does not control off-critical zeros.

It does not prove RH.

The profile is a frozen prediction to be tested against reproducibly generated finite zero data.
