from enum import unique
from typing import Optional
from werkzeug.security import generate_password_hash, check_password_hash
import sqlalchemy as sa
import sqlalchemy.orm as so
from app import  db
from flask_login import UserMixin, login_manager
from app import login
from app import app

# Настройка базы данных SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

class User(UserMixin, db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    username: so.Mapped[str] = so.mapped_column(sa.String(64), index=True,  unique=True)
    email: so.Mapped[str] = so.mapped_column(sa.String(120), index=True, unique=True)
    password_hash: so.Mapped[Optional[str]] = so.mapped_column(sa.String(256))
    balance: so.Mapped[int] = so.mapped_column()
    registration_date: so.Mapped[str] = so.mapped_column(sa.String(20))
    user_card: so.Mapped[str] = so.mapped_column(sa.String(100))

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


@login.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))



class Card(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    name: so.Mapped[str] = so.mapped_column(index=True, unique=True)
    rarity: so.Mapped[str] = so.mapped_column(index=True)
    value: so.Mapped[int] = so.mapped_column(index=True)
    image_filename = db.Column(db.String(100), nullable=False)  # имя файла картинки из static/images

    def repr(self):
        return f'<Card {self.title}>'


