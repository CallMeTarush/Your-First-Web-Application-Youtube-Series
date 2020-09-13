from flask import Flask
from datetime import datetime
from flask_cors import CORS
app = Flask(__name__)
cors = CORS(app)

@app.route('/')
def hello_world():
    return 'Hi! John The time is ' + str(datetime.now())
