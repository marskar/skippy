from typing import Tuple
from sklearn.model_selection import train_test_split


def split_data(dataset,
               train_size: float = 0.8,
               test_size: float = 0.2,
               random_state: int = 0) -> Tuple:

    splits = train_test_split(
        dataset['data'], dataset['target'],
        train_size=train_size,
        test_size=test_size,
        random_state=random_state)

    return splits
