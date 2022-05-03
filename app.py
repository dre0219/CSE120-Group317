from curses import tparm
from operator import length_hint
import sqlite3
from flask import Flask, request, jsonify, render_template, url_for, current_app, g, redirect
from flask.cli import with_appcontext
from flask_sqlalchemy import SQLAlchemy
from DBClass import DBClass 




app = Flask(__name__)
dbc = DBClass()


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index 3.html')


@app.route('/contact')
def ex():
    return render_template('contact.html')


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

@app.route('/deleteallshapes', methods=['DELETE'])
def delete_all_shapes():
    dbc.delete_all_areas_from_db()
    dbc.coordinate_array = []


@app.route('/test/tables', methods = ['POST', 'GET'])
def tables():
    """ Function that sends output of search_querying of the composite area to the DataTable
    Returns:
        dict/json: Returns the data from shape_querying as a readable json file
    """
    data_to_send = dbc.composite_logic()
    return {"data": data_to_send}

@app.route('/test/searchtables', methods = ['POST', 'GET'])
def searchtables():
    print("Search table setup")
    data_to_send = dbc.load_composites_from_user(0)
    return {"data": data_to_send}

   
if __name__ == "__main__":
    app.run(debug=True)