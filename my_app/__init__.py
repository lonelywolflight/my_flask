from flask import Flask
from my_app.hello.views import hello
from my_app.jinja2.views import jinj2
app = Flask(__name__)
app.register_blueprint(hello)
app.register_blueprint(jinj2)