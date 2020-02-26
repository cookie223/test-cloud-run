import os

from flask import Flask

app = Flask(__name__)

@app.route('/<whoami>')
def hello_world(whoami):
    return "Hello {}".format(whoami)

 @app.route('/')
def hello_world():
    return "Hello World"
