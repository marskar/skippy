import skippy as skp

skp.classification(dataset='iris',
                   model_type='linear_model',
                   model_name='LogisticRegression')

skp.classification(dataset='iris',
                   model_type='ensemble',
                   model_name='RandomForestClassifier')

skp.classification(dataset='iris',
                   model_type='naive_bayes',
                   model_name='GaussianNB')

skp.classification(dataset='iris',
                   model_type='neighbors',
                   model_name='KNeighborsClassifier')
