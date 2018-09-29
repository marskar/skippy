import matplotlib.pyplot as plt
import seaborn as sns


def confusion_matrix_plot(cm,
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


def residual_plot(fitted, target,
                  mse=None, r2=None,
                  filename='residual_plot.png') -> None:
    sns.residplot(fitted, target, lowess=True, line_kws={'color': 'red'})
    plt.xlabel('Fitted Values')
    plt.ylabel('Residuals')
    if mse is not None and r2 is not None:
        plt.title(f'MSE = {mse:.0f} and $R^2$ = {r2:.0%}')
    plt.savefig(filename)
    # In addition to saving the plot, you can show it
    plt.show()
