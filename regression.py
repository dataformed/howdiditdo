########################################################################################################################
# Imports
import numpy as np

from typing import Union


########################################################################################################################
# Variables

Numeric = Union[int, float]


########################################################################################################################
# Functions

class Regression:

    def __init__(self, pred, actual):
        self.pred = np.array(pred)
        self.actual = np.array(actual)

    def get_errors(self):
        self.errors = self.pred - self.actual

    def mean_squared_error(self):
        if ~hasattr(self, 'errors'):
            self.get_errors()
        self.mse = np.mean(np.square(self.errors))

