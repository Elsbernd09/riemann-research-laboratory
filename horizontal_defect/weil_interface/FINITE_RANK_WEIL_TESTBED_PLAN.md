# Finite-Rank Weil Testbed Plan

## Purpose

Build a controlled computational and theoretical testbed for how off-critical zero quartets create negative directions in Weil-type quadratic forms.

This is not a new Weil criterion.

It is a laboratory for understanding detection.

---

# 1. Synthetic zero quartet

Use a synthetic quartet:

\[
\rho_1=\frac12+x+i\gamma,
\]

\[
\rho_2=\frac12-x+i\gamma,
\]

\[
\rho_3=\frac12+x-i\gamma,
\]

\[
\rho_4=\frac12-x-i\gamma.
\]

The parameter \(x\) measures horizontal displacement.

RH corresponds to

\[
x=0.
\]

---

# 2. Test-feature vector

Choose a finite set of test functions or basis features

\[
\varphi_1,\ldots,\varphi_m.
\]

Define the feature vector

\[
v(\rho)
=
(\varphi_1(\rho),\ldots,\varphi_m(\rho))^T.
\]

Then define a finite quadratic matrix model

\[
G
=
\sum_{\rho\in\Omega}
\sigma_\rho
v(\rho)v(\rho)^*,
\]

where \(\sigma_\rho\) records the sign structure appropriate to the model.

---

# 3. Detection problem

A negative direction exists if

\[
\lambda_{\min}(G)<0.
\]

The experiment asks:

1. Does \(\lambda_{\min}(G)\) become negative for \(x\ne0\)?
2. How does it scale with \(x\)?
3. How many basis functions are needed?
4. Does the signal persist under background critical-line zeros?
5. Does the construction resemble known Weil finite truncations?

---

# 4. Why this matters

Classical Weil positivity is already RH-equivalent.

The goal is not to rediscover the criterion.

The goal is to understand, in a finite controlled model, how horizontal displacement creates detectable negative directions.

---

# 5. Expected outcomes

Possible outcomes:

1. clean negative-direction detection;
2. detection only with enough basis functions;
3. severe conditioning problems;
4. cancellation under background zeros;
5. collapse into known Weil/Li theory.

Any of these outcomes is useful.

