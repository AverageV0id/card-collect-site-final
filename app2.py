from flask import render_template, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import os
from app import app
from app.forms import *
from app.models import *

app = Flask(__name__)

# Настройка базы данных SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


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


@app.route('/register', methods=["GET", "POT"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash('Вы зарегистрировались как {}'.format(form.username.data))
    return render_template('register.html', form=form)

@app.route('/shop')
def shop():
    return render_template('shop.html')



if __name__ == '__main__':
    # Создаем базу и таблицы при первом запуске
    if not os.path.exists('cards.db'):
        db.create_all()
        # Добавим пример карточек
        card1 = Card(name='Первая карточка',rarity='1 in 5',value='500', image_filename='example1.jpg')
        card2 = Card(title='Вторая карточка',rarity='1 in 15',value='2000', image_filename='example2.jpg')
        db.session.add_all([card1, card2])
        db.session.commit()
    app.run(debug=True)