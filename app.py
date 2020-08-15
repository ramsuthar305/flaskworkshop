from flask import Flask,request, render_template, Markup
import json
import chardet

app = Flask(__name__)
app.config.from_object("config.config")

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/put_task',methods=['GET','POST'])
def put_task():
    if request.method=='POST':
        task=request.form['task']
        priority=request.form['priority']
        print(task,priority)
        tasks=[
            {'task':task,'priority':priority,'date':datetime.now()},
            {'task':'task1','priority':'priority2','date':datetime.now()},
            {'task':'task2','priority':'priority2','date':datetime.now()}
        ]
    return render_template('index.html',tasks=tasks)

if __name__=='__main__':
    app.run(debug=True)


