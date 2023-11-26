"""This module contains the :class:`Cleaner` class which applies the cleaning actions.

Typical usage example:

>>> import polars as pl
>>> from pykurina.actions import clean
>>> from pykurina.cleaner import Cleaner
>>> import pykurina.wrappers as cv
>>> df = pl.LazyFrame({ "integers": [1, 2], "strings": ["2022-01-01", "2022-01-02"] })
>>> cleaner = Cleaner(df, {
... "integers": clean().to_string(),
... "strings": clean().to_date()
... })
>>> df2 = cleaner().collect()
>>> assert df2["integers"].dtype == pl.Utf8
>>> assert df2["strings"].dtype.is_temporal()
>>>
>>> df3 = df2.select(
... cv.to_int('integers'),
... cv.to_string('strings')
... )
>>> assert df.frame_equal(df3)

"""

import polars as pl

from pykurina.actions import ColumnActions


class Cleaner:
    """Applies a list of actions to the specified columns.

    This class runs cleaning actions on a polars dataframe. The return
    value is a copy of the cleaned dataframe in the form of a LazyFrame.
    While Cleaner expects a polars LazyFrame or DataFrame, the :attr:`make_lazy`
    attribute will convert a DataFrame to a LazyFrame to increase performance.

    Attributes:
      dataframe: A polars dataframe of type DataFrame or LazyFrame.
      actions: A dictionary of columns and actions.
      make_lazy:
        A boolean indicating whether to convert a DataFrame to a LazyFrame
    """

    def __init__(
        self,
        dataframe: pl.DataFrame | pl.LazyFrame,
        actions: dict[str, ColumnActions],
        make_lazy: bool = True,
    ):
        """
        Args:
          dataframe (pl.DataFrame | pl.LazyFrame): A polars dataframe.
          actions (dict[str, ColumnActions]): A dictionary of columns and actions.
          make_lazy (bool): Convert the dataframe to a LazyFrame.
        """
        self.actions = actions
        self.dataframe = dataframe

        if make_lazy and isinstance(dataframe, pl.DataFrame):
            self.dataframe = dataframe.lazy()
        elif not make_lazy and isinstance(dataframe, pl.DataFrame):
            print("Using DataFrame! Switch to LazyFrame for better performance")

    def __call__(self):
        """Applies the actions to the columns.

        Returns:
          A polars LazyFrame
        """
        actions = [rule(k) for k, rule in self.actions.items()]
        self.dataframe = self.dataframe.with_columns(*actions)
        return self.dataframe
