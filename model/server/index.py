from flask import Flask, request
from model import *
from textblob import TextBlob

app = Flask(__name__)

@app.route("/", methods=["POST"])
def index(name=None):
    if request.method == 'POST':
        message = request.json['message']

        if len(message) < 3:
        	message += "   "
        if TextBlob(message).detect_language() in ["en", "fr"] :
        	return json.dumps({
		        "status": "error",
		        "messages": ["المرجو طرح الأسئلة المتعلقة بكورونا بالدارجة المغربية سواء بحروف عربية او لاتينية . سهم لازال تحت التطوير وسيتم اضافة اللغات الاخرى قريبا"]
		    })

        loaded_model = Net(message)
        result = loaded_model.main()
        return result