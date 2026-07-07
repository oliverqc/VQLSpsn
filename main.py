import numpy as np
from ansatz import build_ansatz
from cost_function import cost_func
from graphing import plot_history
from operators import build_A, build_H_op
from optimization import optimize
from qiskit_ibm_runtime import EstimatorV2, Session
from runtime import initialize_runtime


def main():
    # WARNING: setting backend_type_str to boston/fez uses allocation

    N = 1
    depth = 2
    ansatz_type = "real_amplitudes"
    noise_type_str = "ibm_marrakesh"  # ibm_boston, ibm_fez, ibm_marrakesh
    backend_type_str = "marrakesh"  # aer, boston, fez, marrakesh

    A = build_A(N)

    H_op, H_op_norm = build_H_op(N, A)

    ansatz = build_ansatz(N, depth, ansatz_type)
    # ansatz_type1 = "efficient_su2"
    # ansatz1 = ansatz.build_ansatz(depth, ansatz_type1)

    ansatz_opt, H_op_opt, H_op_norm_opt, backend_type, backend_noise = (
        initialize_runtime(
            noise_type_str,
            backend_type_str,
            ansatz,
            H_op,
            H_op_norm,
        )
    )

    estimator = EstimatorV2(mode=backend_type)
    warm_estimator = EstimatorV2(mode=backend_noise)

    initial_theta = np.random.uniform(-np.pi, np.pi, ansatz_opt.num_parameters)
    method = "COBYLA"

    warm_history = []

    warm_bound_cost_func = lambda p: cost_func(
        p,
        ansatz_opt,
        H_op_opt,
        H_op_norm_opt,
        warm_estimator,
        warm_history,
    )

    print("Beginning warm start optimization...")
    warm_theta, warm_energy = optimize(warm_bound_cost_func, initial_theta, method, 35)
    print(f"Final warm energy: {warm_energy:.6f}")

    final_history = []

    with Session(backend=backend_type, max_time="20m") as session:
        estimator = EstimatorV2(mode=session)

        final_bound_cost_func = lambda p: cost_func(
            p,
            ansatz_opt,
            H_op_opt,
            H_op_norm_opt,
            estimator,
            final_history,
        )

        final_energy = optimize(final_bound_cost_func, warm_theta, method, 15)[1]
        print(f"Final energy: {final_energy:.6f}")

    plot_history(warm_history, final_history)


if __name__ == "__main__":
    main()
