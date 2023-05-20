from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from redis import Redis
# from my_app.hello.views import hello
# from my_app.jinja2.views import jinj2

redis = Redis()

# create the extension
db = SQLAlchemy()

app = Flask(__name__)
# app.register_blueprint(hello)
# app.register_blueprint(jinj2)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:Programdog666@localhost/flask_db"
db.init_app(app)
migrate = Migrate(app, db)

from my_app.database.views import database
app.register_blueprint(database)


with app.app_context():
    db.create_all()