import os

BASE_DIR = os.path.dirname(__file__)

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'swsecteam1.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False


# check before launching
SECRET_KEY = "dev"
