from sklearn.linear_model import LogisticRegression
from split_data import split_data
import pickle

def logistic():

    x_train, x_test, y_train, y_test = split_data()

    model = LogisticRegression()
    model.fit(x_train, y_train)

    # Pickle the model using the highest protocol available.
    with open('model.pickle', 'wb') as f:
        pickle.dump(model, f, pickle.HIGHEST_PROTOCOL)

    return model
