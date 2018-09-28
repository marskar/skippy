from sklearn.model_selection import train_test_split
from get_data import get_data
from typing import Tuple

def split_data(train_size: float = 0.8,
               test_size: float = 0.2,
               random_state: int = 0) -> Tuple:

    splits = train_test_split(
        get_data()[0], get_data()[1],
        train_size=train_size,
        test_size=test_size,
        random_state=random_state)

    return splits
