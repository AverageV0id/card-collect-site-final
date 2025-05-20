import random
from flask import render_template, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import login_user, current_user, login_required
from app import app
from app.forms import *
from app.models import *
from flask import request, jsonify



def create_test_user():
    user = User.query.filter_by(username='testuser').first()
    if not user:
        user = User(
            username='testuser',
            email='testuser@example.com',
            balance=1000,
            registration_date='2025-05-20',
            user_card='default_card'
        )
        user.set_password('testpassword')  # задаем пароль
        db.session.add(user)
        db.session.commit()
    return user



@app.route('/auto_login')
def auto_login():
    user = create_test_user()
    login_user(user)
    flash('Вы автоматически вошли как тестовый пользователь.')
    return redirect('/profile')



@app.route('/')
def start():
    user = create_test_user()
    login_user(user)
    cards = Card.query.all()
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



@app.route('/update_balance', methods=['POST'])
@login_required
def update_balance():
    data = request.get_json()
    coins_to_add = data.get('coins', 0)
    if coins_to_add <= 0:
        return jsonify({'error': 'Invalid coins amount'}), 400

    # Обновляем баланс пользователя
    current_user.balance += coins_to_add
    db.session.commit()

    return jsonify({'new_balance': current_user.balance})



@app.route('/shop')
def shop():
    id = random.randint(1, 2)
    card1 = Card.query.get(id)
    id = random.randint(3, 4)
    card2 = Card.query.get(id)
    id = random.randint(5, 6)
    card3 = Card.query.get(id)
    id = random.randint(7, 9)
    card4 = Card.query.get(id)
    return render_template('shop.html', card1=card1, card2=card2, card3=card3, card4=card4)