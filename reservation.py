from flask import Blueprint, abort, request, render_template, flash
from app import Suite, Reservation
from datetime import datetime

reservation_api = Blueprint('reservation_api', __name__)


@reservation_api.route("/reservation", methods=['GET', 'POST'])
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
            Reservation.create(suite=suite, client=1, datebeginning=start, dateend=end)
        except Exception:
            flash("Une erreur inconnue est survenue")
            return 'ok erreur inconnue'
        return 'ok'
    else:

        suites = Suite.select()
        reservation = Reservation.select().where(Reservation.suite == suiteid)
        # rajouter where(Reservation.client == current_user.id)
        return render_template("reservation.html", suites=suites, reservation=reservation)
