from unittest.mock import patch
from flask import url_for 
from flask_testing import TestCase
import requests_mock

from application import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):
    def test_get_phone_brand(self):
        response = self.client.get(url_for('get_phone_brand'))
        #phone = [b"Iphone5", b"Iphone6", b"Iphone7", b"Iphone8"]
        #phone = 'Iphone5,Iphone6,Iphone7,Iphone8'
        #self.assertIn(b'I phone5', response.data)
        self.assertIn(response.data, b'IPhone 5, Iphone 6,Iphone 7, Iphone 8')
        


    
