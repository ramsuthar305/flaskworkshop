from flask import Flask,request
from flask_pymongo import PyMongo
# from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.config.from_object("config.Config")
mongo = PyMongo(app)
# csrf = CSRFProtect(app)

from authModule.views import auth

app.register_blueprint(auth, url_prefix='/auth')


if __name__ == '__main__':
    app.run(debug=True)
    



