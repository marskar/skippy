import skippy as skp

skp.classification(dataset='digits',
                   model_type='linear_model',
                   model_name='LogisticRegression',
                   pickle_name='digits_logistic_regression.pickle',
                   plot_name='digits_logistic_regression.png')

skp.classification(dataset='digits',
                   model_type='ensemble',
                   model_name='RandomForestClassifier',
                   pickle_name='digits_random_forest.pickle',
                   plot_name='digits_random_forest.png')

skp.classification(dataset='digits',
                   model_type='naive_bayes',
                   model_name='GaussianNB',
                   pickle_name='digits_naive_bayes.pickle',
                   plot_name='digits_naive_bayes.png')

skp.classification(dataset='digits',
                   model_type='neighbors',
                   model_name='KNeighborsClassifier',
                   pickle_name='digits_knearest_neighbors.pickle',
                   plot_name='digits_knearest_neighbors.png')
