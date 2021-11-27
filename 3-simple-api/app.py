########################################################################
# Simple API example
#
# This script was written for the Victoria Raspberry PiMakers And Others
# Meetup Group presentation on November 27, 2021.
#
# Gordon M. Celesta
# gordo@sdf.lonestar.org
#
# FURTHER READING
#
# API
# https://en.wikipedia.org/wiki/API
#
# JSON
# https://en.wikipedia.org/wiki/JSON
#
# cURL
# https://en.wikipedia.org/wiki/CURL
#
# Flask-RESTful extension
# https://flask-restful.readthedocs.io/
#
########################################################################

import random
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/pond-temp", methods=['GET'])
def get_pond_temp():
    """
    Return JSON data containing random water temperature in Fahrenheit
    between 35 °F and 85 °F (the survivable range for koi fish) and its
    equivalent in celsius

    Example using cURL
    curl http://the-demo.website:5000/pond-temp
    """
    temp_f = round(random.uniform(35,85),1)
    temp_c = round((temp_f - 32) / 1.8, 1)
    return jsonify({'fahrenheit': temp_f, 'celsius': temp_c })

@app.route("/pond-temp", methods=['POST'])
def set_pond_temp():
    """"
    Demonstrate receiving JSON data

    Example using cURL
    curl -X POST -H "Content-Type: application/json" -d '{ "farenheit_min" : 40, "farenheight_max" : 75 }' http://the-demo.website:5000/pond-temp
    """
    print(request.get_json())
    return '', 204

if __name__ == "__main__":
    app.run(host='::')
