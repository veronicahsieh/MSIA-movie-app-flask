from flask import Flask, request, render_template
from wtforms import Form, BooleanField, StringField, IntegerField, validators
from flask_wtf import FlaskForm
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)

csrf= CSRFProtect(app)

class movie_form(FlaskForm):
    #genre = SelectField(u'Movie Genres', choices = ['action','comedy','horror'])
    release_year = IntegerField('Year')
    rating = IntegerField('Movie Rating')
    popularity = IntegerField('Popularity Scale', [validators.NumberRange(min = 1,max = 10)])
    runtime = IntegerField('Runtime')
    budget = IntegerField('Budget')

@app.route('/',methods = ['GET','POST']) #root directory, homepage of the website
def index():
    form = movie_form()
    return render_template('index.html', form = form)

if __name__ == "__main__": #quick check that only run app whenever this app is called directly
    app.run(debug=True) #start this app


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/inputdata', methods = ['POST'])
def show_data():
    if request.method == 'POST':
        return request.form['genre']
