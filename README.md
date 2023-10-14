<!-- These are examples of badges you might want to add to your README:
     please update the URLs accordingly
[![PyPI-Server](https://img.shields.io/pypi/v/pykurina.svg)](https://pypi.org/project/pykurina/)
[![Conda-Forge](https://img.shields.io/conda/vn/conda-forge/pykurina.svg)](https://anaconda.org/conda-forge/pykurina)
[![Monthly Downloads](https://pepy.tech/badge/pykurina/month)](https://pepy.tech/project/pykurina)
[![Twitter](https://img.shields.io/twitter/url/http/shields.io.svg?style=social&label=Twitter)](https://twitter.com/pykurina)
-->

[![ReadTheDocs](https://readthedocs.org/projects/pykurina/badge/?version=latest)](https://pykurina.readthedocs.io/en/stable/)
[![Coveralls](https://img.shields.io/coveralls/github/maqui7295/pykurina/main.svg)](https://coveralls.io/r/<USER>/pykurina)
[![Project generated with PyScaffold](https://img.shields.io/badge/-PyScaffold-005CA0?logo=pyscaffold)](https://pyscaffold.org/)

# Pykurina

> Pykurina is a Python data cleaning and validation package that wraps the awesome [polars](https://pypi.org/project/polars/) to provide a very fast and expressive API for common data cleaning and validation tasks, especially for large datasets.

## Why Pykurina?

Data cleaning is a painful aspect of data analytics. Typically, data analysts spend about 80% of their time cleaning data. In some cases, the data analyst/engineer also needs to document the data errors found, the solutions, and also, needs to validate the dataset to ensure it meets requirements.

Pykurina aims to achieve the following goals:

- Abstract away the painful and repeatable parts of data cleaning and validation
- Fast and memory-friendly (thanks to polars!)
- Generate clear documentation of the cleaning code

## Alternative

While pykurina works with pandas dataframe, consider using [pyjanitor](https://github.com/pyjanitor-devs/pyjanitor) if you have a small dataset and you're already using pandas. For large datasets (in GBs), use pykurina.

## Installation

Not yet available

## Features

### Cleaning Columns

- [ ] Data type conversion - numeric, categorical, date, string/text, etc
- [ ] Cap numeric/date column to specific max/min/formula/value
- [ ] Replace numeric outliers (with min/max/specified value)
- [ ] Fill missing values (numeric/categorical) with mean/median/mode
- [ ] Fill missing values (numeric/categorical) with other methods
- [ ] Ensure specific members in a categorical column
- [ ] Ensure consistent values in a categorical column
- [ ] Collapse categorical column into top N and "other"
- [ ] Change text casing of a categorical column to lowercase/uppercase/titlecase
- [ ] Represent categorical column in numeric format
- [ ] Represent categorical column in string format
- [ ] Collapse two or more members of a categorical column into one
- [ ] Collapse categorical column into top N and "other"

### Tidying a Dataframe

- [ ] Rename columns
- [ ] Drop unwanted columns
- [ ] Drop rows with missing values
- [ ] Drop rows with outliers
- [ ] Drop rows with complete duplicates
- [ ] Merge rows with incomplete duplicates
- [ ] Separate a column into two or more columns
- [ ] Combine two or more columns into a single column
- [ ] Extract and create a new column based on specified text
- [ ] Convert from wide format to long format or vice versa
- [ ] Filter dataframe by one or more columns
- [ ] Sort dataframe by one or more columns

### Data Validation

- [ ] Data type validation
- [ ] Constraint validation - range, field length, uniqueness, etc.
- [ ] Structure validation
- [ ] Consistency validation
- [ ] Code validation

### Miscellaneous

- [ ] Inspect columns/dataframe
- [ ] Describe columns/dataframe
- [ ] Generate documentation for the cleaning code
- [ ] Join dataframes using record linkage

## Contribution

See the [contribution guide](https://github.com/maqui7295/pykurina/blob/main/CONTRIBUTING.md)

<!-- pyscaffold-notes -->

## Note

This project has been set up using PyScaffold 4.5. For details and usage
information on PyScaffold see https://pyscaffold.org/.
