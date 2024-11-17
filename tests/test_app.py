import logging
import time
import unittest

import flask
from flask import Response

from flask_requests_logging import FlaskRequestsLogging

app = flask.Flask(__name__)
FlaskRequestsLogging(app)


@app.route('/', methods=['GET'])
def response():
    return Response('ok')


@app.route('/value', methods=['GET'])
def value():
    raise ValueError()


@app.route('/stream', methods=['GET'])
def stream2():
    def stream():
        yield b'test'
        yield b'test'
        time.sleep(3)
        yield b'test'

    return Response(stream())


class TestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.client = app.test_client()

    def test_requests(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_error(self):
        resp = self.client.get('/value')
        self.assertEqual(resp.status_code, 500)

    def test_streaming_response(self):
        resp = self.client.get('/stream')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.data, b'testtesttest')
