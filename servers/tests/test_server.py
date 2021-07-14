from flask import url_for
from flask_testing import TestCase
import requests_mock

from application import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestHome(TestBase):
    def test_home():
        with request_mock.Mocker() as mocker:
            mocker.get('http://phone_brand_api:5000/get_phone_brand', text='Iphone')
            mocker.get('http://colour_of_phone_api:5000/get_colour_of_phone', text='red')
            mocker.post('http://price_api:5000/post_price', text='500')
            response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'The Iphone is red at the price of 500', response.data)

