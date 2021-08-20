import logging
import unittest

import flask
from flask import Response

from flask_requests_logging import FlaskRequestsLogging

app = flask.Flask(__name__)
FlaskRequestsLogging(app)

logging.basicConfig(level=logging.INFO)


@app.route('/', methods=['GET'])
def response():
    return Response('ok')


@app.route('/value', methods=['GET'])
def value():
    raise ValueError()


class TestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.client = app.test_client()

    def test_requests(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_error(self):
        resp = self.client.get('/value')
        self.assertEqual(resp.status_code, 500)
