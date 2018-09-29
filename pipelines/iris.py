from skippy import classification

classification(dataset='iris',
               model_type='linear_model',
               model_name='LogisticRegression',
               pickle_name='iris_logistic_regression.pickle',
               plot_name='iris_logistic_regression.png')

classification(dataset='iris',
               model_type='ensemble',
               model_name='RandomForestClassifier',
               pickle_name='iris_random_forest.pickle',
               plot_name='iris_random_forest.png')

classification(dataset='iris',
               model_type='naive_bayes',
               model_name='GaussianNB',
               pickle_name='iris_naive_bayes.pickle',
               plot_name='iris_naive_bayes.png')

classification(dataset='iris',
               model_type='neighbors',
               model_name='KNeighborsClassifier',
               pickle_name='iris_knearest_neighbors.pickle',
               plot_name='iris_knearest_neighbors.png')
