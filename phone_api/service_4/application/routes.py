from flask import Flask, render_template, Response, request
from application import app
import random


@app.route("/price", methods=["GET","POST"])
def price():

    phone_deal = request.get_json()
    phone = {"Iphone5", "Iphone6", "Iphone7", "Iphone8"}
    colour = {"red", "black", "white"}
    price = ("500","600","700","800")


    if phone == "Iphone 5":
        if colour == 'black':
            price = '500'
        elif colour == 'white':
            price = '500'
        elif colour == 'red':
            price = '500'

    elif phone == "Iphone 6":
        if colour == 'black':
            price = '600'
        elif colour == 'white':
            price = '600'
        elif colour == 'red':
            price = '600'

    elif phone == "I phone 7":
        if colour == 'black':
            price = '700'
        elif colour == 'white':
            price = '700'
        elif colour == 'red':
            price = '700'

    elif phone == "I phone 8":
        if colour == 'black':
            price = '800'
        elif colour == 'white':
            price = '800'
        elif colour == 'red':
            price = '800'

    else:
        return Response(random.choice(price), mimetype = "text/plain")




    

    