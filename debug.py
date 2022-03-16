from flask import Blueprint
from app import Suite
import tablib

debug_api = Blueprint('debug_api', __name__)


@debug_api.route("/debug/suites")
def suites():
    """ Renvoie la liste des suites """

    data = tablib.Dataset()
    data.headers = ['id', 'titre', 'img', 'description', 'hotel_id']
    query = Suite.select()

    for suite in query:
        data.append([suite.id, suite.titre, suite.img, suite.description, suite.hotel])

    return data.export('html')
