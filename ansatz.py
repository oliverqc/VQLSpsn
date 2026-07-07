from qiskit.circuit.library import efficient_su2, real_amplitudes


def build_ansatz(N, depth, ansatz_type):
    if ansatz_type == "real_amplitudes":
        ansatz = real_amplitudes(
            2 * N,
            entanglement="linear",
            reps=depth,
            skip_final_rotation_layer=True,
        ).decompose()
    elif ansatz_type == "efficient_su2":
        ansatz = efficient_su2(
            2 * N,
            entanglement="linear",
            reps=depth,
            skip_final_rotation_layer=True,
        )
    else:
        raise ValueError(f"Ansatz type '{ansatz_type}' is not yet implemented.")

    return ansatz
