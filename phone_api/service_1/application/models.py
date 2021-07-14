from application import db

class Phone(db.Model):
    id = db.column(db.Integer, primary_key=True)
    phone_brand = db.column(db.string(50), nullable=False)
    colour_of_phone = db.column(db.string(30),nullable=False)
    price = db.column(db.string(1000),nullable=False)

