from flask import Flask, render_template, Response
from application import app
import random

@app.route("/colour_of_phone", methods = ["GET"])
def get_colour_of_phone():


    colour = ["black", "white", "red"]
    colour_of_phone = random.choice(colour)

    return Response(colour, mimetype="text/plain")



    