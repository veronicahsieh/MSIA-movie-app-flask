
SECRET_KEY = 'development_key'

# Local database
#SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/tracks.db'

# RDS database
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://[name_of_RDS_endpoint]'
SQLALCHEMY_TRACK_MODIFICATIONS = False
