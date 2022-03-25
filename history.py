from flask import Blueprint, flash, render_template
from flask_login import current_user
from app import Reservation, Customer

history_api = Blueprint('history_api', __name__)


@history_api.route("/mes-reservations")
def customer_reservations():
    """ Renvoie l'ensemble des réservations d'un client """

    customer = Customer.select().where(Customer.user == current_user.id).get_or_none()
    if not customer:
        flash("Vous devez être connecté avec un compte client")

    reservations = Reservation.select().where(Reservation.customer == customer.id)

    return render_template("history.html", reservations=reservations)
