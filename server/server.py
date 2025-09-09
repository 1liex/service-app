from flask import Flask
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)


#====== Functions ======

def open_files(path, resource_id = None):

    with open(path, "r") as f:
        data = json.load(f)     
        return data

@app.route("/<name>")
def hello(name):
    if name == "student":
        gg = open_files("server/data/Keywords.json")
        return gg
    elif name == "s":
        return "hh"


if __name__ == "__main__":
    app.run(debug=True)