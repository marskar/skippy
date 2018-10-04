import skippy as skp

skp.regression(dataset='boston',
           model_type='linear_model',
           model_name='Ridge')

skp.regression(dataset='boston',
           model_type='ensemble',
           model_name='RandomForestRegressor')

skp.regression(dataset='boston',
           model_type='linear_model',
           model_name='Lasso')
