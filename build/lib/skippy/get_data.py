from importlib import import_module


def get_data(name: str):
    """load data from sklearn.datasets"""
    datasets = import_module('sklearn.datasets')
    load_dataset = getattr(datasets, 'load_'+name)
    dataset = load_dataset()
    return dataset
