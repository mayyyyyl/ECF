from flask import Blueprint, render_template

index_api = Blueprint('index_api', __name__)


@index_api.route("/")
def index():
    """ Renvoie la page d'accueil"""
    return render_template("index.html")
