from __init__ import collection,index_path,alert_now
from PIL import Image
import io

def news_load_index(n:int=3)->tuple:
    sorted_documents = collection.find().sort('time',-1)

    _announce = tuple()
    for i in range(n):
        _announce+=(sorted_documents[i]['title'],)
        image =collection.find_one({"time":sorted_documents[i]['time']})
        pil_img = Image.open(io.BytesIO(image['img']))
        pil_img.save(f"{index_path}/static/img/announcement/time_a.png")
    print(_announce)
    return _announce


def alert_show()->dict:
    if alert_now:
        return alert_now
    return None