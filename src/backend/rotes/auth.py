from flask import Blueprint, request, jsonify
from app import db, bcrypt
from app.models.user import User # type: ignore

auth_bp = Blueprint("auth", _name_) # type: ignore

@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.json

    # Verifica se o email já existe
    if User.query.filter_by(email=data["email"]).first():
        return jsonify({"message": "Este e-mail já está cadastrado."}), 400

    # Criptografa a senha
    senha_criptografada = bcrypt.generate_password_hash(data["senha"]).decode("utf-8")

    # Cria novo usuário
    novo_usuario = User(
        nome=data["nome"],
        email=data["email"],
        senha=senha_criptografada
    )

    db.session.add(novo_usuario)
    db.session.commit()

    return jsonify({"message": "Conta criada com sucesso!"}), 201

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json

    # Busca o usuário pelo email
    usuario = User.query.filter_by(email=data["email"]).first()

    # Verifica se o usuário existe e se a senha está correta
    if usuario and bcrypt.check_password_hash(usuario.senha, data["senha"]):
        return jsonify({"message": "Login bem-sucedido!"}), 200
    else:
        return jsonify({"message": "Email ou senha inválidos."}),401