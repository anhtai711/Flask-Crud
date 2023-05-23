from re import I
from flask import Flask
from flask_marshmallow import Marshmallow
from app.db import db
from config import Config
from flask_migrate import Migrate

app = Flask(__name__)
ma = Marshmallow(app)

app.config["SQLALCHEMY_DATABASE_URI"] = Config.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = Config.SQLALCHEMY_TRACK_MODIFICATIONS 

from app.routes.category import category
from app.routes.author import author
from app.routes.book import book
app.register_blueprint(category)
app.register_blueprint(author)
app.register_blueprint(book)

db.init_app(app)
Migrate(app, db)
