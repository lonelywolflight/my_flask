from flask import Flask
from flask_mongoengine import MongoEngine

db = MongoEngine()

app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = [{
    "DB": 'my_app',
    "host": "localhost",
    "port": 27017,
    "alias": "default",
}]

db.init_app(app)


from my_app.database.views import database
app.register_blueprint(database)