from contextlib import redirect_stderr
from curses import tparm
import sqlite3
from ast import Slice
from re import S
from flask import Flask, request, jsonify, render_template, url_for, current_app, g, redirect
from flask.cli import with_appcontext
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_restful import Api, Resource, reqparse
import json

app = Flask(__name__)
api = Api(app)
CORS(app)

# parser = reqparse.RequestParser()
# parser.add_argument('list', type = list)

area_id = 0 
coordinates = []
@app.route('/', methods=['GET', 'POST'])
def index():
    connection = get_db_connect()
    cursor = connection.cursor()
    cursor.execute('''pragma foreign_keys = ON''')
    connection.commit()
    return render_template('index 3.html')


def get_db_connect():
    connection = None
    try:
        connection = sqlite3.connect("sf_food_program_db_project_ver.sqlite")
    except sqlite3.error as e:
        print(e)
    return connection


@app.route('/save', methods=['POST'])
def save_area_to_db():
    print("saving to db")
    global area_id
    global coordinates
    if request.method == 'POST':
        data = request.form.to_dict()
        connection = get_db_connect()
        cursor = connection.cursor()
        cursor.execute('''pragma foreign_keys = ON''')
        connection.commit()
        latitude1 = data['testcoordNE[lat]']    #assign to latitude1
        longitude1 = data['testcoordNE[lng]']   #assign to longitude1
        latitude2 = data['testcoordSW[lat]']    #assign to latitude2
        longitude2 = data['testcoordSW[lng]']   #assign to longitude2
        composite_id = 0
        # cursor.execute('''INSERT INTO areas(area_id, latitude1, longitude1, latitude2, longitude2, composite_id) VALUES(?,?,?,?,?,?)
        #                 ''', (area_id, latitude1, longitude1, latitude2, longitude2, composite_id))
        area_id += 1
        composite_id += 0
        connection.commit()
        coordinates = {"lat1": latitude1, "long1": longitude1, "lat2": latitude2, "long2":longitude2}
        print(coordinates)
    return ""

@app.route('/save', methods=['POST'])
def save_composite_to_db(composite_id, name):
    print("saving to db")
    if request.method == 'POST':
        data = request.form.to_dict()
        connection = get_db_connect()
        cursor = connection.cursor()
        cursor.execute('''pragma foreign_keys = ON''')
        connection.commit()
        cursor.execute('''INSERT INTO areas(composite_id, composite_name, user_id) VALUES(?,?,?)
                         ''', (composite_id, name, composite_id))
        composite_id += 1
        connection.commit()
    return ""

def load_areas_from_composite(composite_id):
    connection = get_db_connect()
    cursor = connection.cursor()
    cursor.execute('''pragma foreign_keys = ON''')
    connection.commit()
    cursor.execute('''SELECT * FROM AREAS WHERE composite_id = ?''', (composite_id, name, composite_id))
    connection.commit()

@app.route('/delete/<int:id>', methods=['DELETE'])
def delete_area_from_db(id):
    connection = get_db_connect()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM areas WHERE area_id = ?", (id,))
    connection.commit()


def access_most_recent_area():
    print("most recent composite")
    connection = get_db_connect()
    cursor = connection.cursor()
    cursor.execute('''SELECT * FROM areas WHERE area_id = (SELECT MAX(area_id) FROM areas)''')
    area = cursor.fetchone()
    # area = dict(area_id = row[0], lat1 = row[1], long1 = row[2], lat2 = row[3], long2 = row[4], composite_id = row[5]) 
    print(area)
    return area

def access_most_recent_composite():
    print("most recent composite")
    connection = get_db_connect()
    cursor = connection.cursor()
    cursor.execute('''SELECT * FROM composites WHERE composite_id = (SELECT MAX(composite_id) FROM composites)''')
    composites = cursor.fetchone()
    # area = dict(area_id = row[0], lat1 = row[1], long1 = row[2], lat2 = row[3], long2 = row[4], composite_id = row[5]) 
    print(composites)
    return composites    

def shape_querying(latestcoords):
    connection = get_db_connect()
    connection.row_factory = dict_factory
    cursor = connection.cursor()


    cursor.execute('''
    SELECT *
    FROM businesses
    WHERE latitude < ? AND latitude > ? AND longitude > ? AND longitude < ?
    ''', (latestcoords["lat1"],latestcoords["lat2"], latestcoords["long2"], latestcoords["long1"]))

    # # latitude of rectangle is less than the top left y (latitude decreases southward from positive value in northern hemisphere), 
    # # and greater than bottom right's y (going northwards increases latitude)
    # # longitude of rectangle is less than the bottom right's x (longitude increases eastward from negative value in western hemisphere)
    # # and greater than top left's x (longitude decreases westward in western hemisphere)
    places = [[]]
    # for row in cursor.fetchall():
    #     print(str(row[1]) + ", " + str(row[2]) + ", " + str(row[3]) + ", " + str(row[4]) + ", " + str(row[5]) + ", " + str(row[6]))
    #     places.append([str(row[1]),str(row[2]),str(row[3]),str(row[4])])
    
    output_data = cursor.fetchall()
    print(output_data)


    print(">>>>>> Shape Querying Functions")
    return output_data


def dict_factory(cursor, row):
    return dict((cursor.description[idx][0], value)
                for idx, value in enumerate(row))

    

# @app.route('/test/tables/', methods = ['POST', 'GET'])
# def tables():
#     global coordinates
#     if request.method == 'POST':
#         data_to_send = shape_querying(coordinates)
#         print(data_to_send)
#         # DataParser = parser.parse_args()
#         print(">>>>>> Sending data backk to datatable")
#         return jsonify({'data':data_to_send})


@app.route('/test/tables', methods = ['POST', 'GET'])
def tables():
    global coordinates
    data_to_send = shape_querying(coordinates)
    print(data_to_send)
    return {"data": data_to_send}

# @app.route('/test/tables')
# def data():
#     return {'data':[{'name': 'Jowi', 'age':100000, 'address': 'Earth', 'phone': 9120132210, "email": 'jasaras@asdas.com'}]}


if __name__ == "__main__":
    app.run(debug=True)