from time import timezone
from flask_login import UserMixin
from sqlalchemy import true
from sqlalchemy.sql import func
from App import db


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    userName=db.Column(db.String(150), unique=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    
    reviews=db.relationship("Reviews", uselist=False)


class Reviews(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.Text)
    
    # date = db.Column(db.DateTime(timezone=True), default=func.now())
    date = db.Column(db.String(20))

    rating=db.Column(db.Float)
    rentlisting_id = db.Column(db.Integer) 
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class RentalListing(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    appartmentName = db.Column(db.String(150), unique=True)
    appartmentEmail = db.Column(db.String(150), unique=True)
    contactNumber = db.Column(db.String(20))
    price = db.Column(db.Float)
    distance = db.Column(db.Integer)
    location = db.Column(db.String(150))
    utilities = db.Column(db.String(50))
    curfew = db.Column(db.String(20))
    environment = db.Column(db.String(150))
    restrictions = db.Column(db.String(50))