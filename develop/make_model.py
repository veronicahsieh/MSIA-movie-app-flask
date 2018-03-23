# loading necessary packages
import sys
import csv
import math
import numpy as np
import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
import random
from sklearn.metrics import r2_score

from movies_data_cleaning import get_data


def make_model(frame, x_col, y_col):
    """
    Takes the movie DataFrame and splits it into a training/test set.
    Decision tree model is created from training set and evaluated on the test
    data.

    Args:
        frame (DataFrame): used to build the various data sets and model.

    Returns:
        Model object which can predict movie revenue
    """
    # Creating the training and test set
    train_frame, test_frame = train_test_split(frame, test_size=0.2, random_state=33)
    x_train = train_frame[x_col]
    y_train = train_frame[y_col]
    x_test = test_frame[x_col]
    y_test = test_frame[y_col]

    # Building the model object
    movie_model = DecisionTreeRegressor(max_depth=8, min_samples_leaf=7)
    movie_model = movie_model.fit(x_train, y_train)

    # Evaluating the test set
    y_pred_test = movie_model.predict(x_test)
    test_rsquared = r2_score(y_test, y_pred_test)
    print(test_rsquared)
    return movie_model


# Saving the model object
def create_pickle(path, model):
    """Saves the model object to a pickle file."""
    pickle_path = open(path, 'wb')
    pickle.dump(model, pickle_path)
    pickle_path.close()


if __name__ == '__main__':
    # Loading in the data
    data = sys.argv[1]
    clean_movies = get_data('', "clean_movies.csv")
    clean_movies = clean_movies.dropna()

    # Create model using dataset
    x_columns = ['budget', 'runtime', 'vote_average', 'release_timespan',
                           'popularity_scaled', ' 10402', ' 10749', ' 10751',
                           ' 10752', ' 10769', ' 10770', ' 12', ' 14', ' 16',
                           ' 18', ' 27', ' 28', ' 35', ' 36', ' 37', ' 53',
                           ' 80', ' 878', ' 9648', ' 99']
    y_columns = ['revenue']
    movie_model = make_model(clean_movies, x_columns, y_columns)

    # Write the model file to csv
    create_pickle('movies.pkl', movie_model)
