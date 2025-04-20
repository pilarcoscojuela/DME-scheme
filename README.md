# Structural Attack on DME− Signature Scheme

This repository implements a structural attack against the DME-minus digital signature scheme. The attack uses polynomial system solving and Gröbner basis techniques to recover secret keys. Because Magma V2.21-5 does not support exponents larger than 2^(30), this toy example works over the finite field F_q with q = 2^14.

## Main Files

- initial_setup.txt (Magma)
  Initializes cryptographic parameters, finite field F_q, polynomial rings, and matrices.

- compute_equations.txt (Magma)
  - Generates a public key from a fixed private key defined in initial_setup.txt.
  - Constructs the original system of equations (written to original_system.txt) following the framework introduced by Daniel Smith-Tone et al. Only four lists appear, corresponding to the known components of the public key in the DME-minus variant.
  - Instead of directly computing a Gröbner basis on the original system, the script generates an alternative equation system (written to result.txt) by introducing auxiliary variables (Rt, St, Kt, Lt, Zt, Wt, Xt, Yt, H).
  - The relations between auxiliary and original variables are written to linear_system.txt, drastically reducing the number of variables.
  - In this toy example, all equations in result_replaced.txt are solved at once; however, introducing H-variables simplifies Gröbner basis computations by removing collisions before recovering Rt, St, Kt, Lt, Zt, Wt.

- simplify.txt
  Simplifies exponent expressions (e.g., transforms Rt1^(2^3) * Xt1^(2^5) = T^5 into Rt1 * Xt1^(2^2) = (T^5)^(2^11)).

- replace.py
  Replaces large exponents with new variable names (e.g., Rt1^4096 -> Rt1b). Reads result.txt and writes result_replaced.txt.

- GB_solution.txt (Magma)
  Computes a Gröbner basis of systems in result_replaced.txt to recover secret variables (Rt, St, Kt, Lt, Zt, Wt, Xt, Yt, H).

- iterate_compute_equations.py
  Re-runs compute_equations.txt iteratively, appending each iteration’s linear system to linear_system.txt.

- Intermediate Outputs
  original_system.txt, result.txt, result_replaced.txt, linear_system.txt.

- last_round_recovery.txt (Magma)
  Recovers completely polynomials before the last exponential map.

## Usage
Run last_round_recovery.txt on Magma (version V2.21-5)

## Notes
Visit 
https://blogs.mat.ucm.es/dme/ for a precise definition of DME minus.




