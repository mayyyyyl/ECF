from flask import flash, redirect, url_for
from app import Reservation
from datetime import datetime, timedelta


message_error = []
# Vérifie que start < end


def valideperiod(start, end):
    if start >= end:
        message_error.append("Période incorrecte")
        return False
    return True

# Vérifie date n'est pas le futur


def pastperiod(start, end):
    if start < datetime.now() or end < datetime.now():
        message_error.append("Période dans le passé")
        return False
    return True

# Vérifie longueur période < 15h


def periodlength(start, end):
    if end - start > timedelta(weeks=54):
        message_error.append("Période trop longue")
        return False
    return True

# Vérifier le chevauchement de période


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
            message_error.append("Période qui se chevauche")
            return False
    return True
