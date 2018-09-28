from sklearn.metrics import confusion_matrix, accuracy_score
from split_data import split_data
from predict import predict

def accuracy():
    """ get accuracy score """
    a = accuracy_score(split_data()[3], predict())
    return a

def confmat():
    """ get accuracy score """
    cm = confusion_matrix(split_data()[3], predict())
    return cm


