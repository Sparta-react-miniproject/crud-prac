from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
import certifi
ca = certifi.where()
client = MongoClient('mongodb+srv://test:sparta@cluster0.aewa2iq.mongodb.net/Cluster0?retryWrites=true&w=majority', tlsCAFile=ca)
db = client.dbsparta


@app.route('/')
def home():
    return render_template('index.html')


@app.route("/crud", methods=["POST"])
def crud_post():
    first_receive = request.form['First_give']
    last_receive = request.form['Last_give']

    crud_list = list(db.crud.find({}, {'_id': False}))
    count = len(crud_list) + 1

    doc = {
        'num': count,
        'First': first_receive,
        'Last': last_receive
    }
    db.crud.insert_one(doc)

    return jsonify({'msg':'등록 완료'})


@app.route("/crud/delete", methods=["POST"])
def crud_delete():
    num_receive = request.form['num_give']
    db.crud.delete_one({'num': int(num_receive)})
    return jsonify({'msg': '삭제 완료!'})


@app.route("/crud", methods=["GET"])
def crud_get():
    crud_list = list(db.crud.find({}, {'_id': False}))
    return jsonify({'names': crud_list})

if __name__ == '__main__':
   app.run('0.0.0.0', port=5050, debug=True)