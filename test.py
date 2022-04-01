class User(db_wrapper.Model, flask_login.UserMixin):
    lastname = CharField()
    firstname = CharField()
    email = CharField(unique=True)
    password = CharField()
    updated = DateTimeField(default=datetime.now)
    is_admin = False

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

class Gestion():
    user = 
    hotel = For