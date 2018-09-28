from get_data import get_data
from sklearn.model_selection import train_test_split
from typing import Tuple

def split_data(train_size: float = 0.8,
               test_size: float = 0.2,
               random_state: int = 0) -> Tuple:

    data, target = get_data()

    splits = train_test_split(
        data, target,
        train_size=train_size,
        test_size=test_size,
        random_state=random_state)

    return splits
