from flask import Flask, request, jsonify
import base64
from io import BytesIO
import re
from PIL import Image, ImageFilter
from flask import render_template

from model import *

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index(name=None):
    if request.method == 'POST':
        message = request.json['message']

        

        loaded_model = Net(message)
        result = loaded_model.main()
        return result