# loading necessary packages
import csv
import numpy as np
import math
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

import random
import datetime

# Part I: Loading & Processing Data

# Reading in the data


def get_data(ext, file_name):
    """Reads the movie data file into a pandas DataFrame."""
    data = pd.read_csv(ext + file_name)
    return data

# movies = pd.read_csv('../movies_metadata.csv')

# Data Cleaning & Manipulation


def drop_columns(frame, col_list):
    """Removes unwanted columns from the data frame."""
    new_frame = frame.drop(list, axis=1)
    return new_frame


rem_list = ['adult', 'belongs_to_collection', 'homepage', 'original_language', 'overview', 'poster_path',
            'production_companies', 'production_countries', 'spoken_languages', 'status', 'tagline', 'video']


# movies_v1 = drop_columns(movies, rem_list)
# movies_v1.head()

# After dropping unecessary data, dataframe now has 12 columns


def clean_genre(frame, orig_col, new_col):
    """
    Creates a new genre column to the Dataframe that extracts the first genre
    for each movie from raw movie file. Original genre column was a dictionary
    coerced into string.

    Args:
        frame (DataFrame): movie DataFrame with raw genre
        orig_col (str): name of existing genre column
        new_col (str): name of new genre column

    Returns:
        DataFrame: dataframe with new genre column

    """
    frame[new_col] = frame[orig_col].str.split(',').apply(lambda x: x[0].split(',')[0][7:])
    return frame


# clean_genre(movies_v1, orig_col='genres', new_col='genre1').head()
# movies_v1.genre1.nunique()  # there are 24 unique genres in this dataset


def get_release_year(frame):
    """Creates a new column that extracts the release year for each movie."""
    frame['release_year'] = pd.to_numeric(frame.release_date.str.slice(0, 4), errors='coerce')
    return frame

# get_release_year(movies_v1)


def conv_to_numeric(frame):
    """Converts continuous variables from string to integer."""

    frame['popularity'] = pd.to_numeric(frame.popularity, errors='coerce')
    frame['revenue'] = pd.to_numeric(movies.revenue, errors='coerce')
    frame['budget'] = pd.to_numeric(movies.budget, errors='coerce')
    return frame

# conv_to_numeric(movies_v1)


def release_timespan(frame):
    """Calculates time between current year and release year of movie."""
    frame['release_timespan'] = datetime.datetime.now().year - frame['release_year']


# movies_v1['release_timespan'] = datetime.datetime.now().year - movies_v1['release_year']
# movies_v1.head(1)

def shift_pop(frame):
    """Converts all zeroes in the popularity column to 1."""
    frame.popularity[frame.popularity == 0] = 1
    return frame

# shift_pop(movies_v1)


def scale_pop(frame, orig_col, new_col):
    """Takes log transformation of a numeric column in dataframe."""
    frame[new_col] = np.log(frame[orig_col])
    return frame

# scale_pop(movies_v1, 'popularity', 'popularity_scaled')
# movies_v1.head(5)

# movies_v1.dtypes

# Exploratory Data Analysis


# looking for missing values in each column
# movies_v1.isnull().sum()


# working off a new copy of the cleaned up data frame to build the training set
# movies_v2 = movies_v1.copy()
# movies_v2.shape


def remove_empty(frame):
    """Removes observations with N/As or zeroes."""
    frame = frame[frame.revenue != 0]
    frame = frame[frame.budget != 0]
    frame = frame[frame.genre1 != ""]
    new_frame = frame.dropna(subset=['revenue', 'vote_average',
                                     'budget', 'runtime', 'release_year'])
    new_frame = frame.reset_index()
    return new_frame

# movies_v3 = remove_empty(movies_v2)
# movies_v3.shape

# Creating dummy variables for each movie genre


def make_genre_dummy(frame, genre_col):
    """Creates DataFrame with dummy variables for each genre."""
    genre_factor = pd.get_dummies(frame[genre_col])
    return genre_factor

# dummies = make_genre_dummy(movie_v3,'genre1')


def merge_dummies(frame1, frame2):
    """Merges movies DataFrame with movie genre dummies Dataframe."""
    movies_data = pd.merge(frame1, frame2, left_index=True, right_index=True)
    return movies_data


# Merging the dummy variables dataframe back to the existing movie dataframe
# movies_v4 = pd.merge(movies_v3, dummies, left_index=True, right_index=True)
# movies_v4.head()


# list of columns to drop for movies train dataset
rem_list2 = ['index', 'genre1', 'release_year', 'genres', 'id', 'title', 'release_date', 'imdb_id',
             'original_title', 'popularity', 'vote_count', "': 'Aniplex'", "': 'Carousel Productions'", "': 'Odyssey Media'"]

#clean_movies = drop_columns(movies_v4, rem_list2)
# Training set has approximately 5000 observations and 6 feature variables
# movies_v5.shape


#movies_v5.to_csv("movies_v5.csv", index=False)
