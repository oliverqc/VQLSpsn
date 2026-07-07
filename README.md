# Intro
This project solves the 2D Poisson equation on IBM quantum hardware using a variational quantum linear solver (VQLS). The goal of this repository is to provide reproducable and understandable code so that quantum computing beginners can solve their own PDEs using qiskit motions. This project contains work I completed in both my personal research in the Civil Eng department at MST and the QIC 2026 summer internship at Mizzou.

# Learning
Learn the basics behind how the quantum computing community approaches solivng a linear system of equations on quantum hardware **solvinglinearsystems.md**. I discuss how a VQLS is built on a basic level and why I chose the VQLS amidst the many other quantum algorithm choices in **buildingvqls.md**. Finally, I mention what I believe to be the most promising approaches for the future of solving PDEs on quantum hardware.

# File Structure 
- **main.py** : Contains full VQLS loop and imports functions from all other files. 
- **operators.py** : Defines functions for building laplacian operator.
- **ansatz.py** : Creates hardware efficient ansatz circuit. 
- **runtime.py** : Contains qiskit motions for executing on quantum hardware or simulation with the quantum hardware's noise. 
- **cost_function.py** : Defines cost function.
- **optimization.py** : Defines optimizer.
- **graphing.py** : Plots cost function history.

# Status 
- Implements a periodic boundary condition with initialized zero driving term for simplicity.
- Local hamiltonian operator and cost function.
- Uses a hardware efficient ansatz.
- Displays cost history from warm start (if applied) and quantum hardware.

# How to install and run
This project uses python and qiskit. Because the code initializes QiskitRuntimeService using IBM quantum platform you must have an IBM quantum account with an instance. You can install the required dependencies via requirements.txt. To run install the whole VQLSpsn folder and then run main.py. 

### Settings
You can change the number of qubits, anstaz depth and type, and backend types at the top of main.py. The settings are commented in `main.py`. 

I recommend keeping the `N = 1 or 2` for real hardware runs. `For N = 1` (2 qubits total) and `depth = 2` with only 15 iterations on real hardware took 20 minutes of allocation. So be considerate of what settings you are choosing and how much allocation you have. To change the ansatz type replace `ansatz_type` with the corresponding string from `ansatz.py`. The runtime setting `noise_type_string` refers to the quantum processing unit (QPU) choice for the **AerSimulator** defined in `runtime.py`. Instead, a QPU can be selected by `backend_type_str`. There is also a optimizer variable `optimizer_method` with settings for common scipy optimizers. 

At the time of writing this I have prepared the code for a QPU and included a warm start in `main.py` however you can easily remove the extra loop and plug `initial_theta` into the final loop. 

# License
This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).
