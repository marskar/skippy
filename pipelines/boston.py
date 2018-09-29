from skippy import regression

regression(dataset='boston',
           model_type='linear_model',
           model_name='Ridge',
           pickle_name='digits_Ridge_regression.pickle',
           plot_name='digits_logistic_regression.png')

regression(dataset='boston',
           model_type='ensemble',
           model_name='RandomForestClassifier',
           pickle_name='digits_random_forest.pickle',
           plot_name='digits_random_forest.png')

regression(dataset='boston',
           model_type='naive_bayes',
           model_name='GaussianNB',
           pickle_name='digits_naive_bayes.pickle',
           plot_name='digits_naive_bayes.png')

regression(dataset='boston',
           model_type='neighbors',
           model_name='KNeighborsClassifier',
           pickle_name='digits_knearest_neighbors.pickle',
           plot_name='digits_knearest_neighbors.png')
