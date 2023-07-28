from flask import Flask, render_template
from news.newssystem import app_route as newssystem
from __init__ import client
from news.news_load import news_load_index
import pymongo
import os

app = Flask(__name__)
app.register_blueprint(newssystem)



@app.route('/')
def index():
    _announce = news_load_index()
    print(_announce)
    return render_template('index.html',a=_announce[0],b=_announce[1],c=_announce[2])

@app.route('/about_us')
def aboutus():
    return render_template('about_us.html')

@app.route('/work_with_us')
def rounded():
    return render_template('wantyou.html')

@app.route('/explainVtuber')
def explainVtuber():
    return render_template('whatv.html')

@app.errorhandler(404)
def erro404(e):
    return render_template('404.html'),404



if __name__=="__main__":
    print(client.list_database_names())
    app.run( port=5000,debug=True) #host='0.0.0.0'