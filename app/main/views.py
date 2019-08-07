from flask import render_template, request, redirect, url_for, abort
from . import main
from ..models import User,Pizza,Roles,Topping,Crust
from flask_login import login_required,current_user


@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template('profile/profile.html',user = user)


@main.route('/')
def pizza():
    '''
    pizza order page
    '''
    title = "Home"

    return render_template('index.html', title = title)
