"""This module contains utitilities for creating a series of cleaning functions.

The :func:`clean` function instantiates a :class:`ColumnActions` class.
The instance created contains dynamically imports methods from the wrappers module.
The method calls are chainable since each call returns the ColumnActions instance.

Typical usage example::

    actions = {
        'column1': clean().trim().to_int(),
        'column2': clean().trim().replace('something', 'something_else'),
        'column3': clean().trim().remove('something')
    }

"""

import types
from typing import Any, Callable

import polars as pl

import pykurina.utils
import pykurina.wrappers


# https://stackoverflow.com/questions/972/adding-a-method-to-an-existing-object-instance-in-python
class ColumnActions:
    """Cleans a column using dynamically imported chainable methods."""

    def __init__(self, wrappers: types.ModuleType) -> None:
        """Create a ColumnAction instance.
        Args:
          wrappers (ModuleType): A module containing the wrapped function
        """
        self.functions: list[Callable] = []
        self.wrappers: types.ModuleType = wrappers

    def __call__(self, column: pl.Series) -> pl.Series:
        """Applies the list of functions to a polars column.
        Args:
          column (pl.Series): A polars column
        Returns:
          pl.Series: A modified polars column
        """
        for f in self.functions:
            column = f(column)
        return column

    def __getattr__(self, __name: str) -> Any:
        """Dynamically calls a function from the wrappers module.

        Args:
          __name (str): The function to retrieve from self.wrappers.

        Returns:
          An instance of ColumnActions.

        Raises:
          AttributeError:
            An error occurs if the function is missing from wrappers module.
        """

        def action(func, self):
            self.functions.append(func)

        f = pykurina.utils._configure_action_for_instance(__name, action)
        setattr(self, __name, types.MethodType(f, self))
        return super().__getattribute__(__name)


def clean() -> ColumnActions:
    """Creates an instance of ColumnActions."""
    return ColumnActions(pykurina.wrappers)
