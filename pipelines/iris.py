from skippy import get_data, split_data, get_model, pickle_model, plot_cm
from sklearn.metrics import confusion_matrix, accuracy_score

iris = get_data(name='iris')
x_train, x_test, y_train, y_test = split_data(iris)
logistic = get_model(model_type='linear_model', model_name='LogisticRegression')
fit = logistic.fit(x_train, y_train)
pickle_model(filename='iris_logistic.pickle', model=fit)
predictions = fit.predict(x_test)
accuracy = accuracy_score(y_test, predictions)
confmat = confusion_matrix(y_test, predictions)
plot_cm(cm=confmat, filename='iris_confusion_matrix.images', acc=accuracy)
