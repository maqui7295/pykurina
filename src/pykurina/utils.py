"""This modules contains utilities for working with the wrapper functions."""

from functools import wraps
from types import ModuleType
from typing import Callable

import polars as pl

TAKES_ADDITIONAL_ARGS = "TAKES_ADDITIONAL_ARGS"


def needs_currying(f: Callable) -> Callable:
    """Set an attribute on a function that might need currying.

    This is useful if the function takes a pl.Series and additional arguments.

    Args:
      f: A function.

    Returns:
      The function with a **TAKES_ADDITIONAL_ARGS** attribute.
    """
    setattr(f, TAKES_ADDITIONAL_ARGS, True)
    return f


# Problem: I wanted a free function
# I also pass the arguments to the function one at a time
# Solution: A curry decorator
def curry_decorator(f: Callable) -> Callable:
    """Curries a function.

    Args:
      f: A function to be curried.

    Returns:
      A decorator containing the curried function.
    """

    @wraps(f)
    def outer(*args, **kwargs):
        @wraps(f)
        def inner(column: pl.Series):
            return f(column, *args, **kwargs)

        return inner

    return outer


def _configure_action_for_instance(
    name: str, action: Callable, wrappers: ModuleType = None
):
    """Configures a function from :mod:`wrappers` module as an instance method.

    Args:
      name: The name of the module function.
      action: A function to enclose the module function.
      wrappers: A module (defaults to the wrappers module).

    Returns:
      A function.

    Raises:
      AttributeError:
        An error occurred while accessing the :mod:`pykurina.wrappers` module.
    """

    def inner(instance, *args, **kwargs):
        nonlocal wrappers

        if wrappers is None:
            wrappers = instance.wrappers
        try:
            func = getattr(wrappers, name)
            if hasattr(func, TAKES_ADDITIONAL_ARGS):
                func = curry_decorator(func)
                func = func(*args, **kwargs)
            action(func, instance)
            return instance
        except AttributeError as e:
            raise AttributeError(
                f"In '{instance.__class__.__name__}' has no function called '{name}'"
            ) from e

    inner.__name__ = name

    return inner
