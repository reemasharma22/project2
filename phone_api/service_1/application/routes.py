from flask import Flask, render_template, Response
from application import app, db
import random
from application.models import Phone


@app.route('/')
def home():
    phone = request.get('http://phone_brand_api:5000/get_phone_brand')
    colour = request.get('http://colour_of_phone_api:5000/get_colour_of_phone')
    price = request.post('http://price_api:5000/get_price')
    return render_template('index.html', phone_brand=phone.text, colour_of_phone=colour.text, price=price.text)


    












