from flask import Flask
from .config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
print(Config.SQLALCHEMY_DATABASE_URI)
app.config.from_object(Config)
db = SQLAlchemy(app)
# ma = Marshmallow(app)
migrate = Migrate(app, db)

from app import routes, models
