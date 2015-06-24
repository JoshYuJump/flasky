#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Blueprint
from flask.ext import restful


app_api = Blueprint('app_api', __name__)
api = restful.Api()
api.init_app(app_api)

class HelloWorld(restful.Resource):
    def get(self):
        return [{'hello': 'world'}]
    def patch(self):
    	return {'patch':'success'}
    def patch1(self):
    	return {'aaa':'success'}	    

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app_api.run(debug=True)