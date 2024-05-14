from flask import Blueprint, redirect, request, url_for
from src.models import Livreur, Plat, db

admin = Blueprint('admin', __name__)

@admin.route("/add_plat", methods=['POST'])
def add_plat():
    if request.method == 'POST':
        libelle = request.form.get("libelle")
        quantite = int(request.form.get("quantite"))
        description = request.form.get("description")
        prix = int(request.form.get("prix"))
        image_url = request.form.get("image_url")
        new_plat = Plat(libelle=libelle, quantite=quantite, description=description, prix=prix, image_url=image_url)
        db.session.add(new_plat)
        db.session.commit()
        return redirect(url_for('app.index'))

@admin.route("/update_plat", methods=['POST'])
def update_plat():
    if request.method == 'POST':
        plat_id = request.form.get("id")
        quantite = int(request.form.get("quantite"))
        prix = int(request.form.get("prix"))
        plat = Plat.query.get(plat_id)
        if plat:
            plat.quantite = quantite
            plat.prix = prix
            db.session.commit()
        return redirect(url_for('app.index'))

@admin.route("/delete_plat", methods=['POST'])
def delete_plat():
    if request.method == 'POST':
        plat_id = request.form.get("id")
        plat = Plat.query.get(plat_id)
        if plat:
            db.session.delete(plat)
            db.session.commit()
        return redirect(url_for('app.index'))

@admin.route("/refuse_livreur", methods=['POST'])
def refuse_livreur():
    if request.method == 'POST':
        livreur_id = request.form.get("id")
        livreur = Livreur.query.get(livreur_id)
        if livreur:
            db.session.delete(livreur)
            db.session.commit()
        return redirect(url_for('app.index'))

@admin.route("/end_commande", methods=['POST'])
def end_commande():
    if request.method == 'POST':
        commande_id = request.form.get("commande_id")
        # Ici, vous mettez à jour le statut de la commande dans la base de données
        return redirect(url_for('app.index'))