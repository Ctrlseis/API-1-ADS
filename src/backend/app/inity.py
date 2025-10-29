from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
bcrypt = Bcrypt()

def create_app():
    app = Flask(_name_) # type: ignore

    # Configurações do banco de dados
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://usuario:senha@localhost/scrumdb'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'sua-chave-secreta-aqui'

    # Inicializa extensões
    db.init_app(app)
    bcrypt.init_app(app)

    # Importa e registra as rotas
    from app.routes.auth import auth_bp # type: ignore
    app.register_blueprint(auth_bp)

    return app