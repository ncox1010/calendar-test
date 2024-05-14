from flask import Flask # type: ignore
import flask
import json
import csv
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route('/Sampledata', methods=["GET"])
def Sampledata():
    with open('Sampledata.csv', 'r') as file:
        reader = csv.reader(file)
        data = list(reader)  # Read all rows and store them in a list
        return flask.jsonify(data)
    
@app.route('/Parserfile', methods=["GET"])
def Parsefile():
    with open('Parserfile.csv', 'r') as file:
        reader = csv.reader(file)
        data = list(reader)  # Read all rows and store them in a list
        return flask.jsonify(data)

if __name__ == "__main__":
    app.run("localhost", 6969)