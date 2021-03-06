from flask import Blueprint, abort, request, render_template, flash, jsonify, redirect, url_for
from flask_login import current_user, login_required
from app import Hotel, Reservation, Suite
from datetime import datetime
from utils.utils_date import *
from app import csrf

reservation_api = Blueprint('reservation_api', __name__)


@reservation_api.route("/reservation", methods=['GET', 'POST'])
@login_required
def reservation():
    """ Renvoie le formulaire pour reserver (GET), Envoie le formulaire (POST)"""

    # fonction anonyme qui formate la date au format datetimelocal
    str_to_datetime = lambda x: datetime.strptime(x, "%Y-%m-%d")

    if request.method == 'POST':

        suite = request.form.get('suiteIdSelected')
        start = str_to_datetime(request.form.get('start'))
        end = str_to_datetime(request.form.get('end'))

        if current_user is None:
            flash("Compte client inexistant")
            return redirect(url_for('index_api.index'))

        tests = []

        tests.append(valideperiod(start, end))
        tests.append(periodlength(start, end))
        tests.append(pastperiod(start, end))
        tests.append(overlapperiod(suite, start))
        tests.append(overlapperiod(suite, end))

        if not all(tests):
            flash("Une erreur inconnue est survenue")
            return redirect(url_for('reservation_api.reservation'))

        else:
            try:
                Reservation.create(suite=suite, customer=current_user.id, datebeginning=start, dateend=end)
            except Exception:
                flash("Une erreur inconnue est survenue")
                return redirect(url_for('reservation_api.reservation'))
            return redirect(url_for('history_api.customer_reservations'))
    else:

        hotels = Hotel.select()
        return render_template("reservation.html", hotels=hotels, suiteid=None, nexturl=None)


@reservation_api.route("/reserver", methods=['GET', 'POST'])
@login_required
def reservation_prefilled():
    """ Renvoie le formulaire pour reserver (GET), Envoie le formulaire (POST)"""

    # fonction anonyme qui formate la date au format datetimelocal
    str_to_datetime = lambda x: datetime.strptime(x, "%Y-%m-%d")

    if request.method == 'POST':

        suite = request.form.get('suiteIdSelected')
        start = str_to_datetime(request.form.get('start'))
        end = str_to_datetime(request.form.get('end'))

        if current_user is None:
            flash("Compte client inexistant")
            return redirect(url_for('index_api.index'))

        tests = []

        tests.append(valideperiod(start, end))
        tests.append(periodlength(start, end))
        tests.append(pastperiod(start, end))
        tests.append(overlapperiod(suite, start))
        tests.append(overlapperiod(suite, end))

        if not all(tests):
            flash("Une erreur inconnue est survenue")
            return redirect(url_for('reservation_api.reservation'))
        else:
            try:
                Reservation.create(suite=suite, customer=current_user.id, datebeginning=start, dateend=end)
            except Exception:
                flash("Une erreur inconnue est survenue")
                return redirect(url_for('reservation_api.reservation_prefilled'))
            return redirect(url_for('history_api.customer_reservations'))
    else:
        try:
            suiteid = int(request.args.get('suiteid'))
            nexturl = request.args.get('next')
        except Exception:
            abort(404, "pas de donn??es")

        try:
            Suite.get(Suite.id == suiteid)
        except Exception:
            abort(404, "Suite inexistant")

        suite = Suite.select().where(Suite.id == suiteid).get_or_none()
        hotel = Hotel.select().where(Hotel.id == suite.hotel).get_or_none()
        return render_template("reservation_prefilled.html", hotel=hotel, suite=suite, nexturl=nexturl)


@reservation_api.route("/api/reservation", methods=['POST'])
@csrf.exempt
@login_required
def checkdate():
    """ V??rifie s'il n'y a pas d??j?? une r??servation ?? ces dates """

    # fonction anonyme qui formate la date au format datetimelocal
    str_to_datetime = lambda x: datetime.strptime(x, "%Y-%m-%d")

    suiteid = request.form.get('suiteId')
    start = request.form.get('start')
    end = request.form.get('end')

    if not suiteid:
        abort(400, 'Missing arguments')

    reservations = Reservation.select().where(Reservation.suite == suiteid)

    try:
        suiteid = int(suiteid)
        start = str_to_datetime(start)
        end = str_to_datetime(end)
    except Exception as error:
        print(error)
        abort(400, "Echec dans la r??cup??ration des donn??es")

    tests = []
    message_error.clear()

    tests.append(valideperiod(start, end))
    tests.append(periodlength(start, end))
    tests.append(pastperiod(start, end))
    if reservations:
        tests.append(overlapperiod(suiteid, start))
        tests.append(overlapperiod(suiteid, end))

    if not all(tests):
        return jsonify(message_error)
    else:
        # Pas de reservation sur cette suite
        return "", 204
