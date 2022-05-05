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
    dbc.disp_internal()
    # dbc.save_composite_to_db(1, "Test.py search")
    # print("Loading composite 1's stuff before insert " + str(dbc.load_areas_from_composite(1)))
    # dict = {'testcoordNE[lat]': '37.8', 'testcoordNE[lng]': '-122.8', 'testcoordSW[lat]': '37.0', 'testcoordSW[lng]': '-122.0'}
    # dbc.save_area_to_db(dict)
    # print("Loading composite 1's stuff after insert: " + str(dbc.load_areas_from_composite(1)))
    # dbc.delete_composites_from_db(1)
    # print("Loading composite 1's stuff after delete: " + str(dbc.load_areas_from_composite(1)))

if __name__ == "__main__":
    main()



