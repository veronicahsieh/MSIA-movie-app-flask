import pytest
import sys
import csv
import numpy as np
import math
import pandas as pd
import random
import datetime

sys.path.append("..")
from movies_data_cleaning import conv_to_numeric, scale_pop, drop_columns
from predict import movie_pred, build_pred_frame

# Construct dataframe of test data

test_data = pd.DataFrame(
    {"country": ['Morocco', 'Japan', 'Indonesia', 'South Africa',
                 'Brazil', 'Japan', 'Japan', 'South Africa'],
     "popularity": ['150', '56', '26', '13', '16', '175', '57', '87'],
     "release_year": ['2014', '2010', '2000', '2015', '2015', '2000', '2000', '2018'],
     "budget": ['30000', '75000', '250000', '34500', '750000', '120000', '880950', '22500'],
     "random": ['green', 'blue', 'blue', 'red', 'blue', 'red', 'purple', 'orange'],
     "random2": ['hello', 'hi', 'hey', 'goodbye', 'adios', 'byebye', 'hello_again', 'today'],
     "revenue": ['502000', '20140000', '2103000', '37045000', '7535000', '21350000', '103200500', '35010320']}, index=[1, 2, 3, 4, 5, 6, 7, 8])

remove = ['country', 'random', 'random2']


def test_conv_to_numeric():
    """Test that data is properly read into a DataFrame."""

    # Check that output is the correct data type
    assert conv_to_numeric(test_data).popularity[1] == 150


def test_drop_columns():
    """Test that data is properly read into a DataFrame."""

    # Check that output is still a DataFrame
    assert isinstance(drop_columns(test_data, remove), pd.DataFrame)

    # Check that output has the correct number of columns
    assert drop_columns(test_data, remove).shape[1] == 4


def test_build_pred_frame():
    """Check that Dataframe is properly constructed from user input data."""

    # Check that output is a DataFrame
    assert isinstance(build_pred_frame('28', 2010, 400, 7, 4, 50000), pd.DataFrame)

    # Check that function returns DataFrame with 25 columns
    assert build_pred_frame('28', 2010, 400, 7, 4, 50000).shape == (1, 25)
