from skippy import classification

classification(dataset='wine',
               model_type='linear_model',
               model_name='LogisticRegression')

classification(dataset='wine',
               model_type='ensemble',
               model_name='RandomForestClassifier')

classification(dataset='wine',
               model_type='naive_bayes',
               model_name='GaussianNB')

classification(dataset='wine',
               model_type='neighbors',
               model_name='KNeighborsClassifier')
