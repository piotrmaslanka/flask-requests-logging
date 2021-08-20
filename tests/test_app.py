import unittest

import flask
from flask import Response

from flask_requests_logging import FlaskRequestsLogging

app = flask.Flask(__name__)
FlaskRequestsLogging(app)


@app.route('/', methods=['GET'])
def response():
    return Response('ok')


class TestCase(unittest.TestCase):
    def test_requests(self):
        client = app.test_client()
        resp = client.get('/')
        self.assertEqual(resp.status_code, 200)
