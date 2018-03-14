from msiapp import db
from msiapp.models import Movie
import os

# Creates a table in the database provided as the 'SQLALCHEMY_DATABASE_URI'
# configuration parameter in __init__.py with the schema defined by models.Movies()

#SQLALCHEMY_DATABASE_URI = os.environ['SQLALCHEMY_DATABASE_URI']
#db.create_engine(SQLALCHEMY_DATABASE_URI)


def create_db():
    db.create_all()
    movie1 = Movie(genre='Action', year = '2010', runtime = '100', popularity = '9',rating = '4.5', budget = '500000')
    movie2 = Movie(genre='Comedy', year = '2015', runtime = '200', popularity = '7.7',rating = '5', budget = '1000000')
    db.session.add(movie1)
    db.session.add(movie2)
    db.session.commit()

if __name__ == "__main__":
    create_db()
