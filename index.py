from flask import Blueprint, render_template, request
from app import Hotel, Suite

index_api = Blueprint('index_api', __name__)


@index_api.route("/")
def index():
    """ Renvoie la page d'accueil """
    return render_template("index.html")


@index_api.route("/hotels")
def hotel_list():
    """ Renvoie la liste des hotels """

    hotels = Hotel.select()

    return render_template("hotel_list.html", hotels=hotels)


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
