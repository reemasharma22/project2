from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from application import db


class Phone(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    phone_brand = db.Column(db.String(50), nullable=False)
    colour_of_phone = db.Column(db.String(30),nullable=False)
    price = db.Column(db.String(1000),nullable=False)

