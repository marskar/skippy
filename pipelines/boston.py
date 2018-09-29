import skippy as skp

skp.regression(dataset='boston',
           model_type='linear_model',
           model_name='Ridge',
           pickle_name='digits_ridge_regression.pickle',
           plot_name='digits_logistic_regression.png')

skp.regression(dataset='boston',
           model_type='ensemble',
           model_name='RandomForestRegressor',
           pickle_name='boston_random_forest.pickle',
           plot_name='boston_random_forest.png')

skp.regression(dataset='boston',
           model_type='linear_model',
           model_name='Lasso',
           pickle_name='boston_lasso_regression.pickle',
           plot_name='boston_lasso_regression.png')
