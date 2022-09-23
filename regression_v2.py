########################################################################################################################
# Imports
import numpy as np

from typing import Union


########################################################################################################################
# Variables

Numeric = Union[int, float]


########################################################################################################################
# Functions

def errors(pred, actual) -> np.array:
    return pred - actual


def mean_squared_error(pred, actual) -> Numeric:
    return np.mean(np.square(pred - actual))


def get_summary(pred, actual, print_results=True):
    # Error check
    if len(pred) != len(actual):
        raise ValueError(f'Predictions of length {len(pred)} does not match actual values of lenght {len(actual)}')

    # Get statistics
    mse = mean_squared_error(pred=pred, actual=actual)

    if print_results:
        print(f'Means squared error: {mse}')
