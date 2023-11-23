"""cleaner module

>>> import polars as pl
>>> from pykurina.actions import clean
>>> from pykurina.cleaner import Cleaner
>>> import pykurina.wrappers as cv
>>> df = pl.DataFrame({ "integers": [1, 2], "strings": ["2022-01-01", "2022-01-02"] })
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
    """Applies a list of actions to the specified columns"""

    def __init__(
        self,
        dataframe: pl.DataFrame | pl.LazyFrame,
        rules: dict[str, ColumnActions],
        copy: bool = False,
        make_lazy: bool = True,
    ):
        """
        Args:
          dataframe (pl.DataFrame): A polars dataframe
          rules (dict[str, ColumnActions]): A dictionary of columns and actions
          copy (bool): Copy the dictionary before cleaning. Defaults to False.
          make_lazy (bool): Convert the dataframe to a LazyFrame
        """
        self.rules = rules
        self.dataframe = dataframe

        if make_lazy and isinstance(dataframe, pl.DataFrame):
            self.dataframe = dataframe.lazy()
        elif not make_lazy and isinstance(dataframe, pl.DataFrame):
            print("Using DataFrame! Switch to LazyFrame for better performance")

        if copy:
            self.dataframe = self.dataframe.clone()

    def __call__(self):
        """Apply the actions to the columns"""
        actions = [rule(k) for k, rule in self.rules.items()]
        self.dataframe = self.dataframe.with_columns(*actions)
        return self.dataframe
