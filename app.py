import sqlite3
from ast import Slice
from re import S
from flask import Flask, request, jsonify, render_template, url_for, current_app, g
from flask.cli import with_appcontext
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

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
    app.run(debug=True)