import pickle


def load_model():
    with open('model.pickle', 'rb') as f:
        return pickle.load(f)
