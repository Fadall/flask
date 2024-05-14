from flask import Blueprint, flash, redirect, render_template, request, session, url_for
from src.models import Users, db

auth = Blueprint('auth', __name__)

@auth.route("/account", methods=['GET', 'POST'])
def account():
    if request.method == 'POST':
        prenom = request.form.get('prenom')
        nom = request.form.get('nom')
        telephone = request.form.get('telephone')
        password = request.form.get('password')
        confirmPassword = request.form.get('confirmPassword')
        if not prenom or not nom or not telephone or not password:
            flash('Veuillez remplir tous les champs', 'errorChamps')
            return render_template("form/account.html")
        if password != confirmPassword:
            flash("Les mots de passe ne correspondent pas", 'errorPassword')
            return render_template("form/account.html")
        if Users.query.filter_by(telephone=telephone).first():
            flash('Le numéro de téléphone est déjà utilisé', 'error')
            return render_template("form/account.html")
        new_user = Users(prenom=prenom, nom=nom, telephone=telephone, password=password)
        db.session.add(new_user)
        db.session.commit()
        flash('Votre compte a été créé avec succès', 'success')
        session['ConnectedUser'] = new_user.telephone
        session["role"] = new_user.role
        return redirect(url_for('index'))
    else:
        return render_template("form/account.html")
    

@auth.route("/login", methods=['GET', 'POST'])
def login():
    nom = session['nom']
    role = session.get('role', 1)
    if request.method == 'POST':
        telephone = request.form.get('telephone')
        password = request.form.get('password')
        user = Users.query.filter_by(telephone=telephone).first()
        if user:
            if user.password == password:
                session['ConnectedUser'] = user.telephone
                session["role"] = user.role
                return redirect(url_for('index'))
            else:
                flash('Mot de passe incorrect', 'password')
        else:
            flash('Numéro de téléphone incorrect', 'telephone')
    return render_template("form/login.html", nom=nom, role=role)

@auth.route("/logout")
def logout():
    if 'ConnectedUser' in session:
        session.pop('ConnectedUser')
        session.pop('role')
        return redirect(url_for("index"))
    return redirect(url_for("index"))