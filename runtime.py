from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager
from qiskit_aer import AerSimulator
from qiskit_ibm_runtime import QiskitRuntimeService


def initialize_runtime(
    noise_type_str,
    backend_type_str,
    ansatz,
    H_op,
    H_op_norm,
):
    seed = 42
    service = QiskitRuntimeService(channel="ibm_quantum_platform")
    backend_noise = service.backend(noise_type_str)
    if backend_type_str == "aer":
        print(f"Using AerSimulator with noise type: {noise_type_str}")
        backend_type = AerSimulator.from_backend(backend_noise, seed_simulator=seed)
    elif backend_type_str == "boston":
        print(f"WARNING: USING IBM ALLOCATION TYPE: {backend_type_str}...")
        backend_type = service.backend("ibm_boston")
    elif backend_type_str == "fez":
        print(f"WARNING: USING IBM ALLOCATION TYPE: {backend_type_str}")
        backend_type = service.backend("ibm_fez")
    elif backend_type_str == "marrakesh":
        print(f"WARNING: USING IBM ALLOCATION TYPE: {backend_type_str}")
        backend_type = service.backend("ibm_marrakesh")
    else:
        raise ValueError(f"Backend type '{backend_type_str}' is not supported.")

    backend_noise = AerSimulator.from_backend(backend_noise, seed_simulator=seed)

    pm = generate_preset_pass_manager(optimization_level=3, backend=backend_type)
    ansatz_opt = pm.run(ansatz)
    H_op_opt = H_op.apply_layout(ansatz_opt.layout)
    H_op_norm_opt = H_op_norm.apply_layout(layout=ansatz_opt.layout)

    return ansatz_opt, H_op_opt, H_op_norm_opt, backend_type, backend_noise


def turn_off_noise(backend):
    backend.set_options(noise_model=None)
    pass
