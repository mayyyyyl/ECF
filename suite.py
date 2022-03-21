from flask import Blueprint, request, flash, redirect, url_for, render_template
from flask_login import current_user, login_required
from login import gerant_required
from utils import *
from app import Suite, Gerant

suite_api = Blueprint('suite_api', __name__)


@suite_api.route("/ajout_suite", methods=['GET', 'POST'])
@login_required
@gerant_required
def suite_add():
    """ Renvoie le formulaire d'ajout d'une suite (GET), Envoie le formulaire (POST)"""

    if request.method == 'POST':
        titre = request.form.get('titre').title()
        img = request.form.get('img')
        price = request.form.get('price')
        link = request.form.get('link')
        description = request.form.get('description')

        error = 0

        if not checkname(titre):
            flash('Titre de la suite invalide')
            error += 1

        if not checkurl(link):
            flash('Lien booking (url) invalide')
            error += 1

        floatprice = convertingfloat(price)

        if not floatprice:
            flash('Format du prix non valide')
            error += 1

        if error:
            return redirect(url_for('suite_api.suite_add'))

        gerant_hotel = Gerant.select().where(Gerant.user == current_user.id).get_or_none()
        if gerant_hotel:
            try:
                Suite.create(titre=titre, img=img, description=description, price=floatprice, link=link, hotel=gerant_hotel.hotel)

            except Exception:
                flash("Une erreur inconnue est survenue")
                return redirect(url_for('suite_api.suite_add'))

            return redirect(url_for('index_api.index'))

        else:
            flash('Compte gérant pas trouvée dans la base')
            return redirect(url_for('suite_api.suite_add'), code=303)

    else:
        return render_template('suiteform.html', suite=None)
