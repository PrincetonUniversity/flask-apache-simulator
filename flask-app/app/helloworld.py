#!/bin/env python

from flask import Flask
from flask import request
import logging
app = Flask(__name__)

@app.route('/')
def hello_world():
    logging.debug(f"request headers:{request.headers}")
    return 'Flask Dockerized'


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    app.run(debug=True,host='0.0.0.0',port='8888')
