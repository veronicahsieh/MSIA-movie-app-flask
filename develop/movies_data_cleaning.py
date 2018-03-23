# loading necessary packages
import sys
import csv
import numpy as np
import math
import pandas as pd
import random
import datetime


def get_data(ext, file_name):
    """Reads the movie data file into a pandas DataFrame."""
    data = pd.read_csv(ext + file_name)
    return data


def drop_columns(frame, col_list):
    """Removes unwanted columns from the data frame."""
    new_frame = frame.drop(col_list, axis=1)
    return new_frame


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
        Dataframe with new genre column
    """
    frame[new_col] = frame[orig_col].str.split(',').apply(lambda x: x[0].split(',')[0][7:])
    return frame


def get_release_year(frame):
    """Creates a new column that extracts the release year for each movie."""
    frame['release_year'] = pd.to_numeric(frame.release_date.str.slice(0, 4), errors='coerce')
    return frame


def conv_to_numeric(frame):
    """Converts continuous variables from string to integer."""

    frame['popularity'] = pd.to_numeric(frame.popularity, errors='coerce')
    frame['revenue'] = pd.to_numeric(frame.revenue, errors='coerce')
    frame['budget'] = pd.to_numeric(frame.budget, errors='coerce')
    return frame


def release_timespan(frame):
    """Calculates time between current year and release year of movie."""
    frame['release_timespan'] = datetime.datetime.now().year - frame['release_year']
    return frame


def shift_pop(frame):
    """Converts all zeroes in the popularity column to 1."""
    frame.popularity[frame.popularity == 0] = 1
    return frame


def scale_pop(frame, orig_col, new_col):
    """Takes log transformation of a numeric column in dataframe."""
    frame[new_col] = np.log(frame[orig_col])
    return frame


def remove_empty(frame):
    """Removes observations with N/As or zeroes."""
    frame = frame[frame.revenue != 0]
    frame = frame[frame.budget != 0]
    frame = frame[frame.genre1 != ""]
    new_frame = frame.dropna(subset=['revenue', 'vote_average',
                                     'budget', 'runtime', 'release_year'])
    new_frame = frame.reset_index()
    return new_frame


def make_genre_dummy(frame, genre_col):
    """Creates DataFrame with dummy variables for each genre."""
    genre_factor = pd.get_dummies(frame[genre_col])
    return genre_factor


def merge_dummies(frame1, frame2):
    """Merges movies DataFrame with movie genre dummies Dataframe."""
    movies_data = pd.merge(frame1, frame2, left_index=True, right_index=True)
    return movies_data


if __name__ == '__main__':
    # Loading in the data
    data = sys.argv[1]
    movies = get_data('', data)

    # Data cleaning and transformations
    rem_list = ['adult', 'belongs_to_collection', 'homepage', 'original_language',
                'overview', 'poster_path', 'production_companies', 'production_countries',
                'spoken_languages', 'status', 'tagline', 'video']
    movies_v1 = drop_columns(movies, rem_list)
    movies_v1 = clean_genre(movies_v1, orig_col='genres', new_col='genre1')
    movies_v1 = get_release_year(movies_v1)
    movies_v1 = conv_to_numeric(movies_v1)
    movies_v1 = release_timespan(movies_v1)
    movies_v1 = shift_pop(movies_v1)
    movies_v1 = scale_pop(movies_v1, 'popularity', 'popularity_scaled')
    movies_v2 = movies_v1.copy()
    movies_v2 = remove_empty(movies_v1).reset_index()

    # Create dummy variables and feature variables dataset
    genres_frame = make_genre_dummy(movies_v2, 'genre1').reset_index()

    rem_list2 = ['level_0', 'index_x', 'index_y', 'genre1', 'release_year', 'genres', 'id', 'title', 'release_date',
                 'imdb_id', 'original_title', 'popularity', 'vote_count',
                 "': 'Aniplex'", "': 'Carousel Productions'", "': 'Odyssey Media'"]
    movies_v3 = merge_dummies(movies_v2, genres_frame)
    movies_v4 = drop_columns(movies_v3, rem_list2)

    # Write final dataset to csv
    movies_v4.to_csv("clean_movies.csv", index=False)
