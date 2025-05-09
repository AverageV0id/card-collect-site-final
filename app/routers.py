import random

from flask import render_template, redirect, flash
from flask_sqlalchemy import SQLAlchemy

from app import app
from app.forms import *
from app.models import *

@app.route('/')
def start():
    cards = Card.query.all()
    print(cards)
    return render_template('profile.html', cards=cards)

@app.route('/clicker')
def clicker():
    return render_template('clicker.html')


@app.route('/profile')
def profile():
    cards = Card.query.all()
    print(cards)
    return render_template('profile.html', cards=cards)


@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Вы вошли как {}'.format(
            form.username.data))
    return render_template('login.html', form=form)


@app.route('/register', methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash('Вы зарегистрировались как {}'.format(form.username.data))
    return render_template('register.html', form=form)

@app.route('/shop')
def shop():
    id = random.randint(1, 9)
    card = Card.query.get(id)
    return render_template('shop.html', card=card)