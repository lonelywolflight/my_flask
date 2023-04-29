from flask import Blueprint

jinj2 = Blueprint('jinja', __name__)

@jinj2.route('/hello/<user>')
def hello_jinja2(user = None):
    user = user or 'Max'
    return '''
    <html>
        <head>
            <title>Flask Framework Cookbook</title>
        </head>
            <body>
                <h1>Hello %s!</h1>
                <p>Welcome to the world of Flask!</p>
            </body>
    </html>''' % user