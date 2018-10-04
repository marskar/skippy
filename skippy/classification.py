from sklearn.metrics import confusion_matrix, accuracy_score
import skippy as skp


def classification(dataset: str = 'digits',
                   model_type: str = 'linear_model',
                   model_name: str = 'LogisticRegression') -> str:
    data = skp.get_data(dataset)
    x_train, x_test, y_train, y_test = skp.split_data(data)
    model = skp.get_model(model_type=model_type, model_name=model_name)
    fit = model.fit(x_train, y_train)
    skp.pickle_model(model=fit, filename=f'{dataset}_{model_name}.pickle')
    predictions = fit.predict(x_test)
    confmat = confusion_matrix(y_true=y_test, y_pred=predictions)
    accuracy = accuracy_score(y_true=y_test, y_pred=predictions)
    skp.confusion_matrix_plot(cm=confmat, acc=accuracy,
                              filename=f'{dataset}_{model_name}.png')
    return (f'The {model_name} was'
            f'{accuracy:.0%} in classifying'
            f'the {dataset} dataset.')
