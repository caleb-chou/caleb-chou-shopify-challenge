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
        if not request.json['ID'] in data:
            return {'Error': 'Record Does Not Exists'}, 400
        for key in request.json:
            data[request.json['ID']][key] = request.json[key]
        f.seek(0)
        json.dump(data, f, indent=4, ensure_ascii=False,)
    return request.json

# DELETED ITEM STRUCTURE
# KEY : ITEM ID
# VALUE: LIST OF DELETED VERSIONS OF ITEMS

@app.route('/delete', methods = ['POST'])
def delete():
    if request.content_type != 'application/json':
        return {'Error': 'Endpoint only Accept JSON'}, 400
    with open('app/data/data.json', 'r+', encoding='utf-8') as f:
        data = json.load(f)
        if not request.json['ID'] in data:
            return {'Error': 'Record Does Not Exists'}, 400
        res = data.pop(request.json['ID'])
        f.seek(0)
        f.truncate()
        json.dump(data, f, indent=4, ensure_ascii=False)
    with open('app/data/deleted.json', 'r+', encoding='utf-8') as d:
        deleted = json.load(d)
        if res['ID'] in deleted:
            deleted[res['ID']].append(res)
        else:
            deleted[res['ID']] = [res]
        d.seek(0)
        json.dump(deleted, d, indent=4, ensure_ascii=False)
    return res

@app.route('/restore', methods = ['POST'])
def restore():
    if request.content_type != 'application/json':
        return {'Error': 'Endpoint only Accept JSON'}, 400
    with open('app/data/deleted.json', 'r+', encoding='utf-8') as d:
        deleted = json.load(d)
        if request.json['ID'] in deleted:
            r = deleted[request.json['ID']].pop(request.json['INDEX']) if 'INDEX' in request.json else deleted[request.json['ID']].pop(0)
        d.seek(0)
        d.truncate()
        json.dump(deleted, d, indent=4, ensure_ascii=False)
    with open('app/data/data.json', 'r+', encoding='utf-8') as f:
        data = json.load(f)
        if request.json['ID'] in data:
            return {'Error': 'Record Already Exists'}, 400
        data[request.json['ID']] = r
        f.seek(0)
        json.dump(data, f, indent=4, ensure_ascii=False,)
    return request.json

@app.route('/getdeleted', methods = ['GET'])
def getdeleted():
    with open('app/data/deleted.json', 'r+', encoding='utf-8') as f:
        res = json.load(f)
        return(res)

@app.route('/view', methods = ['GET', 'POST'])
def view():
    if request.method == 'POST':
        if request.content_type != 'application/json':
            return {'Error': 'Endpoint only Accept JSON'}, 400
        with open('app/data/data.json', encoding='utf-8') as f:
            data = json.load(f)
            if not request.json['ID'] in data:
                return {'Error': 'Record Does Not Exists'}, 400
            return data[request.json['ID']]
    else:
        with open('app/data/data.json', encoding='utf-8') as f:
            data = json.load(f)
            return data

