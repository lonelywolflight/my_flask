from my_app import app
from my_app.hello.models import MESSAGE


@app.route('/')
@app.route('/hello')
def hello_world():
    return MESSAGE['default']


@app.route('/show/<key>')
def get_message(key):
    return MESSAGE.get(key) or "%s not found!" % key


@app.route('/add/<key>/<message>')
def add_or_update_message(key, message):
    MESSAGE[key] = message
    return "%s Added/Updated" % key