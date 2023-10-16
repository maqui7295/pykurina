import pandas as pd

import pykurina.shared

# Casts


def to_int(column):
    return column.astype("int")


def to_string(column):
    return column.astype("str")


def to_datetime(column):
    return pd.to_datetime(column)


@pykurina.shared._returns_func
def remove(string):
    return pykurina.shared.replace(string, "", regex=False)


def trim(column):
    return column.str.strip()
