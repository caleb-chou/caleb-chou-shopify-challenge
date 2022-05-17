from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def home():
    return "<p>Test</p>"

@app.route('/create', methods = ['POST'])
def create():
    if request.content_type != 'application/json':
        return {}, 400
    return request.json