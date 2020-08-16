from flask import Flask, Blueprint, request, redirect, session, jsonify
from .models import auth1
import json
auth_obj = auth1()

auth = Blueprint('auth', __name__, template_folder='',
                 static_folder='', static_url_path='')

auth_obj = auth1()
# 127.0.0.1:5000/auth/login


@auth.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':
        data = request.get_data()
        data = json.loads(data)
        data['_id']=data['email']
        status = auth_obj.register_user(data)
    return json.dumps(data)

@auth.route('/login', methods=['POST'])
def login():
    if request.method=='POST':
        if 'logged_in' in session:
            return jsonify({"status":'user is already logged.'})
        else:
            data = request.get_data()
            data = json.loads(data)
            data['_id']=data['username']
            del data['username']
            status = auth_obj.login_user(data)
            if not status:
                return jsonify({"status":'login credentials invalid'})
            else:
                session['username']=status["_id"]
                session['logged_in']=True
                return jsonify({"data":status,"status":"user logged in succesffully"})

@auth.route('/logout',methods=['GET'])
def logout():
    del session['logged_in']
    del session['username']
    return jsonify({"status":"user logged out in succesffully"})
