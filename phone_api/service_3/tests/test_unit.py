from unittest.mock import patch
from flask import url_for 
from flask_testing import TestCase
import requests_mock

from application import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):
    def test_get_colour_of_phone(self):
        response = self.client.get(url_for('get_colour_of_phone'))
        self.assertIn(response.data, b'black, red, white')
        #with patch("random.choice") as mock_random:
         #   random.choice = "black"
          #  response = self.client.get(url_for('get_colour_of_phone'))
           # self.assertEqual(b'black', response.data)

