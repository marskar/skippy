from split_data import split_data
from model import logistic

def predict():
    """ get predictions """
    model = logistic()
    return model.predict(split_data()[1])
