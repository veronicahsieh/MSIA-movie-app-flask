import pickle
import datetime

import pandas as pd
from sklearn.externals import joblib

# function that takes dataframe to predict revenue


def movie_pred(user_frame):
    """Generates predicted revenue based on movie metadata.

    Args:
        user_frame: dataframe containing movie attributes.

    Returns:
        Predicted movie revenue value. Value is displayed on the results
        page of application.
    """
    movie_model = joblib.load("./develop/movie_tree.pkl")
    predicted_revenue = movie_model.predict(user_frame)
    # print(type(predicted_revenue))
    display_predicted_revenue = '${:,.2f}'.format(predicted_revenue[0])
    return display_predicted_revenue

# function to generate dataframe based on user input


def build_pred_frame(genre_code, year, runtime, popularity, rating, budget):
    """Creates data frame based on user input on movies homepage.

    Args:
        genre_code (str): code of the movie genre selected by the user. Code for a movie genre is extracted by a dictionary which maps a movie genre to its corresponding code.
        year (int): release year entered by the user.
        runtime (int): runtime of movie entered by the user.
        popularity (int): popularity of movie entered by the user.
        rating (int): rating of movie entered by the user.
        budget (int): budget of movie entered by the user.

    Returns:
        Dataframe used to make movie revenue prediction. Serves as input parameter in movie_pred(user_frame) function.

    """
    col_names = ['budget', 'runtime', 'vote_average', 'release_timespan', 'popularity_scaled', ' 10402', ' 10749', ' 10751', ' 10752',
                 ' 10769', ' 10770', ' 12', ' 14', ' 16', ' 18', ' 27', ' 28', ' 35', ' 36', ' 37', ' 53', ' 80', ' 878', ' 9648', ' 99']
    release_timespan = datetime.datetime.now().year - int(year)
    new_frame = pd.DataFrame([[int(budget), int(runtime), int(rating), release_timespan, int(
        popularity), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]], columns=col_names)
    new_frame[" " + genre_code] = 1
    return new_frame
