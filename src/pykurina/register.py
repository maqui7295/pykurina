import types
from typing import Any

import polars as pl

import pykurina.shared
import pykurina.wrappers


@pl.api.register_series_namespace("clean")
class ColumnActionShortcut:
    def __init__(self, s: pl.Series):
        self._s = s

    def square(self) -> pl.Series:
        self._s = self._s * self._s
        return self

    def __call__(self) -> pl.Series:
        return self.get()

    def get(self) -> pl.Series:
        return self._s

    def __getattr__(self, __name: str) -> Any:
        def act(action, self):
            self._s = action(self._s)

        f = pykurina.shared._configure_action_for_instance(
            __name, act, pykurina.wrappers
        )
        setattr(self, __name, types.MethodType(f, self))
        return super().__getattribute__(__name)
