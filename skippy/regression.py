import skippy as skp
from sklearn.metrics import mean_squared_error, r2_score


def regression(dataset: str,
               model_type: str,
               model_name: str,
               pickle_name: str,
               plot_name: str) -> str:

    data = skp.get_data(dataset)
    x_train, x_test, y_train, y_test = skp.split_data(data)
    model = skp.get_model(model_type=model_type, model_name=model_name)
    fit = model.fit(x_train, y_train)
    if pickle_name is not None:
        skp.pickle_model(filename=pickle_name, model=fit)
    predictions = fit.predict(x_test)
    mse = mean_squared_error(y_true=y_test, y_pred=predictions)
    r2 = r2_score(y_true=y_test, y_pred=predictions)
    if plot_name is not None:
        skp.residual_plot(fitted=predictions,
                          target=y_test,
                          mse=mse, r2=r2,
                          filename=plot_name)
    return (f'The {model_name} explained'
            f'{r2:.0%} of the variance ($R^2$)'
            f'in the {dataset} dataset.')
