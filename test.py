<<<<<<< HEAD
from curses import tparm
from operator import length_hint
from flask import Flask, request, jsonify, render_template, url_for, current_app, g, redirect
from flask.cli import with_appcontext
from flask_sqlalchemy import SQLAlchemy
from DBClass import DBClass 




app = Flask(__name__)
dbc = DBClass()


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index 3.html')


@app.route('/save', methods=['GET','POST'])
def save_area_to_db():
    print("saving to db")
    if request.method == 'POST':
        data2 = request.form.to_dict()
        dbc.save_area_to_db(data2)
    return ""


@app.route('/load', methods = ['GET', 'POST'])
def load_areas_from_db(id):
    return dbc.load_areas_from_composite()    
    
    
@app.route('/delete/<int:id>', methods=['DELETE'])
def delete_composites_from_db(id):
    dbc.delete_composites_from_db(id)


@app.route('/test/tables', methods = ['POST', 'GET'])
def tables():
    """ Function that sends output of search_querying of the composite area to the DataTable

    Returns:
        dict/json: Returns the data from shape_querying as a readable json file
    """
    
    # data_to_send = shape_querying(coordinates)
    data_to_send = dbc.composite_logic()
    return {"data": data_to_send}





    
if __name__ == "__main__":
    app.run(debug=True)
    
=======
from contextlib import redirect_stderr
import sqlite3
from ast import Slice
from re import S
from flask import Flask, request, jsonify, render_template, url_for, current_app, g, redirect
from flask.cli import with_appcontext
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_restful import Api, Resource, reqparse
from DBClass import DBClass 
import json

# app = Flask(__name__)
# api = Api(app)
# CORS(app)
dbc = DBClass()

def main():
    print("test")
    print(dbc.load_areas_from_composite(0))
    dbc.delete_area_from_db(7)
    print(dbc.load_areas_from_composite(0))
    dbc.save_composite_to_db(1, "Test.py search")
    print("Loading composite 1's stuff before insert " + str(dbc.load_areas_from_composite(1)))
    dict = {'testcoordNE[lat]': '37.8', 'testcoordNE[lng]': '-122.8', 'testcoordSW[lat]': '37.0', 'testcoordSW[lng]': '-122.0'}
    dbc.save_area_to_db(dict)
    print("Loading composite 1's stuff after insert: " + str(dbc.load_areas_from_composite(1)))
    dbc.delete_composites_from_db(1)
    print("Loading composite 1's stuff after delete: " + str(dbc.load_areas_from_composite(1)))

if __name__ == "__main__":
    main()



>>>>>>> 79020d0d76897e70bb5b1bf44f832da20f1451ef
