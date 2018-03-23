# loading necessary packages
import csv
import math
import numpy as np
import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
import random
from sklearn.metrics import r2_score


def make_model(frame):
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
    x_train = train_frame[['budget', 'runtime', 'vote_average', 'release_timespan',
                           'popularity_scaled', ' 10402', ' 10749', ' 10751',
                           ' 10752', ' 10769', ' 10770', ' 12', ' 14', ' 16',
                           ' 18', ' 27', ' 28', ' 35', ' 36', ' 37', ' 53',
                           ' 80', ' 878', ' 9648', ' 99']]
    y_train = train_frame['revenue']
    x_test = test_frame[['budget', 'runtime', 'vote_average', 'release_timespan',
                         'popularity_scaled', ' 10402', ' 10749', ' 10751',
                         ' 10752', ' 10769', ' 10770', ' 12', ' 14', ' 16', ' 18',
                         ' 27', ' 28', ' 35', ' 36', ' 37', ' 53', ' 80', ' 878',
                         ' 9648', ' 99']]
    y_test = test_frame['revenue']

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
