from flask import Blueprint, render_template, request
from flask_login import current_user, login_required
from app import Hotel, Suite, Gerant
from route.login import gerant_required

index_api = Blueprint('index_api', __name__)


@index_api.route("/")
def index():
    """ Renvoie la page d'accueil """

    return render_template("index.html")


@index_api.route("/gerant")
def index_gerant():
    """ Renvoie la page d'accueil pour les gérants """

    return render_template("gerant/index.html")


@index_api.route("/hotels")
def hotel_list():
    """ Renvoie la liste des hotels """

    hotels = Hotel.select()
    return render_template("hotel_list.html", hotels=hotels)


@index_api.route("/mon-etablissement")
@login_required
@gerant_required
def gerant_hotel():
    """ Renvoie l'hotel du gerant """

    try:
        hotel = Hotel.select(Hotel, Gerant, Suite).join(Gerant).switch(Hotel).join(Suite).where(Gerant.user == current_user.id, Gerant.hotel == Hotel.id, Suite.hotel == Hotel.id)
        if hotel:
            return render_template("gerant/etablissement.html", hotel=hotel)
        else:
            return render_template("404.html", message="Etablissement inexsitant")
    except Exception:
        return render_template("404.html", message="Une erreur est survenue")


@index_api.route("/hotels/hotel")
def hotel_info():
    """ Renvoie les informations d'un hotel """

    hotelid = request.args.get('hotelid')

    try:
        Hotel.get(Hotel.id == hotelid)
    except Exception:
        return render_template("404.html", message="Hotel inexistant")

    suites = Suite.select().where(Suite.hotel == hotelid)

    return render_template("hotel_info.html", suites=suites)
