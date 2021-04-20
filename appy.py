from flask import Flask
from flask_pymongo import PyMongo
from bson.json_util import dumps
from bson.objectid import ObjectId
from flask import jsonify, request
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

app.secret_key = "secretkey"

app.config['MONGO_URI'] = "mongodb://localhost:27017/Users"
mongo = PyMongo(app)

@app.route('/add', methods=['POST']) # adding user in database
def add_user():
    _json = request.json
    _name = _json['name']
    _email = _json['email']
    _password = _json['pwd']

    if _name and _email and request.method == 'POST':
        
        _hashed_password = generate_password_hash(_password)

        id = mongo.db.user.insert({'name': _name, 'email': _email,'pwd': _hashed_password})
        resp = jsonify("User added successfully")
        resp.status_code = 200
        return resp

    else:
        return not_found()

@app.route('/additems/<id>', methods=['POST']) # adding items for particular user
def add_item(id):
    _json = request.json
    _item1 = _json['item1']
    _item2 = _json['item2']
    _item3 = _json['item3']

    id = mongo.db.user.insert({'item1': _item1, 'item2': _item2,'item3': _item3})
    resp = jsonify("Useritem added successfully")
    resp.status_code = 200
    return resp


@app.route('/users') # viewing all  the users in the database
def users():
    users = mongo.db.user.find()
    resp = dumps(users)
    return resp

@app.route('/user/<id>') # viewing the particular user in the database with particular id
def user(id):
    user = mongo.db.user.find_one({'_id': ObjectId(id)})
    resp = dumps(user)
    return resp


@app.route('/delete/<id>',methods=['DELETE']) # deleting the user
def delete_user(id):
    mongo.db.user.delete_one({'_id': ObjectId(id)})
    resp = jsonify("User deleted successfully")
    resp.status_code = 200
    return resp


@app.route('/update/<id>',methods=['PUT']) # updating the user information
def update_user(id):
    _id = id
    _json = request.json
    _name = _json['name']
    _email = _json['email']
    _password = _json['pwd']

    if _name and _email and _password and _id and request.method == 'PUT':
        _hashed_password = generate_password_hash(_password)

        mongo.db.user.update_one({'id': ObjectId(_id['$oid']) if '$oid' in _id else ObjectId(_id)}, {'$set': {'name':_name, 'email':_email, 'pwd':_hashed_password}})

        resp = jsonify("user updated successfully")

        resp.status_code = 200

        return resp
    else:
        return not_found()

@app.errorhandler(404)
def not_found(error = None):
    message = {
        'status':404,
        'message':'Not Found' + request.url
    }
    resp = jsonify(message)
    resp.status_code = 404
    return resp

if __name__ == "__main__":
    app.run(debug=True)


