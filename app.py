import random
from flask import Flask, flash, render_template, redirect, request, session, url_for
from auth import auth
from src.models import Commande, Livreur, Panier, Plat, db,Users

app = Flask(__name__)
app.config['SECRET_KEY'] = 'FADAL'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///aloneur.db' 
db.init_app(app)

app.register_blueprint(auth)

@app.before_request
def before_request():
    session['nom'] = 'Se connecter'
    if 'ConnectedUser' in session:
        user = Users.query.filter_by(telephone=session['ConnectedUser']).first()
        if user:
            session['nom'] = user.prenom

@app.route("/")
@app.route("/index")
def index():
    nom = session.get('nom','Se connecter')
    role = session.get("role",1)
    plats_from_db = Plat.query.all()
    plats = [{"image_url":plat.image_url}for plat in plats_from_db] 
    return render_template("layout/index.html", nom=nom, role=role, plats=plats_from_db)

@app.route("/rechercher")
def rechercher_plat():
    nom = session.get('nom','Se connecter')
    if request.method == 'POST':
        recherche = request.form.get('recherche')
        plats = Plat.query.filter(Plat.libelle.startswith(recherche)).all()
        return render_template("recherche.html", plats=plats, recherche=recherche, nom=nom)
    else:
        return redirect(url_for('index'))

@app.route("/parcourir")
def plats():
    nom = session.get('nom', 'Se connecter')
    plats_from_db = Plat.query.all()
    plats = [
        {"libelle":plat.libelle, "image_url": plat.image_url, "quantite": plat.quantite, "description": plat.description} for plat in plats_from_db
    ]
    return render_template("layout/nos_plats.html", plats=plats, nom=nom)

@app.route("/tracking")
def menu():
    nom = session.get('nom','Se connecter')
    role = session.get("role",1)
    if 'ConnectedUser' in session:
        return render_template("menu/tracking.html", nom=nom, role=role)
    return redirect(url_for('auth.login'))

@app.route("/compte")
def compte():
    if 'ConnectedUser' in session:
        user_id=session.get('ConnectedUser')
        nom = session.get('nom','Se connecter')
        users = Users.query.all()
        return render_template("menu/compte.html", nom=nom, users=users)
    return redirect(url_for('auth.login'))

@app.route("/panier")
def panier():
    nom = session.get('nom','Se connecter')
    if 'ConnectedUser' in session:
        client = session['ConnectedUser']
        commandes_recentes = Commande.query.filter_by(client=client).all()
        panier = Panier.query.filter_by(client=client).all()
        plats = Plat.query.all()
        plats_au_hasard = random.sample(plats, k=len(plats)//2)
        return render_template("menu/panier.html", nom=nom, commandes_recentes=commandes_recentes, panier=panier, plats_au_hasard=plats_au_hasard)
    return redirect(url_for('auth.login'))

@app.route('/add_commande', methods=['POST'])
def add_commande():
    if request.method == 'POST':
        etat = request.form.get("etat")
        livreur = random.choice(Livreur.query.all())
        livreur_nom = livreur.prenom + ' ' + livreur.nom
        plat_nom = request.form.get("platNom")
        quantite = int(request.form.get("quantite"))
        if 'ConnectedUser' in session:
            client = session['ConnectedUser']
            plat = Plat.query.filter_by(libelle=plat_nom).first()
            if plat:
                if plat.quantite >= quantite:
                    plat.quantite -= quantite
                    new_comm = Commande(etat=etat, client=client, livreur=livreur_nom, plat=plat_nom, quantite=quantite)
                    db.session.add(new_comm)
                    db.session.commit()
                    panier = Panier.query.filter_by(client=client, plat=plat_nom).first()
                    if panier:
                        panier.quantite -= quantite
                        db.session.commit()
                    return redirect(url_for('panier'))
                flash("La quantité commandée n'est pas disponible.")
                return redirect(url_for('panier'))
            else:
                flash("Plat non trouvé.")
                return redirect(url_for('panier'))
        return redirect(url_for('auth.login'))

@app.route("/add_livreur", methods=['POST'])
def add_livreur():
    if request.method == 'POST':
        prenom = request.form.get("prenom")
        nom = request.form.get("nom")
        telephone = int(request.form.get("telephone"))
        new_livreur = Livreur(prenom=prenom, nom=nom, telephone=telephone)
        db.session.add(new_livreur)
        db.session.commit()
        return redirect(url_for('index'))

@app.route('/add_panier', methods=['POST'])
def add_panier():
    if request.method == 'POST':
        plat = request.form.get("platNom")
        if 'ConnectedUser' in session:
            client = session['ConnectedUser']
            new_panier = Panier(client=client,plat=plat)
            db.session.add(new_panier)
            db.session.commit()
            return redirect(url_for('index'))
        return redirect(url_for("plats"))

