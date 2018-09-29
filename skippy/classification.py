import skippy as skp
from sklearn.metrics import confusion_matrix, accuracy_score


def classification(dataset: str,
                   model_type: str,
                   model_name: str,
                   pickle_name: str = None,
                   plot_name: str = None) -> str:
    data = skp.get_data(dataset)
    x_train, x_test, y_train, y_test = skp.split_data(data)
    model = skp.get_model(model_type=model_type, model_name=model_name)
    fit = model.fit(x_train, y_train)
    if pickle_name is not None:
        skp.pickle_model(filename=pickle_name, model=fit)
    predictions = fit.predict(x_test)
    confmat = confusion_matrix(y_true=y_test, y_pred=predictions)
    accuracy = accuracy_score(y_true=y_test, y_pred=predictions)
    if plot_name is not None:
        skp.confusion_matrix_plot(cm=confmat, acc=accuracy, filename=plot_name)
    return (f'The {model_name} was'
            f'{accuracy:.0%} in classifying'
            f'the {dataset} dataset.')
