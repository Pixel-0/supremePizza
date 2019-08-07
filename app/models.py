from . import db
from flask_login import UserMixin
from . import login_manager
from werkzeug.security import generate_password_hash,check_password_hash


@login_manager.user_loader
def load_user(user_id):

    return User.query.get(int(user_id))


class User(db.Model):
    '''
    creating table for users
    '''
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255), index = True)
    password_hash = db.Column(db.String(255))
    pass_secure = db.Column(db.String(255))


    #securing passwords
    @property
    def password(self):
        raise AttributeError('You cannot read the Password Attribute')

    @password.setter
    def password(self,password):
        self.pass_secure= generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

    def __repr__(self):
        return f'User{self.username}'


class Roles(db.Model):
    '''
    database table for Roles
    '''
    __tablename__ = 'Roles'
    id = db.Column(db.Integer, primary_key = True)
    type = db.Column(db.String(255))
    users = db.relationship("User", backref = "Role", lazy="dynamic")

class Pizza(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    size = db.Column(db.String(255))
    price = db.Column(db.Numeric(8,2))
    description = db.Column(db.String(255))
    users = db.relationship("User", backref = "Pizza", lazy="dynamic")


    def save_pizza(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_pizza(cls,id):
        pizza = Pizza.query.filter_by(pizza_size=size)