from flask import Flask
from peewee import *
from playhouse.flask_utils import FlaskDB
from datetime import datetime
from utils import hashingpassword
from flask_admin import Admin
from flask_admin.contrib.peewee import ModelView
import click
import flask_login
# from flask_appbuilder import expose

login_manager = flask_login.LoginManager()

DATABASE = 'sqlite:///hotels.db'
SECRET_KEY = '3RreRxY4kKWqUAq4'

app = Flask(__name__)
app.config.from_object(__name__)

db_wrapper = FlaskDB(app)

login_manager.init_app(app)
login_manager.login_view = "login_api.login"

admin = Admin(app, name='Easy Admin ', template_mode='bootstrap4')

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
    def is_authenticated(self):
        return True

    @property
    def fullname(self):
        return f'{self.firstname} {self.lastname}'


class Admin(db_wrapper.Model):
    user = ForeignKeyField(User, backref='admin')


class Customer(db_wrapper.Model):
    user = ForeignKeyField(User, backref='customer')


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
    customer = ForeignKeyField(Customer, backref='reservation')
    datebeginning = DateTimeField()
    dateend = DateTimeField()
    updated = DateTimeField(default=datetime.now)

    def save(self, *args, **kwargs):
        self.updated = datetime.now()
        return super(Reservation, self).save(*args, **kwargs)


# class AllView(ModelView):

#     def is_accessible(self):
#         return login.current_user.is_authenticated

#     def inaccessible_callback(self, name, **kwargs):
#         return redirect(url_for('login_api.login'))
# from flask_login.utils import current_user


# class MyView(ModelView):
#     @expose('/')
#     def index(self):
#         return self.render('admin/index.html')

#     def is_accessible(self):
#         return current_user.is_authenticated()

# admin.add_view(MyView(ModelView))
admin.add_view(ModelView(Gerant))
admin.add_view(ModelView(User))
admin.add_view(ModelView(Suite))


class HotelView(ModelView):
    column_exclude_list = ['id']
    # model_form_converter = CustomModelConverter
    # filter_converter = filters.FilterConverter()
    fast_mass_delete = False


admin.add_view(HotelView(Hotel))


# Import des Blueprints


from index import index_api
from reservation import reservation_api
from login import *
from user import user_api
from suite import suite_api
from history import history_api

app.register_blueprint(index_api)
app.register_blueprint(reservation_api)
app.register_blueprint(login_api)
app.register_blueprint(user_api)
app.register_blueprint(suite_api)
app.register_blueprint(history_api)

# Commande permettant d'inisialiser la base de données


@app.cli.command("init_db")
def init_db():
    """Cette commande initialise la BDD """

    try:
        with db_wrapper.database:
            db_wrapper.database.create_tables([User, Admin, Gerant, Hotel, Suite, Customer, Reservation])

        first = click.prompt('Your first name', type=str)
        last = click.prompt('Your last name', type=str)
        password = click.prompt('Your password', type=str, hide_input=True)
        email = click.prompt('Your email address', type=str)

        newhotel = Hotel.create(name='Mon premier Hotel', address='9 Rue de la Fontaine Grillée', city='La Haie-Fouassière', description='ipsum in blandit ultrices enim lorem ipsum dolor sit amet consectetuer adipiscing elit proin interdum mauris non ligula pellentesque ultrices phasellus id sapien in sapien iaculis congue vivamus metus arcu adipiscing molestie hendrerit at vulputate vitae nisl aenean lectus pellentesque')
        Suite.create(titre='Suite de reve', img='/static/img/hotel.jpg', description='description de la suite', price='300', link='https://www.booking.com/hotel/fr/holiday-home-bucolique.fr.html?aid=390156;label=duc511jc-1DCAsoTUIWaG9saWRheS1ob21lLWJ1Y29saXF1ZUgzWANoTYgBAZgBDbgBF8gBDNgBA-gBAYgCAagCA7gC3OLIkQbAAgHSAiQ1NTI1NmFkOC00Y2MzLTQ4MjAtYmNlNC1hM2RiYzFkOTJkM2LYAgTgAgE;sid=2b3a5887ae5f0c86c2fcc89e7a12a735;dist=0&keep_landing=1&sb_price_type=total&type=total&', hotel=newhotel.id)

        newadmin = User.create(firstname=first, lastname=last, email=email, password=hashingpassword(password))
        newclient = User.create(firstname='paul', lastname='Dupont', email='paul@email.fr', password=hashingpassword('paul'))
        newgerant = User.create(firstname='jean', lastname='Dupont', email='jean@email.fr', password=hashingpassword('jean'))
        Admin.create(user=newadmin.id)
        Customer.create(user=newclient.id)
        Gerant.create(user=newgerant.id, hotel=newhotel.id)

    except Exception:
        click.echo('Une erreur s\'est produite.')
        exit(1)

    else:
        click.echo('Base de données correctement initialisée.')
        exit(0)
