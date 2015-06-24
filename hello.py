#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, request
import api
import pdb

app = Flask(__name__)
app.register_blueprint(api.app_api, url_prefix='/api')

@app.route('/')
def index():
    pdb.set_trace()
    return 'hello world!'

app.run(debug=True)
