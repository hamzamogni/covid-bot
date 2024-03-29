from flask import Flask, request, jsonify
from model import *
from Crawler import Crawler

from textblob import TextBlob
import textblob
import string



app = Flask(__name__)

@app.route("/", methods=["POST"])
def index(name=None):
    if request.method == 'POST':
        message = request.json['message']
        message = message.translate(str.maketrans(" ", " ", string.punctuation + "؟"))

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


@app.route("/crawler", methods=["GET"])
def crawl(name=None):
    if request.method == 'GET':
        country = request.args.get('country')
        if country == None:
            return jsonify({"error": "invalid query parameters"})
        
        try:
            if country == "المغرب":
                country = "Morocco"
            else:
                country = str(TextBlob(country).translate(to="en"))
        except textblob.exceptions.NotTranslated:
            pass
        
        if len(country) < 4:
            country = country.upper()
        else:
            country = country.title()
        
        print(country)
        crawler = Crawler()
        response = crawler.run(country)
        return jsonify(response)