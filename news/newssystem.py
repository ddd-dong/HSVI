from flask import Blueprint, render_template, jsonify,redirect
from pymongo.mongo_client import MongoClient
import pymongo
import os
from PIL import Image
import io
app_route = Blueprint('newssystem', __name__, static_folder='static', static_url_path='/static')

# MongoDB connection setup
url = "mongodb+srv://hsvi0919:<password>@hsvi.bquldrx.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(url,tls=True,tlsAllowInvalidCertificates=True)
db = client['hsvi']
collection = db['announcement']


@app_route.route("/catch_announcement")
def catch_announcement():
    pass
