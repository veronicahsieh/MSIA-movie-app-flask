from msiapp import db

# Create a data model for the database to be setup for the app
class Movie(db.Model):
    """Table to store movies metadata entered by a user.

    Attributes:
        attr1: Description of `attr1`.
        attr2: Description of `attr2`.

    """
    id = db.Column(db.Integer, primary_key = True)
    genre = db.Column(db.String(100), unique = False, nullable = False)
    year = db.Column(db.Integer, unique = False, nullable = False)
    runtime = db.Column(db.Integer, unique = False, nullable = False)
    popularity = db.Column(db.Float, unique = False, nullable = False)
    rating = db.Column(db.Float, unique = False, nullable = False)
    budget = db.Column(db.Integer, unique = False, nullable = False)

    def __repr__(self):
        return '<Movie %r>' % self.id
