from sklearn.linear_model import LogisticRegression
from split_data import split_data
import pickle


def logistic():

    model = LogisticRegression()
    model.fit(split_data()[0], split_data()[2])

    # Pickle the model using the highest protocol available.
    with open('model.pickle', 'wb') as f:
        pickle.dump(model, f, pickle.HIGHEST_PROTOCOL)

    return model