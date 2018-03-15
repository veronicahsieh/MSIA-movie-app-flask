from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy

from msiapp import application, db
from msiapp.models import Movie

from develop.genres_map import make_genres_map
from develop.predict import build_pred_frame, movie_pred

import csv
import datetime
import pandas as pd
import pickle
from sklearn.externals import joblib

#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'


@application.route('/')  # root directory, homepage of the website
def index():
    return render_template('index.html')


@application.route('/about')
def about():
    return render_template('about.html')


@application.route('/results', methods=['POST'])
def inputdata():
    if request.method == 'POST':
        genre = request.form['genre']
        year = request.form['release_year']
        runtime = request.form['runtime']
        popularity = request.form['popularity']
        rating = request.form['rating']
        budget = request.form['budget']

        movie_entry = Movie(genre=request.form['genre'], year=request.form['release_year'], runtime=request.form['runtime'],
                            popularity=request.form['popularity'], rating=request.form['rating'], budget=request.form['budget'])
        db.session.add(movie_entry)
        db.session.commit()

        genres_map = {}
        make_genres_map(genres_map, "genres_map.csv")

        genres_code = genres_map.get(genre)

        sample_frame = build_pred_frame(genres_code, year, runtime, popularity, rating, budget)
        revenue = movie_pred(sample_frame)

        return render_template("results.html", revenue=revenue, movies=Movie.query.all())


if __name__ == "__main__":  # quick check that only run app whenever this app is called directly
    application.run(host='0.0.0.0', debug=True)  # start this app
