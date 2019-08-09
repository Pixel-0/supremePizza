from . import db
from flask_login import UserMixin
from . import login_manager
from werkzeug.security import generate_password_hash,check_password_hash


@login_manager.user_loader
def load_user(user_id):

    return User.query.get(int(user_id))



class User(db.Model,UserMixin):
    '''
    creating table for users
    '''
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255), index = True)
    password_hash = db.Column(db.String(255))
    pass_secure = db.Column(db.String(255))
    pizza = db.relationship("Pizza",backref="User")
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    
    
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
    __tablename__ = 'roles'
    
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(255))
    users = db.relationship('User',backref = 'roles',lazy="dynamic")

    def __repr__(self):
        return f'User{self.name}'


class Pizza(db.Model):
    __tablename__="pizza"
    id = db.Column(db.Integer, primary_key = True)
    size = db.Column(db.String(255))
    price = db.Column(db.Numeric(8,2))
    description = db.Column(db.String(255))
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    user = db.relationship("User", backref="Pizza ")
    crust_id = db.Column(db.Integer,db.ForeignKey("crust.id"))
    crust = db.relationship("Crust", backref="Pizza")
 

    def save_pizza(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_pizza(cls):
        pizza = Pizza.query.all()
        
        return pizza

class Crust(db.Model):
    __tablename__="crust"

    id= db.Column(db.Integer, primary_key= True)
    name = db.Column (db.String(255), unique = True)
    price = db.Column(db.Numeric(8,2))
    pizza = db.relationship("Pizza", backref="Crust")


    def save_toppings(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_crust():
        crust = Crust.query.all() 
        return crust       
    
class Topping(db.Model):
    __tablename__="toppings"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique = True)
    price = db.Column(db.Numeric(8,2))
    pizza_id = db.Column(db.Integer,db.ForeignKey("pizza.id"))
    pizza = db.relationship("Pizza", backref= "Topping   ")

    @classmethod
    def  get_toppings(cls):
        toppings = toppings.query.all()
        return  crust

