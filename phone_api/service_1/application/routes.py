from flask import Flask, render_template
import requests
from application import app
from application.models import Phone


@app.route('/')
def home(): 
    phone = requests.get('http://service_2:5000/phone_brand')
    colour = requests.get('http://service_3:5000/colour_of_phone')
    price = requests.post('http://service_4:5000/price', json = {"phone": phone.text, "colour":colour.text})
    return render_template('index.html', phone_brand=phone.text, colour_of_phone=colour.text, price=price.text)


    












