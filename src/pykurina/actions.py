import types
from typing import Any

import pykurina.pdwrappers
import pykurina.shared
import pykurina.wrappers

# https://stackoverflow.com/questions/972/adding-a-method-to-an-existing-object-instance-in-python


class ColumnActions:
    def __init__(self, wrappers):
        self.functions = []
        self.wrappers = wrappers

    def __call__(self, column=""):
        for f in self.functions:
            column = f(column)
        return column

    def __getattr__(self, __name: str) -> Any:
        def act(action, self):
            self.functions.append(action)

        f = pykurina.shared._configure_action_for_instance(__name, act)
        setattr(self, __name, types.MethodType(f, self))
        return super().__getattribute__(__name)


def clean():
    return ColumnActions(pykurina.wrappers)


def clean_pd():
    return ColumnActions(pykurina.pdwrappers)
