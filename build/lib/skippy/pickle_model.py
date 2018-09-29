import pickle


def pickle_model(filename, model):
    """Pickle a model using the highest protocol available."""
    with open(filename, 'wb') as f:
        pickle.dump(model, f, pickle.HIGHEST_PROTOCOL)
