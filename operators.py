import numpy as np
import scipy.sparse as sp
from qiskit.quantum_info import SparsePauliOp


def build_A(N):
    dim = 2**N
    h = 1 / dim

    diag = np.full(dim, -2.0)
    off_diag = np.full(dim - 1, 1.0)
    L_1d = sp.diags([diag, off_diag, off_diag], [0, -1, 1]).tolil()
    L_1d[0, -1] = 1.0
    L_1d[-1, 0] = 1.0
    L_1d = (1.0 / h**2) * L_1d

    pauli_1d = SparsePauliOp.from_operator(L_1d.toarray())

    pauli_list_2d = []
    I_string = "I" * N

    for pauli, coeff in zip(pauli_1d.paulis, pauli_1d.coeffs):
        p_str = str(pauli)
        # X-direction: L_1d (x) I_1d (Qiskit string order is reversed: I_string + p_str)
        pauli_list_2d.append((I_string + p_str, coeff))
        # Y-direction: I_1d (x) L_1d (Qiskit string order: p_str + I_string)
        pauli_list_2d.append((p_str + I_string, coeff))

    A_op = SparsePauliOp.from_list(pauli_list_2d)

    return A_op


def build_H_op(N, A):
    N_total = 2 * N
    local_strings = [("I" * N_total, 0.5)]

    for j in range(N_total):
        z_str = ["I"] * N_total
        z_str[j] = "Z"
        z_string_joined = "".join(z_str)
        local_strings.append((z_string_joined, -1.0 / (2 * N_total)))

    C_L_op = SparsePauliOp.from_list(local_strings)
    H_op_norm = A.adjoint().compose(A).simplify()
    H_op = A.adjoint().compose(C_L_op).compose(A).simplify()

    return H_op, H_op_norm
