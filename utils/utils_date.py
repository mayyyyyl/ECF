from flask import flash, redirect, url_for
from app import Reservation
from datetime import datetime, timedelta
import pendulum


message_error = []
# Vérifie que start < end


def valideperiod(start, end):
    if start >= end:
        message_error.append("Période incorrecte")
        return False
    return True

# Vérifie date n'est pas dans le passé


def pastperiod(start, end):
    if start.date() < datetime.now().date() or end.date() < datetime.now().date():
        message_error.append("Période dans le passé")
        return False
    return True

# Vérifie longueur période < 8 semaines


def periodlength(start, end):
    if end - start > timedelta(weeks=8):
        message_error.append("Période trop longue")
        return False
    return True

# Vérifie que les périodes ne se chevauchent pas


def overlapperiod(suiteid, date):
    try:
        myUserReservations = Reservation.select().where(Reservation.suite == suiteid)
    except Exception:
        flash("Une erreur inconnue est survenue")
        return redirect(url_for('reservation_api.reservation'))

    for r in myUserReservations:
        if r.dateend is None:
            r.dateend = datetime.now()

        if r.datebeginning <= date <= r.dateend:
            message_error.append("Date indisponible")
            return False
    return True

# Vérifie que la date est pas 3 jours avant la réservation


def checkdate(datestart):

    print(pendulum.now())
    print(pendulum.instance(datestart).add(days=-3))

    if pendulum.now() > pendulum.instance(datestart).add(days=-3):
        return False
    else:
        return True
