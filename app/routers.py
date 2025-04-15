from flask import render_template, redirect, flash
from app import app
from app.forms import *

@app.route('/clicker')
def clicker():
    return render_template('clicker.html')


@app.route('/profile')
def profile():
    return render_template('profile.html')


@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Вы вошли как {}'.format(
            form.username.data))
    return render_template('login.html', form=form)


@app.route('/register', methods=["GET", "POT"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash('Вы зарегистрировались как {}'.format(form.username.data))
    return render_template('register.html', form=form)

@app.route('/shop')
def shop():
    return render_template('shop.html')