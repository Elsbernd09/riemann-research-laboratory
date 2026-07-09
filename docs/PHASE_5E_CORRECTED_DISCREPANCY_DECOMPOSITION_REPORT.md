# Phase 5E Corrected Zeta-Window Discrepancy Decomposition Report

## Objective

Independently evaluate the empirical zero-counting and Li-kernel truncation components of the finite actual-zero window-response discrepancy.

The initial Phase 5E execution failed because atomic window endpoints were reconstructed from rounded display serializations.

After the Phase 5E-R endpoint provenance repair, the complete decomposition experiment was rerun using authoritative zero-index anchors.

---

# 1. Corrected decomposition closure

The exact finite-dataset decomposition is

\[
\mathcal W_n-S_{\mathrm{profile}}
=
R_{\mathrm{count}}
+
R_{\mathrm{kernel}}.
\]

The counting remainder was independently evaluated by the Stieltjes expression using:

- authoritative atomic zero anchors;
- piecewise integration between zero ordinates;
- constant empirical count on each open interval;
- the independently validated exact susceptibility derivative.

The corrected maximum decomposition closure error was approximately

\[
\boxed{
6.19\times10^{-61}.
}
\]

The corrected maximum direct-versus-Stieltjes counting-remainder discrepancy was approximately

\[
\boxed{
6.19\times10^{-61}.
}
\]

Thus the independent numerical decomposition closes to the declared arbitrary-precision computation scale.

Status:

VALIDATED.

---

# 2. P-DEC-001

Prediction:

The independently evaluated numerical decomposition will close to arbitrary-precision quadrature tolerance.

Result:

\[
\boxed{
\text{PASS}
}
\]

The original failed execution is retained separately as an endpoint-provenance validation failure.

---

# 3. Counting versus kernel component dominance

The corrected experiment analyzed:

\[
18
\]

dense complete windows and

\[
10
\]

high-occupancy windows.

The dense-window count-dominance rate was

\[
\boxed{1.0}.
\]

The high-occupancy count-dominance rate was

\[
\boxed{1.0}.
\]

Thus every tested dense and high-occupancy window had counting-remainder RMS larger than kernel-remainder RMS.

For the high-occupancy subset, the mean normalized counting RMS was approximately

\[
0.06607224.
\]

The mean normalized kernel RMS was approximately

\[
2.12\times10^{-5}.
\]

The ratio of mean high-occupancy component sizes was

\[
\boxed{
3115.303893\ldots
}
\]

approximately.

Interpretation:

In the frozen first-500-zero experiment, the remaining profile discrepancy is overwhelmingly associated with empirical zero-counting fluctuation rather than the local Li-kernel asymptotic truncation term.

This is a finite computational result.

It is not a new asymptotic theorem for the classical zeta zero-counting remainder.

---

# 4. P-DEC-002

Prediction:

Counting-remainder RMS generally exceeds kernel-remainder RMS in dense and high-occupancy tested windows.

Result:

\[
\boxed{
\text{PASS}
}
\]

Evidence:

Count-dominance rate was 1.0 in both tested occupancy classes.

---

# 5. Finite-range height slopes

The corrected descriptive log-log height slopes were approximately

\[
\boxed{
-1.7339233393
}
\]

for normalized counting-remainder RMS and

\[
\boxed{
-1.8570110118
}
\]

for normalized kernel-remainder RMS.

The kernel component therefore exhibited the steeper finite-range decay trend.

However, the observed slopes do not numerically reproduce the candidate asymptotic exponents

\[
-1
\]

and

\[
-2.
\]

The accessible height interval is not treated as sufficient for asymptotic exponent identification.

---

# 6. P-DEC-003

Prediction:

The normalized kernel remainder will exhibit a steeper height-decay trend than the normalized counting remainder.

Result:

\[
\boxed{
\text{PASS WITH FINITE-RANGE QUALIFICATION}
}
\]

The kernel fitted slope was more negative than the counting fitted slope.

No claim is made that the fitted slopes establish asymptotic exponents.

---

# 7. Left-endpoint atom

For zero-anchored closed windows, the explicit left atom is

\[
R_{\mathrm{atom}}
=
\chi_n^{\mathrm{Li}}(H).
\]

The mean normalized high-occupancy atom RMS was approximately

\[
\boxed{
0.01248.
}
\]

The mean high-occupancy ratio

\[
\frac{
\mathrm{RMS}(\text{left-open profile residual})
}{
\mathrm{RMS}(\text{left-closed profile residual})
}
\]

was

\[
\boxed{
2.4349109619\ldots
}
\]

approximately.

Thus removing the left endpoint atom increased, rather than decreased, the residual RMS.

The atom does not explain the full counting-remainder magnitude.

However, its signed contribution materially participates in cancellation within the closed-window discrepancy.

---

# 8. P-DEC-004

Prediction:

Removing the explicit left-endpoint atom will improve smooth-model agreement slightly but will not explain most of the remaining residual.

Result:

\[
\boxed{
\text{FAIL}
}
\]

Observed behavior:

Removing the atom worsened high-occupancy residual RMS by a factor of approximately

\[
2.43.
\]

Disposition:

The project withdraws the assumption that the zero-anchor atom is merely an additive boundary artifact degrading smooth-profile agreement.

---

# 9. Corrected prediction scorecard

P-DEC-001:

PASS.

P-DEC-002:

PASS.

P-DEC-003:

PASS WITH FINITE-RANGE QUALIFICATION.

P-DEC-004:

FAIL.

Qualitative score:

\[
3/4.
\]

The failed prediction remains recorded.

---

# 10. Main analytic hierarchy supported by the experiment

The project currently observes the following response hierarchy:

\[
\text{individual Li susceptibility}
\longrightarrow
\text{smooth-density window profile}
\longrightarrow
\text{empirical counting fluctuation}.
\]

The smooth Li-kernel truncation component is extremely small relative to the empirical counting-remainder component in the tested dense windows.

Thus the principal residual after the finite-height smooth-density correction is associated with discrete zero-counting structure in the finite data.

---

# 11. Interpretation boundary

The counting remainder is defined using the frozen finite empirical counting function

\[
N_D.
\]

The experiment does not prove a new bound for the classical Riemann-von Mangoldt remainder.

The fitted height slopes are descriptive finite-range regressions.

No discrete convergence theorem is proved.

No new RH criterion, zero-free region, or Li positivity theorem follows.

No claim of progress toward proving RH is made.
