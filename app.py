import os

from flask import Flask

app = Flask(__name__)

@app.route('/hello/<whoami>')
def hello_world(whoami):
    return "Hello {}".format(whoami or "World")

 
