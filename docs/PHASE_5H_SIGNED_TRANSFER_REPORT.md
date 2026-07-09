# Phase 5H — Cancellation-Aware Signed Transfer Report

## Status

COMPLETE.

## Dataset

The experiment used the authoritative-anchor repaired first-500-critical-line-zero dataset.

Population:

- 18 dense complete windows;
- 20 frozen coordinates per window;
- 360 point-level decompositions;
- 60 decimal digits of working precision.

The empirical zero-counting discrepancy was integrated piecewise between consecutive zero ordinates with the staircase count frozen on each open interval.

No RH consequence is claimed.

---

# Exact signed decomposition

For

\[
f(t)=\chi_n^{Li}(t),
\qquad
B=(1+\eta)H,
\]

the empirical counting remainder was decomposed as

\[
R_{\mathrm{count}}
=
R_{\mathrm{atom}}
+
R_{\mathrm{end}}
+
R_{\mathrm{int}},
\]

where

\[
R_{\mathrm{atom}}
=
f(H)\Delta N_D(H),
\]

\[
R_{\mathrm{end}}
=
f(B)E_D(B)
-
f(H)E_D(H),
\]

and

\[
R_{\mathrm{int}}
=
-\int_H^B E_D(t)f'(t)dt.
\]

The interior normalized alignment coefficient was

\[
\kappa_{n,H,\eta}
=
\frac{
\int_H^B E_D(t)f'(t)dt
}{
\|E_D\|_2\|f'\|_2
}.
\]

The scalar cancellation coefficient was

\[
C_{\mathrm{scalar}}
=
\frac{
|R_{\mathrm{count}}|
}{
|R_{\mathrm{atom}}|
+
|R_{\mathrm{end}}|
+
|R_{\mathrm{int}}|
}.
\]

---

# Numerical validation

Maximum signed closure error:

\[
0.
\]

Maximum definitional identity error:

\[
3.7982270983\times10^{-65}.
\]

Maximum reconstruction error against the frozen Phase 5G non-atomic response:

\[
6.0771633573\times10^{-62}.
\]

P-SGN-001:

PASS.

Interpretation:

The Phase 5H signed decomposition is numerically consistent with the repaired Phase 5E/5G machinery at the stated working precision.

This is an implementation validation.

---

# Interior alignment result

Observed range:

\[
-0.0446977491
\le
\kappa
\le
0.0443057829.
\]

Median absolute alignment:

\[
\operatorname{median}|\kappa|
\approx
0.0072296622.
\]

Mean absolute alignment:

\[
\operatorname{mean}|\kappa|
\approx
0.0106294579.
\]

Fraction satisfying

\[
|\kappa|<0.05:
\]

\[
1.0.
\]

Fraction satisfying

\[
|\kappa|>0.25:
\]

\[
0.
\]

P-SGN-002:

FAIL.

The frozen prediction required

\[
\operatorname{median}|\kappa|>0.05.
\]

Interpretation:

Strong interior \(L^2\) alignment between the empirical counting discrepancy and the Li susceptibility derivative was not observed.

Across the tested finite population, the normalized inner products were uniformly small.

This is a finite computational observation.

It is not a theorem of asymptotic orthogonality, statistical independence, or randomness.

---

# Alignment-magnitude descriptive comparison

Baseline absolute interior scale:

\[
P_{\mathrm{abs}}
=
\|E_D\|_2\|f'\|_2.
\]

Observed log-correlation with count-residual magnitude:

\[
0.8374593007.
\]

Alignment-augmented magnitude:

\[
P_\kappa
=
|\kappa|
\|E_D\|_2\|f'\|_2
+
|R_{\mathrm{atom}}|
+
|R_{\mathrm{end}}|.
\]

Observed log-correlation:

\[
0.8414444250.
\]

Improvement:

\[
0.0039851242.
\]

P-SGN-003:

PASS under the frozen strict-greater-than rule.

Qualification:

The improvement is marginal.

The result must not be described as strong evidence that kappa explains or predicts the full counting remainder.

All quantities are in-sample and use the same empirical discrepancy windows.

---

# Scalar cancellation result

Median scalar cancellation coefficient:

\[
\operatorname{median}
C_{\mathrm{scalar}}
\approx
0.2397564067.
\]

Fraction satisfying

\[
C_{\mathrm{scalar}}<0.5:
\]

\[
0.7444444444.
\]

Fraction satisfying

\[
C_{\mathrm{scalar}}<0.25:
\]

\[
0.5138888889.
\]

P-SGN-004:

PASS strongly.

Interpretation:

Component-level signed cancellation among the atom, endpoint, and interior response channels is common and quantitatively material in the tested finite population.

This is a finite computational observation.

---

# Deterministic certificate tightness

Median sup-certificate tightness:

\[
\operatorname{median}T_{\sup}
\approx
0.0949334129.
\]

Observed correlation:

\[
\operatorname{corr}
(
\log T_{\sup},
\log C_{\mathrm{scalar}}
)
\approx
0.9187576394.
\]

Height-only comparison:

\[
\operatorname{corr}
(
\log T_{\sup},
\log(1/H)
)
\approx
0.2006528955.
\]

P-SGN-005:

PASS strongly.

Interpretation:

In the tested finite dataset, scalar cancellation was substantially more strongly associated with deterministic certificate tightness than inverse height alone.

This is an in-sample descriptive association.

It is not causal evidence or predictive generalization.

---

# Phase scorecard

\[
\begin{array}{ll}
\mathrm{P\mbox{-}SGN\mbox{-}001} & \mathrm{PASS},\\
\mathrm{P\mbox{-}SGN\mbox{-}002} & \mathrm{FAIL},\\
\mathrm{P\mbox{-}SGN\mbox{-}003} & \mathrm{PASS\ WITH\ WEAK\ EFFECT},\\
\mathrm{P\mbox{-}SGN\mbox{-}004} & \mathrm{PASS\ STRONGLY},\\
\mathrm{P\mbox{-}SGN\mbox{-}005} & \mathrm{PASS\ STRONGLY}.
\end{array}
\]

---

# Main conclusion

The initial strong-interior-alignment hypothesis was not supported.

The empirical geometry observed in Phase 5H is better summarized as:

\[
\text{small normalized interior alignment}
\]

together with

\[
\text{frequent and material scalar cancellation among signed response components}.
\]

The atom, endpoint, and interior response channels therefore require joint analysis.

The deterministic absolute-value envelope is often loose because it discards this component-level sign cancellation.

---

# Failure-prevention rules

1. The exact kappa reconstruction of the interior component is definitional.

2. The small observed kappa values do not prove asymptotic orthogonality.

3. P-SGN-003 showed only a marginal descriptive-correlation improvement.

4. The strong cancellation/tightness correlation is in-sample.

5. Correlation does not establish causation.

6. No RH consequence follows.

7. The results do not constrain off-critical zeros.

