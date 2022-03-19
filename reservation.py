from flask import Blueprint, abort, request, render_template, flash, jsonify
from flask_login import current_user, login_required
from app import Suite, Reservation, Customer
from datetime import datetime
import pendulum

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

        try:
            customer = Customer.select().where(Customer.user == current_user.id).get_or_none()
        except Exception:
            flash("Vous n'êtes pas connecté avec un compte client")
            return 'ok pas client'

        try:
            Reservation.create(suite=suite, customer=customer.id, datebeginning=start, dateend=end)
        except Exception:
            flash("Une erreur inconnue est survenue")
            return 'ok erreur inconnue'
        return 'ok'
    else:

        suites = Suite.select()
        customer = Customer.select().where(Customer.user == current_user.id)
        reservation = Reservation.select().where(Reservation.suite == suiteid, Reservation.customer == current_user.id)
        return render_template("reservation.html", suites=suites, reservation=reservation)


@reservation_api.route("/api/reservation")
@login_required
def checkdate():
    """ Vérifie s'il n'y a pas déjà une réservation à ces dates """

    # suiteid = request.form.get('suiteIdSelected')
    # print(suiteid)

    reservations = Reservation.select().where(Reservation.suite == 1)
    # reservations_nb = Reservation.select().where(Reservation.suite == 1).count()

    if reservations:
        for r in reservations:
            ret = {}
            ret['start'] = pendulum.instance(r.datebeginning, 'Europe/Paris')

            try:
                ret['end'] = pendulum.instance(r.dateend, 'Europe/Paris')

            except ValueError:
                flash('Une erreur est survenue pendant la vérification')

            ret['reservationId'] = r.id

            return jsonify(ret)
    else:
        # pas de reservation sur cette suite
        return "", 204
