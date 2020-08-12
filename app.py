from pymongo import MongoClient
from flask import Flask
from flask import jsonify
from flask import json
from flask import Response
from flask.json import JSONEncoder
from bson import json_util
from flask import request
from flask_cors import CORS


class CustomJSONEncoder(JSONEncoder):
    def default(self, obj): return json_util.default(obj)


app = Flask(__name__)
CORS(app)
app.json_encoder = CustomJSONEncoder


client = MongoClient(
    "mongodb://admin:admin123@192.168.18.92:27017/news-aggregator-v1?authSource=admin&readPreference=primary&appname=MongoDB%20Compass&ssl=false")

# Database Name
db = client["news-aggregator-v1"]

# Collection Name
news_article = db["news-article"]
news_project = db["news-project"]
news_source = db["news-source"]

# {'author': 'Mohammad Yaqoob'}
# {'name': 'Techavenue'}
# {'sourcename': 'pakistan-today'}


@app.route("/articles", methods=['GET'])
def article():
    articles = news_article.find(
        {
        'source': request.args['source']
    },
        {"_id": 1, "heading": 1, "source": 1,
            "news-link": 1, "news-date": 1, "timestamp": 1,"author":1,"sentiment-type":1}
    )
    json_docs = []
    for a in articles:
        json_docs.append(a)
    return jsonify(results=json_docs)


@app.route("/sources", methods=['GET'])
def source():
    sources = news_source.find({},{'sourcename':1,'_id':0})
    json_docs = []
    for s in sources:
        json_docs.append(s)
    return jsonify(results=json_docs)
