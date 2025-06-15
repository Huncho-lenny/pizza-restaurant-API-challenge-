import os 

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class config:
    SQLALCHEMY_DATABASE_URI = "sqlite:///app.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


