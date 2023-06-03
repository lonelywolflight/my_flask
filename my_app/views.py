from flask.typing import ResponseReturnValue
from flask.views import View, MethodView
from flask import request
from my_app import app

class GetPostRequest(View):

    methods = ['GET', 'POST']
    
    def dispatch_request(self) -> ResponseReturnValue:
        if request.method == 'GET':
            bar = request.args.get('foo', 'bar')
        else:
            bar = request.form.get('foo', 'bar')
        return 'A simple Flask request where foo is %s' % bar
    
app.add_url_rule('/a-request', view_func = GetPostRequest.as_view('a_request'))



class GetRequest(View):

    def dispatch_request(self) -> ResponseReturnValue:
        bar = request.args.get('foo', 'bar')
        return 'A simple Flask request where foo is %s' % bar
    
app.add_url_rule('/a-get-request', view_func=GetRequest.as_view('get-request'))


class GetMethodRequest(MethodView):

    def get(self):
        bar = request.args.get('foo', 'bar')
        return 'A simple Flask request where foo is %s' % bar
    

    def post(self):
        bar = request.form.get('foo', 'bar')
        return 'A simple Flask request where foo is %s' % bar
    
app.add_url_rule('/method-request', view_func=GetMethodRequest.as_view('method_request'))