# import os
# import time

# import pandas as pd
# import polars as pl
# import pytest

# from pykurina.actions import clean, clean_pd
# from pykurina.cleaner import Cleaner, PDCleaner

# __author__ = "maqui7295"
# __copyright__ = "maqui7295"
# __license__ = "MIT"

# path = os.path.join('tests/data/sentiment_articles_including_bert_score.csv')

# sentiments_pd = pd.read_csv(path)
# sentiments_pl = pl.read_csv(path)

# def make_cleaner(Cleaner):
#     def cleaner(df, cleaner, *a, **kw):
#         return Cleaner(df, {
#             "paragraphs": cleaner().trim(),
#             "url": cleaner().remove('//').trim(),
#             "date": cleaner().to_datetime()
#         }, *a, **kw)

#     return cleaner


# def time_it(f):
#     start = time.perf_counter()
#     res = f()
#     end = time.perf_counter()
#     total = 1000 * (end - start)
#     print(f'It took {total:.6f} milliseconds')
#     return res, total


# def inspect(df, show_head=False):
#     if show_head:
#         print(df.head())
#     print(tuple(zip(df.columns, df.dtypes)))


# def test_example():
#     """Example Wrapper Tests"""

#     cleaner = make_cleaner(Cleaner)
#     cleaner_pd = make_cleaner(PDCleaner)

#     spec_pd = cleaner_pd(sentiments_pd, clean_pd)
#     spec_pl = cleaner(sentiments_pl, clean, is_lazy=False)
#     spec_pl_lazy = cleaner(sentiments_pl, clean)

#     res_pd, _ = time_it(spec_pd)
#     res_pl, _ = time_it(spec_pl)
#     res_pl_lazy, _ = time_it(spec_pl_lazy)

#     # The dataframes were modified
#     assert not res_pd.equals(sentiments_pd)
#     assert not res_pl.frame_equal(sentiments_pl)
#     assert not res_pl_lazy.collect().frame_equal(sentiments_pl)

#     # The dates were changed
#     assert sentiments_pl['date'].dtype == pl.Utf8
#     assert res_pl['date'].dtype == pl.Datetime
#     assert res_pl_lazy.collect()['date'].dtype == pl.Datetime


#     # The url column does not contain slashes
#     assert res_pl['url'].str.contains('//').sum() == 0
