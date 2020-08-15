import os

class config:
    DEBUG = os.environ.get('DEBUG')
    FLASK_ENV=os.environ.get('FLASK_ENV')
    SESSION_KEY=os.environ.get('SESSION_KEY')