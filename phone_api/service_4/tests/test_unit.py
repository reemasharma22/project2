from unittest.mock import patch
from flask import url_for 
from flask_testing import TestCase
import requests_mock

from application import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestCase):
    def test_price(self):
        response = self.client.get(url_for('post_price'))
        self.assertIn(response.data, b'500, 600, 700, 800')
    #def test_Iphone5(self):
        #response = self.client.post(url_for('price'), json={'phone_brand' : 'Iphone 5', 'colour_of_phone': 'black'})
        #self.assertEqual(b'500', response.data)
