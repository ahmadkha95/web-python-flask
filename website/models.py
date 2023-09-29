from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
from datetime import datetime

current_datetime = datetime.now()

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(255), default="", nullable=False)  # Change to String type
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref='notes')

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150))
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))

    def __repr__(self):
        return f'<User {self.id}: {self.email}>'
