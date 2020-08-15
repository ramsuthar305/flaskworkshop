from flask import Flask, request, render_template, Markup, jsonify, redirect, url_for, flash
import json
from bson import ObjectId
import chardet
from datetime import datetime
from flask_pymongo import PyMongo

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.config.from_object("config.config")
mongo = PyMongo(app)
db = mongo.db




@app.route('/')
def hello_world():
    tasks = read_from_db()
    print('Data from pymonog: ',tasks)
    return render_template('index.html', tasks=tasks)

def write_to_db(obj):
    res = db.todo.insert(obj)
    print(res)

def read_from_db():
    tasks=list(db.todo.find())
    return tasks

def delete_from_db(id):
    deleteRes=db.todo.delete_one({"_id":ObjectId(id)})
    if deleteRes.deleted_count >0:
        return "Objected deleted successfully"
    else:
        return "object not deleted"


@app.route('/put_task', methods=['GET', 'POST'])
def put_task():
    if request.method == 'POST':
        task = request.form['task']
        priority = request.form['priority']
        write_to_db({'tasks': task, 'priority': priority, 'date': datetime.now()})
        print(task, priority)
        tasks = read_from_db()
        print('Data from pymonog: ',tasks)
    return render_template('index.html', tasks=tasks)

@app.route('/deleteTask',methods=['GET','POST'])
def delete_task():
    if request.method=='GET':
        id=request.args.get('id',default=None,type=str)
        print(id)
        status=delete_from_db(id)
        flash(status)
    return redirect(url_for('hello_world'))


if __name__ == '__main__':
    app.secret_key=b'_5#y2L"F4Q8z\n\xec]/'
    app.run(debug=True)
