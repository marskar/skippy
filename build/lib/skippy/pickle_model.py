import pickle


def pickle_model(model, filename: str = 'model.pickle'):
    """Pickle a model using the highest protocol available."""
    with open(filename, 'wb') as f:
        pickle.dump(model, f, pickle.HIGHEST_PROTOCOL)
