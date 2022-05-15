from flask import Flask, request, jsonify, render_template, url_for, current_app, g, redirect, flash
from DBClass import DBClass
import time

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    global dbc
    dbc =DBClass()
    return render_template('index 3.html')


@app.route('/contact')
def ex():
    return render_template('contact.html')


@app.route('/hi')
def hi():
    print('Hi!')
    return (''), 204


@app.route('/save', methods=['GET', 'POST'])
def save_area_to_db():
    print("saving to db")
    if request.method == 'POST':
        data2 = request.form.to_dict()
        dbc.save_area_to_db(data2)
    return ""


@app.route('/savecomposite', methods=['POST'])
def save_composite_search():
    if request.method == 'POST':
        name = request.form['name']
        print(name)
        if not name:
            flash('name needed')
        else:
            dbc.rename_composite_to_db(name)
    return "Saved composite to DB", 204

@app.route('/load', methods=['GET', 'POST'])
def load_areas_from_db(id):
    print("load called")
    return dbc.load_areas_from_composite()


@app.route('/delete', methods=['DELETE'])
def delete_areas_from_db():
    if request.method == 'DELETE':
        data1=  request.form.to_dict()
        print(data1)
        dbc.delete_area_from_db_coords(data1)
    return "complete"
        

@app.route('/deleteallshapes', methods=['DELETE'])
def delete_all_shapes():
    dbc.delete_all_areas_from_db()


@app.route('/test/tables', methods=['POST', 'GET'])
def tables():
    """ Function that sends output of search_querying of the composite area to the DataTable

    Returns:
        dict/json: Returns the data from shape_querying as a readable json file
    """
    start = time.time()
    data_to_send = dbc.composite_logic()
    print("Time to populate table = ", str(time.time() - start))
    return {"data": data_to_send}


@app.route('/test/searchtables', methods=['POST', 'GET'])
def searchtables():
    print("Search table setup")
    data_to_send = dbc.load_composites_from_user(0)
    return {"data": data_to_send}



if __name__ == "__main__":
    app.run(debug=True)
