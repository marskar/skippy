from sklearn.metrics import mean_squared_error, r2_score
import skippy as skp


def regression(dataset: str = 'boston',
               model_type: str = 'linear_model',
               model_name: str = 'LinearRegression'
               ) -> str:
    data = skp.get_data(dataset)
    x_train, x_test, y_train, y_test = skp.split_data(data)
    model = skp.get_model(model_type=model_type, model_name=model_name)
    fit = model.fit(x_train, y_train)
    skp.pickle_model(model=fit, filename=f'{dataset}_{model_name}.pickle')
    predictions = fit.predict(x_test)
    mse = mean_squared_error(y_true=y_test, y_pred=predictions)
    r2 = r2_score(y_true=y_test, y_pred=predictions)
    skp.residual_plot(fitted=predictions,
                      target=y_test,
                      mse=mse, r2=r2,
                      filename=f'{dataset}_{model_name}.png')
    return (f'The {model_name} explained'
            f'{r2:.0%} of the variance ($R^2$)'
            f'in the {dataset} dataset.')
