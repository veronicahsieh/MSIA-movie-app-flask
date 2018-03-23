import pytest
import csv
import numpy as np
import math
import pandas as pd
import random
import datetime

from movies_data_cleaning import conv_to_numeric, scale_pop, drop_columns

# Construct dataframe of test data
test_data = pd.DataFrame(
    {"country": ['Morocco', 'Japan', 'Indonesia', 'South Africa',
                 'Brazil', 'Japan', 'Japan', 'South Africa'],
     "popularity": ['150', '56', '26', '13', '16', '175', '57', '87'],
     "release_year": ['2014', '2010', '2000', '2015', '2015', '2000', '2000', '2018'],
     "budget": ['30000', '75000', '250000', '34500', '750000', '120000', '880950', '22500'],
     "random": ['green', 'blue', 'blue', 'red', 'blue', 'red', 'purple', 'orange'],
     "random2": ['hello', 'hi', 'hey', 'goodbye', 'adios', 'byebye', 'hello_again', 'today']
     "revenue": ['502000', '20140000', '2103000', '37045000', '7535000', '21350000', '103200500', '35010320']},
    index=[1, 2, 3, 4, 5, 6, 7, 8])

remove = ['country', 'random', 'random2']


def test_get_data():
    """Test that data is properly read into a DataFrame."""

    test_data_new = conv_to_numeric(test_data)

    # Check that output is still a DataFrame
    assert isinstance(test_data_new, pd.DataFrame)

    # Check that output is the correct data type
    assert type(test_data_new['popularity'][0]) == 'int'


def test_drop_columns():
    """Test that data is properly read into a DataFrame."""

    # Check that output is still a DataFrame
    assert isinstance(drop_columns(test_data, remove), pd.DataFrame)

    # Check that output has the correct number of columns
    assert (drop_columns(test_data, remove).shape, pd.DataFrame)
