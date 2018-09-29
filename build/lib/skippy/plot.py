import matplotlib.pyplot as plt
import seaborn as sns


def plot_cm(cm,
            acc=None,
            filename='confusion_matrix.png') -> None:
    sns.heatmap(cm, square=True, annot=True, cbar=False)

    plt.xlabel('Predicted Value')
    plt.ylabel('True Value')
    if acc is not None:
        plt.title(f'Accuracy = {acc:.0%}')
    plt.savefig(filename)

    # In addition to saving the plot, you can show it
    plt.show()
