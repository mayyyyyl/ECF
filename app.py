from flask import Flask
from peewee import *
from playhouse.flask_utils import FlaskDB
from datetime import datetime


app = Flask(__name__)
app.config.from_object(__name__)
db_wrapper = FlaskDB(app)

contacts_db = SqliteDatabase('database.db')

# Définition des modeles


class Admin(db_wrapper.Model):
    email = CharField(unique=True)
    password = CharField()


class Hotel(db_wrapper.Model):
    name = CharField()
    address = CharField()
    city = CharField()
    description = CharField()

    def save(self, *args, **kwargs):
        self.updated = datetime.now()
        return super(Hotel, self).save(*args, **kwargs)


class Gerant(db_wrapper.Model):
    lastname = CharField()
    firstname = CharField()
    email = CharField(unique=True)
    password = CharField()
    id_hotel = ForeignKeyField(Hotel, backref='hotel')

    def save(self, *args, **kwargs):
        self.updated = datetime.now()
        return super(Gerant, self).save(*args, **kwargs)

class Suite(db_wrapper.Model):
    titre = CharField()
    img = BigBitField()
    description = CharField()
    price = FloatField()
    link = CharField()
    id_hotel = ForeignKeyField(Hotel, backref='hotel')

    def save(self, *args, **kwargs):
        self.updated = datetime.now()
        return super(Suite, self).save(*args, **kwargs)

class Client(db_wrapper.Model):
    lastname = CharField()
    firstname = CharField()
    email = CharField(unique=True)
    password = CharField()

    def save(self, *args, **kwargs):
        self.updated = datetime.now()
        return super(Client, self).save(*args, **kwargs)

    @property
    def fullname(self):
        return f'{self.firstname} {self.lastname}'

class Reservation(db_wrapper.Model):
    id_suite = ForeignKeyField(Hotel, backref='suite')
    id_client = ForeignKeyField(Hotel, backref='client')
    date_beginning = DateTimeField()
    date_end = DateTimeField()

    def save(self, *args, **kwargs):
        self.updated = datetime.now()
        return super(Reservation, self).save(*args, **kwargs)
