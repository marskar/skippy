from skippy import classification

classification(dataset='wine',
               model_type='linear_model',
               model_name='LogisticRegression',
               pickle_name='wine_logistic_regression.pickle',
               plot_name='wine_logistic_regression.png')

classification(dataset='wine',
               model_type='ensemble',
               model_name='RandomForestClassifier',
               pickle_name='wine_random_forest.pickle',
               plot_name='wine_random_forest.png')

classification(dataset='wine',
               model_type='naive_bayes',
               model_name='GaussianNB',
               pickle_name='wine_naive_bayes.pickle',
               plot_name='wine_naive_bayes.png')

classification(dataset='wine',
               model_type='neighbors',
               model_name='KNeighborsClassifier',
               pickle_name='wine_knearest_neighbors.pickle',
               plot_name='wine_knearest_neighbors.png')
