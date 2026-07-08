# Cross-Diagnostic Susceptibility Scaling Taxonomy

## Phase 2A

The project now has two parameterized RH-related individual zero kernels.

---

# Li kernel

\[
f_n^{\mathrm{Li}}(z)
=
1-
\left(
1-\frac1z
\right)^n.
\]

Phase coordinate:

\[
\Phi_{\mathrm{Li}}(n,\gamma)
=
\frac n\gamma.
\]

Phase-preserving scaling:

\[
\frac n\gamma\to c.
\]

Height exponent:

\[
\alpha_{\mathrm{Li}}=2.
\]

Profile:

\[
\Psi_{\mathrm{Li}}(c)
=
-2c(c\cos c+2\sin c).
\]

---

# Explicit-formula zero kernel

\[
p_L(z)
=
-\frac{e^{Lz}}{z}.
\]

Native critical-line amplitude:

\[
e^{L/2}.
\]

Amplitude-normalized susceptibility:

\[
\widetilde\chi_L^{\mathrm{EF}}
=
e^{-L/2}
\chi_L^{\mathrm{EF}}.
\]

Phase coordinate:

\[
\Phi_{\mathrm{EF}}(L,\gamma)
=
L\gamma.
\]

Phase-preserving scaling:

\[
L\gamma\to c.
\]

Candidate height exponent:

\[
\alpha_{\mathrm{EF}}=3.
\]

Candidate profile:

\[
\Psi_{\mathrm{EF}}(c)
=
-4c\cos c+2(2-c^2)\sin c.
\]

---

# Candidate taxonomy

For a parameterized kernel family

\[
f_a(z),
\]

the project will investigate whether its quarter-turn susceptibility admits a scaling description of the form

\[
\gamma^\alpha
N(a,\gamma)
\chi_a(\gamma)
\to
\Psi(c)
\]

under a phase-preserving condition

\[
\Phi(a,\gamma)\to c.
\]

Here:

- \(\Phi\) is the asymptotic phase coordinate;
- \(N\) is a mathematically justified kernel-native normalization;
- \(\alpha\) is the height-decay exponent;
- \(\Psi\) is the limiting susceptibility profile.

A provisional family signature is

\[
\boxed{
(\Phi,\alpha,\Psi).
}
\]

This is project methodology.

No claim is made that this taxonomy is known to be novel or useful to experts.

---

# Current cross-diagnostic observation

The generic quarter-turn derivative filter is shared by both kernel families.

The phase-preserving parameter scaling is not shared:

\[
n\asymp\gamma
\]

for the Li kernel, while

\[
L\asymp\gamma^{-1}
\]

for the explicit-formula kernel.

The candidate height exponents also differ:

\[
2
\]

versus

\[
3
\]

after the explicit-formula kernel's native amplitude is removed.

The project must determine whether this distinction is merely elementary asymptotic bookkeeping or the beginning of a useful classification of zero diagnostics.
