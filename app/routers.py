from flask import render_template, redirect, flash
from app import app


@app.route('/clicker')
def clicker():
    return render_template('clicker.html')


@app.route('/profile')
def profile():
    return render_template('profile.html')


@app.route('/login', methods=["GET", "POST"])
def login():
    return render_template('login.html')


@app.route('/register', methods=["GET", "POT"])
def register():
    return render_template('register.html')
