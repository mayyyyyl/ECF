from flask import Blueprint, abort, request, render_template, flash, jsonify
from flask_login import current_user, login_required
from app import Hotel, Suite, Reservation, Customer
from datetime import datetime
from utils_date import *

reservation_api = Blueprint('reservation_api', __name__)


@reservation_api.route("/reservation", methods=['GET', 'POST'])
@login_required
def reservation():
    """ Renvoie au formulaire pour réserver """

    # fonction anonyme qui formate la date au format datetimelocal
    str_to_datetime = lambda x: datetime.strptime(x, "%Y-%m-%d")

    suiteid = request.args.get('suiteid')

    try:
        Suite.get(Suite.id == suiteid)
    except Exception:
        abort(404, "Suite inexistant")

    if request.method == 'POST':

        suite = request.form.get('suiteIdSelected')
        start = str_to_datetime(request.form.get('start'))
        end = str_to_datetime(request.form.get('end'))

        customer = Customer.select().where(Customer.user == current_user.id).get_or_none()
        if customer is None:
            flash("Vous n'êtes pas connecté avec un compte client")
            return 'ok pas client'
        else:
            try:
                Reservation.create(suite=suite, customer=customer.id, datebeginning=start, dateend=end)
            except Exception:
                flash("Une erreur inconnue est survenue")
                return 'ok erreur inconnue'
            return 'ok'
    else:

        # suites = Suite.select(Suite, Hotel).join(Hotel).where(Suite.hotel == Hotel.id)
        hotels = Hotel.select()
        return render_template("reservation.html", hotels=hotels)


@reservation_api.route("/api/reservation", methods=['POST'])
@login_required
def checkdate():
    """ Vérifie s'il n'y a pas déjà une réservation à ces dates """

    str_to_datetime = lambda x: datetime.strptime(x, "%Y-%m-%d")

    suiteid = request.form.get('suiteId')
    start = request.form.get('start')
    end = request.form.get('end')

    if not suiteid:
        abort(400, 'Missing arguments')

    reservations = Reservation.select().where(Reservation.suite == suiteid)

    if reservations:

        try:
            suiteid = int(suiteid)
            start = str_to_datetime(start)
            end = str_to_datetime(end)
        except Exception as error:
            print(error)
            abort(400, "Echec dans la récupération des données")

        tests = []
        message_error.clear()

        tests.append(valideperiod(start, end))
        tests.append(periodlength(start, end))
        tests.append(pastperiod(start, end))
        tests.append(overlapperiod(suiteid, start))
        tests.append(overlapperiod(suiteid, end))

        if not all(tests):
            return jsonify(message_error)
        else:
            return "", 204
    else:
        # pas de reservation sur cette suite
        return "", 204
