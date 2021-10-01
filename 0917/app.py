from flask import Flask, render_template, jsonify, request
from datetime import datetime

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbStock
@app.route('/')
def home():
   return render_template('index.html')

@app.route('/base/codes', methods=['GET'])
def group():
    groups= list(db.codes.distinct('group'))
    return jsonify(groups)

@app.route('/codes', methods=['GET'])
def code():
    group_receive=request.args.get('group')
    groups= list(db.codes.find({'group':group_receive},{'_id':False}))
    return jsonify(groups)


@app.route('/result', methods=['POST'])
def result():
    print('hi')
    market=request.form['market']
    sector=request.form['sector']
    tag=request.form['tag']
    result= list(db.stocks.find({'market':market, 'sector':sector, 'tag':tag},{'_id':False}))
    print(result)
    return jsonify({'msg':market})



@app.route('/stock', methods = ['POST'])
def stock():
    group = request.form['group']
    print(group)
    stocks = list(db.codes.find({'group':group}, {'_id' : False}))
    print(stocks)
    return jsonify({'msg':stocks})


if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)