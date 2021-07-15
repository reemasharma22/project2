from flask import Flask, render_template, Response
from application import app
import random


@app.route("/phone_brand", methods = ["GET"])
def get_phone_brand():

    phone = ["Iphone 5","Iphone 6" "Iphone 7", "Iphone 8"]
    phone_brand = random.choice(phone)

    return Response(phone_brand, mimetype="text/plain")



    

