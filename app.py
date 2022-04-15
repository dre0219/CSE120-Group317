import sqlite3
from ast import Slice
from re import S
from flask import Flask, request, jsonify, render_template, url_for, current_app, g
from flask.cli import with_appcontext
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/data', methods=['GET', 'POST'])
def data():
    con = get_db_connect()
    cur = con.cursor()
    datas = {'data':[]}
    cur.execute('SELECT * FROM businesses2')
    for row in cur.fetchall():
        output = {
            'name': row[1],
            'address': row[2],
            'city': row[3],
            'postal_code': row[4],
            'latitude': row[5],
            'longitude': row[6]
        }
        datas['data'].append(output)
    
    return datas

@app.route('/places', methods=['GET', 'POST'])
def places():
    connection = get_db_connect()
    cursor = connection.cursor()
    if request.method == 'GET':
        cursor = connection.execute("SELECT * FROM businesses2")
        businesses = [
            dict(id = row[0], name = row[1], address = row[2], city = row[3], postal_code = row[4], latitude = row[5], longitude = row[6])
            for row in cursor.fetchall()
        ]
        #businesses = cursor.fetchall()
        if businesses is not None:
            return jsonify(businesses)
    if request.method == 'POST':
        name = request.form['name']
        addr = request.form['address']
        city = request.form['city']
        p_code = request.form['postal_code']
        lat = request.form['latitude']
        long = request.form['longitude']
        sql = """INSERT INTO businesses2 (name, address, city, postal_code, latitude, longitude) VALUES (?,?,?,?,?,?)"""
        cursor = connection.execute(sql, (name, addr,city,p_code,lat,long))
        connection.commit()
        return f"Place w/ id: {cursor.lastrowid} created successfully"



@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index 3.html')

def get_db_connect():
    connection = None
    try:
        connection = sqlite3.connect("sf_food_program_db_project_ver.sqlite")
    except sqlite3.error as e:
        print(e)
    return connection

@app.route('/shape_querying', methods=['GET', 'POST'])
def shape_querying():
    if request.method == 'POST':
        #data = request.form['data']
        #print(data)
        data2 = request.form.to_dict()
        print(data2)
        print(data2['testcoordNE[lat]'])
        print(data2['testcoordNE[lng]'])
        print(data2['testcoordSW[lat]'])
        print(data2['testcoordSW[lng]'])

        connection = get_db_connect()
        cursor = connection.cursor()

        # cursor.execute('''
        # SELECT *
        # FROM businesses2
        # WHERE latitude < ? AND latitude > ? AND longitude > ? AND longitude < ?
        # ''', (coordinfo[0], coordinfo[1], coordinfo[2], coordinfo[3]))

        cursor.execute('''
        SELECT *
        FROM businesses2
        WHERE latitude < ? AND latitude > ? AND longitude > ? AND longitude < ?
        ''', (data2['testcoordNE[lat]'], data2['testcoordSW[lat]'], data2['testcoordSW[lng]'], data2['testcoordNE[lng]']))

        # # latitude of rectangle is less than the top left y (latitude decreases southward from positive value in northern hemisphere), 
        # # and greater than bottom right's y (going northwards increases latitude)
        # # longitude of rectangle is less than the bottom right's x (longitude increases eastward from negative value in western hemisphere)
        # # and greater than top left's x (longitude decreases westward in western hemisphere)
        places = [[]]
        for row in cursor.fetchall():
            print(str(row[1]) + ", " + str(row[2]) + ", " + str(row[3]) + ", " + str(row[4]) + ", " + str(row[5]) + ", " + str(row[6]))
            places.append([str(row[1]),str(row[2]),str(row[3]),str(row[4])])
        
        return ""
    return ""

@app.route('/<name>')
def print_name(name):
    return "Hi, {}". format(name)


@app.route('/place/<int:id>', methods=['GET', 'PUT', 'DELETE'])         
def singleplace(id):
    connection = get_db_connect()
    cursor = connection.cursor()
    place = None
    if request.method == 'GET':
        cursor.execute("SELECT * FROM businesses2 WHERE business_id=?", (id,))
        rows = cursor.fetchall()
        for row in rows:
            place = row
        if place is not None:
            return jsonify(place), 200
        else:
            return "Error", 404
    
    if request.method == "PUT":
        query = """UPDATE businesses2
                SET name = ?,
                    address =?,
                    city = ?,
                    postal_code = ?,
                    latitude = ?,
                    longitude = ?
                    WHERE business_id = ? """
        name = request.form['name']
        addr = request.form['address']
        city = request.form['city']
        p_code = request.form['postal_code']
        lat = request.form['latitude']
        long = request.form['longitude']
        updated_place = {
            "id": id,
            "name": name,
            "address": addr,
            "city": city,
            "postal_code": p_code,
            "latitude": lat,
            "longitude": long,
        }
        connection.execute(query, (name, addr, city, p_code, lat, long, id))
        connection.commit()
        return jsonify(updated_place)

    if request.method == "DELETE":
        query = """DELETE FROM businesses2 WHERE business_id = ? """
        connection.execute(query, (id,))
        connection.commit()
        return "Place w/ id: {} has been deleted".format(id), 200

if __name__ == "__main__":
    app.run(debug=False)