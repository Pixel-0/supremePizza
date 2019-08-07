from flask import render_template, request, redirect, url_for, abort
from . import main
from ..models import User,Pizza,Roles,Toppings,Crust
from .. import db
from . forms import PitchForm, CommentForm, CategoryForm
from flask_login import login_required,current_user

@main.route('/')
def pizza():
    '''
    pizza order page
    '''
    pizza = Pizza.query.all()

    return render_template('index.html', pizza = pizza)
