# Intro
This project solves the 2D Poisson equation on IBM quantum hardware using a VQLS. The goal of this repository is to provide reproducable and understandable code so that QC beginners can solve their own PDEs using Qiskit motions. 

# File Structure 
- **main.py** : Contains full VQLS loop in step by step process.
- **operators.py** : Functions for building laplacian operator
- 

# Status 
- Implements a periodic boundary condition with initialized zero driving term for simplicity.
- Local hamiltonian operator and cost function.
- Uses a hardware efficient ansatz.

