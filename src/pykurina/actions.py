"""
Contains the action class that applies a series of cleaning functions to a column.
"""

import types
from typing import Any, Callable

import polars as pl

import pykurina.utils
import pykurina.wrappers


# https://stackoverflow.com/questions/972/adding-a-method-to-an-existing-object-instance-in-python
class ColumnActions:
    """Performs multiple cleaning actions on a column using chainable methods"""

    def __init__(self, wrappers: types.ModuleType):
        """Create a ColumnAction instance
        Args:
          wrappers (ModuleType): A module containing the wrapped function
        """
        self.functions: list[Callable] = []
        self.wrappers: types.ModuleType = wrappers

    def __call__(self, column: pl.Series):
        """Apply a list of functions to a polars column
        Args:
          column (pl.Series): A polars column
        Returns:
          pl.Series: A modified polars column
        """
        for f in self.functions:
            column = f(column)
        return column

    def __getattr__(self, __name: str) -> Any:
        """Dynamically call a function from the wrappers module
        Args:
          __name (str): The function to retrieve from self.wrappers
        Returns:
          ColumnActions: An instance of ColumnActions
        """

        def action(func, self):
            self.functions.append(func)

        f = pykurina.utils._configure_action_for_instance(__name, action)
        setattr(self, __name, types.MethodType(f, self))
        return super().__getattribute__(__name)


def clean() -> ColumnActions:
    """A factory function that creates an instance of ColumnActions"""
    return ColumnActions(pykurina.wrappers)
