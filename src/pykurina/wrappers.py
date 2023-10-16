"""
This file contains functions or wrappers to cast a column from one data type
to another.

References:
    - https://pola-rs.github.io/polars/user-guide/expressions/casting/
"""

import polars as pl

import pykurina.shared

# from pykurina import __version__

__author__ = "maqui7295"
__copyright__ = "maqui7295"
__license__ = "MIT"


# Data Types Conversions
# Numbers
def to_int8(column: pl.Series):
    return column.cast(pl.Int8)


def to_int16(column: pl.Series):
    return column.cast(pl.Int16)


def to_int(column: pl.Series):
    return column.cast(pl.Int32)


def to_int64(column: pl.Series):
    return column.cast(pl.Int64)


def to_float(column: pl.Series):
    return column.cast(pl.Float64)


def to_float32(column: pl.Series):
    return column.cast(pl.Float32)


# Strings
def to_string(column: pl.Series):
    return column.cast(pl.Utf8)


# Dates and Times
def to_time(column: pl.Series):
    return column.str.to_time()


def to_date(column: pl.Series):
    return column.str.to_date()


def to_datetime(column: pl.Series):
    return column.str.to_datetime()


# Strings cleaning
@pykurina.shared._returns_func
def remove(string: str):
    return pykurina.shared.replace(string, "", literal=True)


def trim(column):
    return column.str.strip()
