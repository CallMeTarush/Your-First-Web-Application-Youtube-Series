from flask import Flask
from datetime import datetime
from flask_cors import CORS
from flask import request

app = Flask(__name__)
cors = CORS(app)

@app.route('/')
def hello_world():
    return 'Hi! John The time is ' + str(datetime.now())

data = ['Web', 'Application']

@app.route('/create', methods=['POST'])
def create():
    name = request.form['name']
    data.append(name)
    return "Done"

@app.route('/read/<index>', methods=['GET'])
def read(index):
	name = data[int(index)]
	return name

@app.route('/update', methods=['POST'])
def update():
	index = int(request.form['index'])
	new_name = request.form['newName']
	data[index] = new_name
	return "Done"

@app.route('/delete/<index>', methods=['DELETE'])
def delete(index):
	data[int(index)] = ''
	return "Done"
