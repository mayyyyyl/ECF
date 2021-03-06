from flask import Blueprint, request, flash, redirect, url_for, render_template
from flask_login import login_user, logout_user, current_user
from utils.utils_check import hashingpassword
from app import Gerant, User, login_manager
from functools import wraps

login_api = Blueprint('login_api', __name__)


@login_api.route("/login", methods=['GET', 'POST'])
def login():
    """ Renvoie la vue login (GET), Envoie du formulaire de login (POST) """

    if request.method == 'POST':

        email = request.form.get('email', '')
        mdp = request.form.get('mdp', '')

        if email == '' or mdp == '':
            flash('Email ou mot de passe erroné')
            return redirect(url_for('login_api.login'))

        hashed = hashingpassword(mdp)

        # test mail et mdp en une requête
        user = User.get_or_none(User.email == email, User.password == hashed)

        if user is None:
            flash('Email ou mot de passe erroné')
            return redirect(url_for('login_api.login'))

        else:
            # on démarre la session utilisateur
            if login_user(user):
                gerant = Gerant.get_or_none(Gerant.user == user.id)
                if gerant:
                    nextroute = request.args.get('next', '/gerant')
                    return redirect(nextroute, code=303)
                else:
                    nextroute = request.args.get('next', '/')
                    return redirect(nextroute, code=303)

            else:
                flash('Email ou mot de passe erroné')
                return redirect(url_for('login_api.login'))

    else:
        return render_template("login.html", title="Connexion")


@login_api.route("/logout")
def logout():
    """ Déconnecte le user """

    logout_user()
    return redirect(url_for('index_api.index'))


@login_manager.user_loader
def load_user(user_id):
    """ Test userid existe en bd """

    return User.get_or_none(User.id == user_id)


def gerant_required(view):
    @wraps(view)
    def wrapped_view(**kwargs):
        """ Vérifie user connecté est un gerant """

        isgerant = Gerant.select().where(Gerant.user == current_user.id).get_or_none()

        if isgerant is None:
            flash('Vous devez être connecté en tant que gérant')
            return redirect(url_for('login_api.login'))

        return view(**kwargs)

    return wrapped_view
