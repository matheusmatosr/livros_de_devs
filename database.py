import pymongo

def conectar_mongo(mongo_url, db_name):
    cliente = pymongo.MongoClient(mongo_url)
    db = cliente[db_name]
    return cliente, db

def fechar_conexao(cliente):
    cliente.close()

def inserir_livros(db, catalogo_livros):
    db.livros.insert_many(catalogo_livros)