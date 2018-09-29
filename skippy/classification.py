import skippy as skp
from sklearn.metrics import confusion_matrix, accuracy_score


def classification(dataset: str,
                   model_type: str,
                   model_name: str,
                   pickle_name: str,
                   plot_name: str) -> None:

    data = skp.get_data(dataset)
    x_train, x_test, y_train, y_test = skp.split_data(data)
    logistic = skp.get_model(model_type=model_type, model_name=model_name)
    fit = logistic.fit(x_train, y_train)
    skp.pickle_model(filename=pickle_name, model=fit)
    predictions = fit.predict(x_test)
    confmat = confusion_matrix(y_test, predictions)
    accuracy = accuracy_score(y_test, predictions)
    skp.plot_cm(cm=confmat, acc=accuracy, filename=plot_name)
