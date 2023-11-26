"""Wrappers around polars cleaning functions.

Each function takes a polars Series or Expression as an argument
and returns a polars Expression. Some functions take additional arguments that
are forwared to the underlying polars method.

References:
  - Casting: https://pola-rs.github.io/polars/user-guide/expressions/casting/


"""

import polars as pl

import pykurina.utils

__author__ = "maqui7295"
__copyright__ = "maqui7295"
__license__ = "MIT"


# ============= Data Types Conversions ===================
def to_int8(column: pl.Series | str):
    """Convert to an 8-bit integer data type."""
    return pl.col(column).cast(pl.Int8)


def to_int16(column: pl.Series | str):
    """Convert to a 16-bit integer data type."""
    return pl.col(column).cast(pl.Int16)


def to_int(column: pl.Series | str):
    """An alias of to_int32()."""
    return pl.col(column).cast(pl.Int32)


def to_int32(column: pl.Series | str):
    """Convert to a 32-bit integer data type."""
    return pl.col(column).cast(pl.Int32)


def to_int64(column: pl.Series | str):
    """Convert to a 64-bit integer data type."""
    return pl.col(column).cast(pl.Int64)


def to_uint8(column: pl.Series | str):
    """Convert to an unsigned 8-bit integer data type."""
    return pl.col(column).cast(pl.UInt8)


def to_uint16(column: pl.Series | str):
    """Convert to an unsigned 16-bit integer data type."""
    return pl.col(column).cast(pl.UInt16)


def to_uint32(column: pl.Series | str):
    """Convert to an unsigned 32-bit integer data type."""
    return pl.col(column).cast(pl.UInt32)


def to_uint64(column: pl.Series | str):
    """Convert to an unsigned 64-bit integer data type."""
    return pl.col(column).cast(pl.UInt64)


def to_float(column: pl.Series | str):
    """An alias of to_float32()."""
    return pl.col(column).cast(pl.Float32)


def to_float32(column: pl.Series | str):
    """Convert to a 32-bit float data type."""
    return pl.col(column).cast(pl.Float32)


def to_float64(column: pl.Series | str):
    """Convert to a 64-bit float data type."""
    return pl.col(column).cast(pl.Float64)


def to_category(column: pl.Series | str):
    """Convert to a categorical data type."""
    return pl.col(column).cast(pl.Categorical)


def to_string(column: pl.Series | str):
    """Convert an integer or float to a string data type."""
    return pl.col(column).cast(pl.Utf8)


@pykurina.utils.needs_currying
def date_to_string(column: pl.Series | str, fmt: str):
    """Convert a date to a string data type."""
    return pl.col(column).dt.to_string(fmt)


def to_bool(column: pl.Series | str):
    """Convert to a boolean data type."""
    return pl.col(column).cast(pl.Boolean)


@pykurina.utils.needs_currying
def to_date(column: pl.Series | str, *args, **kwargs):
    """Convert a string to a date data type."""
    return pl.col(column).str.to_date(*args, **kwargs)


@pykurina.utils.needs_currying
def to_datetime(column: pl.Series | str, *args, **kwargs):
    """Convert to a string to a datetime data type."""
    return pl.col(column).str.to_datetime(*args, **kwargs)


@pykurina.utils.needs_currying
def to_time(column: pl.Series | str, *args, **kwargs):
    """Convert to a string to a time data type."""
    return pl.col(column).str.to_time(*args, **kwargs)


def int_to_date(column: pl.Series | str):
    """Convert an integer to a date data type."""
    return pl.col(column).cast(pl.Date)


def int_to_datetime(column: pl.Series | str):
    """Convert an integer to a datetime data type."""
    return pl.col(column).cast(pl.Datetime)


def int_to_time(column: pl.Series | str):
    """Convert an integer to a time data type."""
    return pl.col(column).cast(pl.Time)


def to_null(column: pl.Series | str):
    """Convert to a null data type."""
    return pl.col(column).cast(pl.Null)


# @needs_currying
# def replace(column: pl.Series, *args, **kwargs):
#     return column.str.replace(*args, **kwargs)


# def trim(column: pl.Series):
#     return column.str.strip()

# Strings cleaning
# @pykurina.shared._needs_currying
# def remove(string: str):
#     return pykurina.shared.replace(string, "", literal=True)
