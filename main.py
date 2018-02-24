from flask import Flask, request, render_template
from test_function import testfunction
from genres_map import make_genres_map
from predict import build_pred_frame, movie_pred
import csv
import datetime
import pandas as pd
import pickle
from sklearn.externals import joblib

app = Flask(__name__)

@app.route('/') #root directory, homepage of the website
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/results', methods = ['POST'])
def inputdata():
    if request.method == 'POST':
        genre = request.form['genre']
        year = request.form['release_year']
        runtime = request.form['runtime']
        popularity = request.form['popularity']
        rating = request.form['rating']
        budget = request.form['budget']

        genres_map = {}
        make_genres_map(genres_map,"genres_map.csv")

        genres_code = genres_map.get(genre)

        sample_frame = build_pred_frame(genres_code,year,runtime,popularity,rating,budget)
        revenue = movie_pred(sample_frame)

        return revenue

        #return render_template("results.html",result = revenue)

if __name__ == "__main__": #quick check that only run app whenever this app is called directly
    app.run(debug=True) #start this app
