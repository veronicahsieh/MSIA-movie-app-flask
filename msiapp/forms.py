from wtforms import Form, BooleanField, StringField, validators
from flask_wtf import Form,FlaskForm

class movie_form(Form):
    #genre = SelectField(u'Movie Genres', choices = ['action','comedy','horror'])
    release_year = IntegerField('Year')
    rating = IntegerField('Movie Rating')
    popularity = IntegerField('Popularity Scale', [validators.NumberRange(min = 1,max = 10)])
    runtime = IntegerField('Runtime')
    budget = IntegerField('Budget')
