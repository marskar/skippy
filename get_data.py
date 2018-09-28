from sklearn.datasets import load_digits
from typing import Tuple


def get_data() -> Tuple:
    # load data
    digits = load_digits()

    column_names = list(digits.keys())

    data = digits[column_names[0]]

    target = digits[column_names[1]]

    return data, target
