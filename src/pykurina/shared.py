"""Contains common actions and helper functions"""
from typing import Callable


def _configure_action_for_instance(__name: str, action: Callable, wrappers=None):
    def inner(instance, *args, **kwargs):
        nonlocal wrappers

        if wrappers is None:
            wrappers = instance.wrappers
        try:
            func = getattr(wrappers, __name)
            if hasattr(func, wrappers.RETURNS_A_FUNCTION):
                func = func(*args, **kwargs)
            action(func, instance)
            return instance
        except AttributeError as e:
            raise AttributeError(
                f"In '{instance.__class__.__name__}' has no function called '{__name}'"
            ) from e

    inner.__name__ = __name

    return inner


# Common wrappers
RETURNS_A_FUNCTION = "returns_func"


def _returns_func(func):
    setattr(func, RETURNS_A_FUNCTION, True)
    return func


@_returns_func
def replace(*args, **kwargs):
    def f(column):
        return column.str.replace(*args, **kwargs)

    return f


def trim(column):
    return column.str.strip()
