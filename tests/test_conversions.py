# import os
# import pytest
from datetime import date, datetime

import polars as pl

import pykurina.wrappers as cv
from pykurina.actions import clean
from pykurina.cleaner import Cleaner

__author__ = "maqui7295"
__copyright__ = "maqui7295"
__license__ = "MIT"


def conv_data():
    df = pl.DataFrame(
        {
            "integers": [1, 2, 3, 4, 5],
            "big_integers": [1, 10000002, 3, 10000004, 10000005],
            "floats": [4.0, 5.0, 6.0, 7.0, 8.0],
            "floats_with_decimal": [4.532, 5.5, 6.5, 7.5, 8.5],
            "date": pl.date_range(date(2022, 1, 1), date(2022, 1, 5), eager=True),
            "datetime": pl.datetime_range(
                datetime(2022, 1, 1), datetime(2022, 1, 5), eager=True
            ),
            "string": [
                "2022-01-01",
                "2022-01-02",
                "2022-01-03",
                "2022-01-04",
                "2022-01-05",
            ],
            "time_string": [
                "13:50:00",
                "13:50:00",
                "00:00:00",
                "19:30:00",
                "00:50:21",
            ],
        }
    )

    return df


def test_ints_and_floats_conversions():
    """Convert to integers and floats"""

    data = conv_data()

    out1 = (
        Cleaner(
            data,
            {
                "integers": clean().to_float32(),
                "floats": clean().to_int(),
                "floats_with_decimal": clean().to_int32(),
                "date": clean().to_int64(),
                "datetime": clean().to_int64(),
            },
        )
    )().collect()

    out2 = data.select(
        cv.to_float32("integers"),
        cv.to_int("floats"),
        cv.to_int32("floats_with_decimal"),
        cv.to_int64("date"),
        cv.to_int64("datetime"),
    )

    # asserts
    assert out1["integers"].dtype == pl.Float32
    assert out1["floats"].dtype == pl.Int32
    assert out1["floats_with_decimal"].dtype == pl.Int32
    assert out1["date"].dtype == pl.Int64
    assert out1["datetime"].dtype == pl.Int64

    assert out2["integers"].dtype == pl.Float32
    assert out2["floats"].dtype == pl.Int32
    assert out2["floats_with_decimal"].dtype == pl.Int32
    assert out2["date"].dtype == pl.Int64
    assert out2["datetime"].dtype == pl.Int64

    # The two dataframes
    assert out1.select(
        pl.col("integers"),
        pl.col("floats"),
        pl.col("floats_with_decimal"),
        pl.col("date"),
        pl.col("datetime"),
    ).frame_equal(out2)


def test_bools_conversion():
    """Convert to Booleans"""

    data = conv_data()

    out1 = (
        Cleaner(
            data,
            {
                "integers": clean().to_bool(),
                "floats": clean().to_bool(),
            },
        )
    )().collect()

    out2 = data.select(
        cv.to_bool("integers"),
        cv.to_bool("floats"),
    )

    assert out1["integers"].dtype == pl.Boolean
    assert out1["floats"].dtype == pl.Boolean
    assert out2["integers"].dtype == pl.Boolean
    assert out2["floats"].dtype == pl.Boolean


def test_strings_conversions():
    """Example Wrapper Tests"""

    data = conv_data()

    out1 = (
        Cleaner(
            data,
            {
                "integers": clean().to_string(),
                "floats": clean().to_string(),
                "floats_with_decimal": clean().to_string(),
                "date": clean().date_to_string("%Y-%m-%d"),
                "datetime": clean().date_to_string("%Y-%m-%d %H:%M:%S"),
            },
        )
    )().collect()

    out2 = data.select(
        cv.to_string("integers"),
        cv.to_string("floats"),
        cv.to_string("floats_with_decimal"),
        cv.date_to_string("date", "%Y-%m-%d"),
        cv.date_to_string("datetime", "%Y-%m-%d %H:%M:%S"),
    )

    # assertions
    assert out1["integers"].dtype == pl.Utf8
    assert out1["floats"].dtype == pl.Utf8
    assert out1["floats_with_decimal"].dtype == pl.Utf8
    assert out1["date"].dtype == pl.Utf8
    assert out1["datetime"].dtype == pl.Utf8

    assert out2["integers"].dtype == pl.Utf8
    assert out2["floats"].dtype == pl.Utf8
    assert out2["floats_with_decimal"].dtype == pl.Utf8
    assert out2["date"].dtype == pl.Utf8
    assert out2["datetime"].dtype == pl.Utf8


def test_dates_conversion():
    """Test date conversions"""

    data = conv_data()

    out1 = (
        Cleaner(
            data,
            {
                "integers": clean().int_to_date(),
                "big_integers": clean().int_to_datetime(),
                "string": clean().to_date(),
                "time_string": clean().to_time(),
            },
        )
    )().collect()

    out2 = data.select(
        cv.int_to_date("integers"),
        cv.int_to_datetime("big_integers"),
        cv.int_to_time("integers").alias("inttime"),
        cv.to_date("string").alias("date"),
        cv.to_datetime("string").alias("datetime"),
        cv.to_time("time_string", "%H:%M:%S").alias("time"),
    )

    assert out1["integers"].dtype.is_temporal()
    assert out1["big_integers"].dtype.is_temporal()
    assert out1["string"].dtype.is_temporal()
    assert out1["time_string"].dtype.is_temporal()

    assert out2["integers"].dtype.is_temporal()
    assert out2["big_integers"].dtype.is_temporal()
    assert out2["date"].dtype.is_temporal()
    assert out2["datetime"].dtype.is_temporal()
    assert out2["time"].dtype.is_temporal()
