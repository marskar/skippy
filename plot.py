from matplotlib import pyplot as plt
from evaluate import accuracy, confmat


def plot() -> None:
    fig, ax = plt.subplots()
    colorbar = ax.matshow(confmat())
    fig.colorbar(colorbar)
    fig.suptitle(f"Accuracy = {accuracy()}")
    fig.savefig('cm.png')

    # In addition to saving the plot, you can show it
    plt.show()