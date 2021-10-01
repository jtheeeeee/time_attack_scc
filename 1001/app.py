import datetime

from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient
from datetime import datetime
app = Flask(__name__)

client = MongoClient("mongodb://localhost:27017/")
db = client.dbStock


@app.route('/')
def index() :
    return render_template('index.html')


@app.route('/post', methods=['POST'])
def save_post() :
    if len(list(db.contents.find({}))) > 0:
        idx = list(db.contents.find({}))[-1]['idx']+1
    else:
        idx=1
    title = request.form['title']
    content=request.form['content']
    doc={'idx':idx, 'title':title, 'content':content, 'reg_date':datetime.now() }
    db.contents.insert_one(doc)
    print(doc)
    return {"result" : "success"}


@app.route('/post', methods=['GET'])
def get_post() :
    datas = list(db.contents.find({}))
    print(datas)
    return {'result':datas}


@app.route('/post', methods=['DELETE'])
def delete_post() :
    idx = request.form['id_give']
    db.contentss.delete_one({'id' : int(idx)})
    return {"result" : "success"}


if __name__ == "__main__" :
    app.run(host="0.0.0.0", port=5000)