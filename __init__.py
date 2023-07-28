from pymongo.mongo_client import MongoClient
import os
from dotenv import load_dotenv
index_path =  os.path.dirname(os.path.abspath(__file__))

load_dotenv(index_path+"/tst.env")

print(os.getenv("password"),os.getenv('token'))

url = f"mongodb+srv://hsvi0919:Fx794j4sLWllGcho@hsvi.bquldrx.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(url,tls=True,tlsAllowInvalidCertificates=True)
db = client['hsvi']
collection = db['announcement']