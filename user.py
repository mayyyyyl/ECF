from flask import Blueprint, request, flash, redirect, url_for, render_template
from utils import *
from peewee import IntegrityError
from app import User

user_api = Blueprint('user_api', __name__)


@user_api.route("/créer_un_compte", methods=['GET', 'POST'])
def custumer_add():
    """ Renvoie le formulaire création d'un compte (GET), Envoie le formulaire (POST) """

    if request.method == 'POST':
        first = request.form.get('first').title()
        last = request.form.get('last').title()
        email = request.form.get('email')
        password = request.form.get('password')

        error = 0

        if not checkname(first):
            flash("Le prénom n'est pas valide")
            error += 1
        if not checkname(last):
            flash("Le nom de famille n'est pas valide")
            error += 1
        if not checkemailadress(email):
            flash("Email n'est pas valide")
            error += 1

        if not checkpassword(password):
            flash("Le mot de passe n'est pas valide")
            error += 1

        if error:
            return redirect(url_for('user_api.custumer_add'))

        hashed = hashingpassword(password)

        try:
            # Création du user
            User.create(firstname=first, lastname=last, password=hashed, email=email)

        except IntegrityError:
            flash("Adresse email déjà utilisée")
            return redirect(url_for('user_api.custumer_add'))

        except Exception:
            flash("Une erreur inconnue est survenue")
            return redirect(url_for('user_api.custumer_add'))

        else:
            return redirect(url_for('index_api.index'), code=303)

    else:
        return render_template('customerform.html')
