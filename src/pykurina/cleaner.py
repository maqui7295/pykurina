import pandas as pd
import polars as pl

from pykurina.actions import ColumnActions


class Cleaner:
    def __init__(
        self,
        dataframe: pl.DataFrame | pl.LazyFrame,
        rules: dict[str, ColumnActions],
        copy: bool = False,
        is_lazy: bool = True,
    ):
        self.rules = rules
        self.dataframe = dataframe

        if is_lazy and isinstance(dataframe, pl.DataFrame):
            self.dataframe = dataframe.lazy()
        elif not is_lazy and isinstance(dataframe, pl.DataFrame):
            print("Using DataFrame!\nSwitch to LazyFrame for better performance")

        if copy:
            self.dataframe = self.dataframe.clone()

    def __call__(self):
        actions = [rule(pl.col(k)) for k, rule in self.rules.items()]
        self.dataframe = self.dataframe.with_columns(*actions)
        return self.dataframe


class PDCleaner:
    def __init__(
        self,
        dataframe: pd.DataFrame,
        rules: dict[str, ColumnActions],
        copy: bool = True,
    ):
        self.rules = rules
        self.dataframe = dataframe
        if copy:
            self.dataframe = dataframe.copy()

    def __call__(self):
        if isinstance(self.dataframe, pd.DataFrame):
            for k, rule in self.rules.items():
                self.dataframe[k] = rule(self.dataframe[k])

        return self.dataframe
