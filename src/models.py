from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    role = db.Column(db.Integer, nullable=False, default=1)
    prenom = db.Column(db.String(50), nullable=False)
    nom = db.Column(db.String(50), nullable=False)
    telephone = db.Column(db.Integer, nullable=False, unique=True)
    password = db.Column(db.String(50), nullable=False)
    user_img = db.Column(db.String(255), nullable=True)

class Plat(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    libelle = db.Column(db.String(50), nullable=False, unique=True)
    quantite = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text, nullable=True)
    prix = db.Column(db.Integer, nullable=False)
    image_url = db.Column(db.String(255), nullable=False)

class Commande(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    etat = db.Column(db.Integer, nullable=False, default=1)
    client = db.Column(db.String(50), nullable=False)
    livreur = db.Column(db.String(50), nullable=False)
    plat = db.Column(db.String(), nullable=False)
    quantite = db.Column(db.Integer, nullable=False)

class Panier(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    image_url = db.Column(db.String(255), nullable=False)
    client = db.Column(db.String(50), nullable=False)
    plat = db.Column(db.String(), nullable=False)
    quantite = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text, nullable=False)

class Livreur(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    prenom = db.Column(db.String(50), nullable=False)
    nom = db.Column(db.String(50), nullable=False)
    telephone = db.Column(db.Integer, nullable=False, unique=True)