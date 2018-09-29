from importlib import import_module


def get_model(model_type, model_name):

    models = import_module('sklearn.'+model_type)
    model = getattr(models, model_name)

    return model()