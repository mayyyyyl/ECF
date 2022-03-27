from flask import Blueprint, flash, render_template, request, abort, redirect, url_for
from flask_login import current_user, login_required
from app import Reservation, Customer
from utils_date import checkdate

history_api = Blueprint('history_api', __name__)


@history_api.route("/mes-reservations")
@login_required
def customer_reservations():
    """ Renvoie l'ensemble des réservations d'un client """

    customer = Customer.select().where(Customer.user == current_user.id).get_or_none()
    if not customer:
        flash("Vous devez être connecté avec un compte client")

    reservations = Reservation.select().where(Reservation.customer == customer.id).order_by(Reservation.datebeginning.desc())

    return render_template("history.html", reservations=reservations)


@history_api.route("/delete-reservation", methods=['POST'])
@login_required
def reservation_del():
    """ Supprimer une reservation """

    try:
        reservationid = int(request.form.get('reservationid'))

    except Exception:
        abort(400, 'Vous devez fournir une reservation id valide.')

    r = Reservation.get_by_id(reservationid)
    if not checkdate(r.datebeginning):
        flash("Vous ne pouvez pas supprimer un réservation 3 jours avant")
        return redirect(url_for('history_api.customer_reservations'))

    r.delete_instance()

    return redirect(url_for('history_api.customer_reservations'), code=303)