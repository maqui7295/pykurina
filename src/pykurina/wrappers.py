"""Wrappers around polars cleaning functions.

References:
    - https://pola-rs.github.io/polars/user-guide/expressions/casting/
"""

import polars as pl

import pykurina.utils

__author__ = "maqui7295"
__copyright__ = "maqui7295"
__license__ = "MIT"


# Data Types Conversions
# Numbers
def to_int8(column: pl.Series | str):
    return pl.col(column).cast(pl.Int8)


def to_int16(column: pl.Series | str):
    return pl.col(column).cast(pl.Int16)


def to_int(column: pl.Series | str):
    return pl.col(column).cast(pl.Int32)


def to_int32(column: pl.Series | str):
    return pl.col(column).cast(pl.Int32)


def to_int64(column: pl.Series | str):
    return pl.col(column).cast(pl.Int64)


def to_uint8(column: pl.Series | str):
    return pl.col(column).cast(pl.UInt8)


def to_uint16(column: pl.Series | str):
    return pl.col(column).cast(pl.UInt16)


def to_uint32(column: pl.Series | str):
    return pl.col(column).cast(pl.UInt32)


def to_uint64(column: pl.Series | str):
    return pl.col(column).cast(pl.UInt64)


def to_float(column: pl.Series | str):
    return pl.col(column).cast(pl.Float32)


def to_float32(column: pl.Series | str):
    return pl.col(column).cast(pl.Float32)


def to_float64(column: pl.Series | str):
    return pl.col(column).cast(pl.Float64)


# Strings
def to_string(column: pl.Series | str):
    return pl.col(column).cast(pl.Utf8)


@pykurina.utils.needs_currying
def date_to_string(column: pl.Series | str, format: str):
    return pl.col(column).dt.to_string(format)


# boolean
def to_bool(column: pl.Series | str):
    return pl.col(column).cast(pl.Boolean)


# Dates and Times
# Date to int works out of the box in polars
@pykurina.utils.needs_currying
def to_date(column: pl.Series | str, *args, **kwargs):
    return pl.col(column).str.to_date(*args, **kwargs)


@pykurina.utils.needs_currying
def to_datetime(column: pl.Series | str, *args, **kwargs):
    return pl.col(column).str.to_datetime(*args, **kwargs)


@pykurina.utils.needs_currying
def to_time(column: pl.Series | str, *args, **kwargs):
    return pl.col(column).str.to_time(*args, **kwargs)


def int_to_date(column: pl.Series | str):
    return pl.col(column).cast(pl.Date)


def int_to_datetime(column: pl.Series | str):
    return pl.col(column).cast(pl.Datetime)


def int_to_time(column: pl.Series | str):
    return pl.col(column).cast(pl.Time)


# Convert to null
def to_null(column: pl.Series | str):
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
