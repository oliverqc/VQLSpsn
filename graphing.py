import matplotlib.pyplot as plt


def plot_history(warm_history, final_history):

    total_history = warm_history + final_history

    plt.figure(figsize=(10, 6))
    plt.plot(
        range(1, len(total_history) + 1),
        total_history,
        marker="o",
        label="Cost Function Value",
    )
    plt.axvline(x=len(warm_history), color="r", linestyle="--", label="Warm Start End")
    plt.title("Cost Function Value Over Iterations")
    plt.xlabel("Iteration")
    plt.ylabel("Cost Function Value")
    plt.legend()
    plt.show()
