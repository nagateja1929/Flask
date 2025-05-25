from flask import *
from flask import Flask
from flask import render_template

app = Flask(__name__)
@app.route('/',methods=['GET'])
def index():
    return {"Content":"HI, how are you?"}

if __name__ == '__main__':
    app.run(port=8888)