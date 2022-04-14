from flask import Blueprint, request, flash, redirect, url_for, render_template, jsonify
from flask_login import current_user, login_required
from werkzeug.utils import secure_filename
from route.login import gerant_required
from utils.utils_check import *
from app import Suite, Gerant

suite_api = Blueprint('suite_api', __name__)


@suite_api.route("/ajout_suite", methods=['GET', 'POST'])
@login_required
@gerant_required
def suite_add():
    """ Renvoie le formulaire d'ajout d'une suite (GET), Envoie le formulaire (POST) """

    if request.method == 'POST':
        titre = request.form.get('titre').title()
        img = request.files['file']
        price = request.form.get('price')
        link = request.form.get('link')
        description = request.form.get('description')

        error = 0

        if not checkname(titre):
            flash('Titre de la suite invalide')
            error += 1

        if not checkurl(link):
            flash('Lien booking invalide (url)')
            error += 1

        floatprice = convertingfloat(price)

        if not floatprice:
            flash('Format du prix non valide')
            error += 1

        if not checkimg(img):
            flash("Le fichier n'est pas une image")
            error += 1

        if error:
            return redirect(url_for('suite_api.suite_add'))

        gerant_hotel = Gerant.select().where(Gerant.user == current_user.id).get_or_none()
        if gerant_hotel:
            try:
                img_name = secure_filename(img.filename)
                img.save(f"./static/img/uploads/{img_name}")
                print("img save")
                Suite.create(titre=titre, img=img_name, description=description, price=floatprice, link=link, hotel=gerant_hotel.hotel)

            except Exception:
                flash("Une erreur inconnue est survenue")
                return redirect(url_for('suite_api.suite_add'))

            return redirect(url_for('index_api.index_gerant'))

        else:
            flash('Compte gérant pas trouvée dans la base, vous n\'êtes pas connecté avec un compte gérant.')
            return redirect(url_for('suite_api.suite_add'), code=303)

    else:
        return render_template('gerant/suiteform.html', suite=None)


@suite_api.route("/api/suites")
@login_required
def get_suites():
    """ Renvoie la liste des suites d'un hotel """

    hotelid = request.args.get('hotelId')

    query = Suite.select().where(Suite.hotel == hotelid)

    if query.count() > 0:
        liste = []
        for suite in query:
            data = {}
            data['id'] = suite.id
            data['titre'] = suite.titre

            liste.append(data)

        return jsonify(liste)
    else:
        return "", 204
