from flask import Flask, render_template
import os
import pymongo

MONGODB_URI = 'mongodb+srv://antonfebianto574:30python@30daysofpython.qiah5b8.mongodb.net/?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
db = client['belajar_python']
m_siswa = [
    {'name':'Elphin','country':'Indonesia','city':'Tulungagung','age':27},
    {'name':'Lee Dong Wok','country':'Korea Selatan','city':'Gangnam','age':33},
    {'name':'Xu Pat Xai','country':'Tiongkok','city':'Pudong','age':200},
    {'name':'Stanford Raffles','country':'Belanda','city':'Amsterdam','age':40}
]
for i in m_siswa:
    db.m_siswa.insert_one(i)
app = Flask(__name__)
if __name__ == '__main__':
    port = int(os.environ.get("PORT",5000))
    app.run(debug=True, host='0.0.0.0', port=port)