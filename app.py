from flask import Flask, render_template, jsonify
import pandas as pd
from bson import json_util
import pymongo

app = Flask(__name__)

# Conexão com o MongoDB
mongo_url = 'mongodb://localhost:27017/'
db_name = 'web' 
cliente = pymongo.MongoClient(mongo_url)
db = cliente[db_name]

@app.route('/')
def index():
    livros = db.livros.find()  
    return render_template('index.html', data=livros)

# Rota para obter o JSON dos produtos 
@app.route('/produtos', methods=['GET'])
def obter_produtos():
    livros = list(db.livros.find())  
    return json_util.dumps(livros, default=str)  

if __name__ == '__main__':
    app.run(debug=True)