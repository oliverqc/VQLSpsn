import time

from scipy.optimize import minimize


def optimize(cost_func, initial_theta, method_str, iterations):
    print(f"Beginning optimization with method: {method_str}")

    start = time.perf_counter()
    res = minimize(
        cost_func,
        initial_theta,
        method=method_str,
        options={"maxiter": iterations},
    )
    end = time.perf_counter()

    print(f"Training done in {end - start:.2f}")
    print(f"Final training energy: {res.fun}")

    theta = res.x
    cost = res.fun

    return theta, cost
