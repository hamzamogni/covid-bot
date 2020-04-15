from flask import Flask, request
from model import *

app = Flask(__name__)

@app.route("/", methods=["POST"])
def index(name=None):
    if request.method == 'POST':
        message = request.json['message']

        loaded_model = Net(message)
        result = loaded_model.main()
        return result