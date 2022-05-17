from flask import Flask
from flask import request
import json

app = Flask(__name__)

@app.route('/')
def home():
    return "<p>Test</p>"

# ITEM STRUCTURE
# ID: str
# NAME : str
# DESCRIPTION: str
# QUANTITY : int
# TAGS : List<str>

@app.route('/create', methods = ['POST'])
def create():
    if request.content_type != 'application/json':
        return {'Error': 'Endpoint only Accept JSON'}, 400
    with open('app/data/data.json', 'r+', encoding='utf-8') as f:
        data = json.load(f)
        if request.json['ID'] in data:
            return {'Error': 'Record Already Exists'}, 400
        data[request.json['ID']] = request.json
        f.seek(0)
        json.dump(data, f, indent=4, ensure_ascii=False,)
    return request.json

@app.route('/update', methods = ['POST'])
def update():
    if request.content_type != 'application/json':
        return {'Error': 'Endpoint only Accept JSON'}, 400
    with open('app/data/data.json', 'r+', encoding='utf-8') as f:
        data = json.load(f)
        if request.json['ID'] in data:
            return {'Error': 'Record Already Exists'}, 400
        data[request.json['ID']] = request.json
        f.seek(0)
        json.dump(data, f, indent=4, ensure_ascii=False,)
    return request.json

@app.route('/delete', methods = ['POST'])
def delete():
    if request.content_type != 'application/json':
        return {'Error': 'Endpoint only Accept JSON'}, 400
    with open('app/data/data.json', 'r+', encoding='utf-8') as f:
        data = json.load(f)
        if request.json['ID'] in data:
            return {'Error': 'Record Already Exists'}, 400
        data[request.json['ID']] = request.json
        f.seek(0)
        json.dump(data, f, indent=4, ensure_ascii=False,)
    return request.json

@app.route('/view', methods = ['GET', 'POST'])
def view():
    if request.method == 'POST':
        return {'POST':''}
    else:
        return {'GET':''}

