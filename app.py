from flask import Flask
from playhouse.flask_utils import FlaskDB
from datetime import datetime
from peewee import *
from utils import hashingpassword
import click
import flask_login

login_manager = flask_login.LoginManager()

DATABASE = 'sqlite:///hotels.db'
SECRET_KEY = '3RreRxY4kKWqUAq4'

app = Flask(__name__)
app.config.from_object(__name__)
db_wrapper = FlaskDB(app)
login_manager.init_app(app)
login_manager.login_view = "login_api.login"


# Définition des modeles

class User(db_wrapper.Model, flask_login.UserMixin):
    lastname = CharField()
    firstname = CharField()
    email = CharField(unique=True)
    password = CharField()
    updated = DateTimeField(default=datetime.now)

    def save(self, *args, **kwargs):
        self.updated = datetime.now()
        return super(User, self).save(*args, **kwargs)

    def get_id(self):
        return str(self.id)

    @property
    def fullname(self):
        return f'{self.firstname} {self.lastname}'


class Admin(db_wrapper.Model):
    user = ForeignKeyField(User, backref='admin')


class Client(db_wrapper.Model):
    user = ForeignKeyField(User, backref='client')


class Hotel(db_wrapper.Model):
    name = CharField()
    address = CharField()
    city = CharField()
    description = CharField()
    updated = DateTimeField(default=datetime.now)

    def save(self, *args, **kwargs):
        self.updated = datetime.now()
        return super(Hotel, self).save(*args, **kwargs)


class Gerant(db_wrapper.Model):
    user = ForeignKeyField(User, backref='gerant')
    hotel = ForeignKeyField(Hotel, backref='gerant')


class Suite(db_wrapper.Model):
    titre = CharField()
    img = BigBitField()
    description = CharField()
    price = FloatField()
    link = CharField()
    hotel = ForeignKeyField(Hotel, backref='suites')
    updated = DateTimeField(default=datetime.now)

    def save(self, *args, **kwargs):
        self.updated = datetime.now()
        return super(Suite, self).save(*args, **kwargs)


class Reservation(db_wrapper.Model):
    suite = ForeignKeyField(Hotel, backref='reservation')
    client = ForeignKeyField(Client, backref='reservation')
    datebeginning = DateTimeField()
    dateend = DateTimeField()
    updated = DateTimeField(default=datetime.now)

    def save(self, *args, **kwargs):
        self.updated = datetime.now()
        return super(Reservation, self).save(*args, **kwargs)

# Import des Blueprints


from index import index_api
from debug import *
from reservation import reservation_api
from login import *

app.register_blueprint(index_api)
app.register_blueprint(debug_api)
app.register_blueprint(reservation_api)
app.register_blueprint(login_api)


@app.cli.command("init_db")
def init_db():
    """Cette commande initialise la BDD """

    try:
        with db_wrapper.database:
            db_wrapper.database.create_tables([User, Admin, Gerant, Hotel, Suite, Client, Reservation])

        first = click.prompt('Your first name', type=str)
        last = click.prompt('Your last name', type=str)
        password = click.prompt('Your password', type=str, hide_input=True)
        email = click.prompt('Your email address', type=str)

        newuser = User.create(firstname=first, lastname=last, email=email, password=hashingpassword(password))
        Admin.create(user=newuser.id)

        newhotel = Hotel.create(name='Mon premier Hotel', address='9 Rue de la Fontaine Grillée', city='La Haie-Fouassière', description='ipsum in blandit ultrices enim lorem ipsum dolor sit amet consectetuer adipiscing elit proin interdum mauris non ligula pellentesque ultrices phasellus id sapien in sapien iaculis congue vivamus metus arcu adipiscing molestie hendrerit at vulputate vitae nisl aenean lectus pellentesque')
        Suite.create(titre='Suite de reve', img='/static/img/hotel.jpg', description='description de la suite', price='300', link='https://www.booking.com/hotel/fr/holiday-home-bucolique.fr.html?aid=390156;label=duc511jc-1DCAsoTUIWaG9saWRheS1ob21lLWJ1Y29saXF1ZUgzWANoTYgBAZgBDbgBF8gBDNgBA-gBAYgCAagCA7gC3OLIkQbAAgHSAiQ1NTI1NmFkOC00Y2MzLTQ4MjAtYmNlNC1hM2RiYzFkOTJkM2LYAgTgAgE;sid=2b3a5887ae5f0c86c2fcc89e7a12a735;dist=0&keep_landing=1&sb_price_type=total&type=total&', hotel=newhotel.id)

    except Exception:
        click.echo('Une erreur s\'est produite.')
        exit(1)

    else:
        click.echo('Base de données correctement initialisée.')
        exit(0)
