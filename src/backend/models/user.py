from app import db

class User (db.model):
    __tablename__ = 'Usuários'

id = db.columm(db.integer, primary_key = True)
nome = db.collumm(db.string(150), nullable = False)
email = db.collum(db.string(150), unique = True, nullable = False)
senha = db.collum(db.string(200), nullable = False)