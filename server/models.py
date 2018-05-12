from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

from server import db, login_manager


class User(db.Model):
    """ User model """

    __tablename__ = 'users'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))

    @property
    def password(self):
        """ Prevent password from being read """

        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        """ Hash password and set it """

        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        """ Check if hashed password matches actual password """

        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User: {}>'.format(self.first_name)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class Todo(db.Model):
    """ Todos model """

    __tablename__ = 'todos'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    day = db.Column(db.String(10), nullable=False)
    todo = db.Column(db.String(128), nullable=False)

    def __repr__(self):
        return '<Todo: {}>'.format(self.todo)


