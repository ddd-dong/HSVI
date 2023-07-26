from flask import Flask, render_template
from news.newssystem import app_route as newssystem
from pymongo.mongo_client import MongoClient
import pymongo
import os
from PIL import Image
import io
app = Flask(__name__)
app.register_blueprint(newssystem)
url = "mongodb+srv://hsvi0919:Fx794j4sLWllGcho@hsvi.bquldrx.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(url,tls=True,tlsAllowInvalidCertificates=True)
db = client['hsvi']
collection = db['announcement']


@app.route('/')
def index():
    sorted_documents = collection.find().sort('time',-1)

    #ann1
    title1=sorted_documents[0]['title']
    image =collection.find_one({"time":sorted_documents[0]['time']})
    pil_img = Image.open(io.BytesIO(image['img']))
    pil_img.save("static/img/announcement/time_{}.png".format("first"))
    #ann2
    title2=sorted_documents[1]['title']
    image =collection.find_one({"time":sorted_documents[1]['time']})
    pil_img = Image.open(io.BytesIO(image['img']))
    pil_img.save("static/img/announcement/time_{}.png".format("second"))
    #ann3
    title3=sorted_documents[2]['title']
    image =collection.find_one({"time":sorted_documents[2]['time']})
    pil_img = Image.open(io.BytesIO(image['img']))
    pil_img.save("static/img/announcement/time_{}.png".format("third"))
    
    return render_template('index.html',a=title1,b=title2,c=title3)

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
    app.run(host='0.0.0.0', port=80,debug=True) #host='0.0.0.0'