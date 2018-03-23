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


# Loading in the clean dataset generated from the EDA/Data Cleansing notebook

def create_train_test(frame, train_frame, test_frame, test_prop):
    train_frame, test_frame = train_test_split(frame, test_size=test_prop, random_state=33)
    return train_frame, test_frame


# X = movies_train[['budget','runtime','vote_average','release_timespan','popularity_scaled',
 ' 10402', ' 10749', ' 10751', ' 10752', ' 10769', ' 10770', ' 12', ' 14', ' 16', ' 18', ' 27', ' 28', ' 35', ' 36', ' 37',
 ' 53', ' 80', ' 878', ' 9648', ' 99']]
# y = movies_train['revenue']


# X_test = movies_test[['budget','runtime','vote_average','release_timespan','popularity_scaled',' 10402',' 10749',
 ' 10751', ' 10752', ' 10769', ' 10770', ' 12', ' 14', ' 16', ' 18', ' 27', ' 28', ' 35', ' 36', ' 37', ' 53', ' 80', ' 878', ' 9648', ' 99']]
#_test = movies_test['revenue']


def make_model(x, y):
    movie_model = DecisionTreeRegressor(max_depth = 8, min_samples_leaf = 7)
    movie_model = movie_model.fit(x, y)
    return movie_model

# tree_fit = make_model(X, y)


# movies_treefit = DecisionTreeRegressor(max_depth = 8, min_samples_leaf = 7)
# movies_treefit = movies_treefit.fit(X, y)


# training R-squared
# y_true= movies_train['revenue']
# y_pred= movies_treefit.predict(X)
# train_rsquared= r2_score(y_true, y_pred)
# train_rsquared

# test R-squared
# y_true_test= movies_test['revenue']
# y_pred_test= movies_treefit.predict(X_test)
# test_rsquared= r2_score(y_true_test, y_pred_test)
# test_rsquared

# X.head()

# Saving Decision Tree Model

def create_pickle(path, model):
    pickle_path = open(path, 'wb')
    pickle.dump(model, pickle_path)
    pickle_path.close()


# movie_model_path= 'movie_tree.pkl'
# Create an variable to pickle and open it in write mode
# model_pickle= open(movie_model_path, 'wb')
# pickle.dump(movies_treefit, model_pickle)
# model_pickle.close()
