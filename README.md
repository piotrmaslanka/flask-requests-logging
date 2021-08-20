# flask-requests-logging
[![Build Status](https://travis-ci.com/smok-serwis/flask-requests-logging.svg)](https://travis-ci.com/smok-serwis/flask-requests-logging)
[![Test Coverage](https://api.codeclimate.com/v1/badges/34b392b61482d98ad3f0/test_coverage)](https://codeclimate.com/github/smok-serwis/flask-requests-logging/test_coverage)
[![Code Climate](https://codeclimate.com/github/smok-serwis/flask-requests-logging/badges/gpa.svg)](https://codeclimate.com/github/smok-serwis/flask-requests-logging)
[![Issue Count](https://codeclimate.com/github/smok-serwis/flask-requests-logging/badges/issue_count.svg)](https://codeclimate.com/github/smok-serwis/flask-requests-logging)
[![PyPI](https://img.shields.io/pypi/pyversions/flask-requests-logging.svg)](https://pypi.python.org/pypi/flask-requests-logging)
[![PyPI version](https://badge.fury.io/py/flask-requests-logging.svg)](https://badge.fury.io/py/flask-requests-logging)
[![PyPI](https://img.shields.io/pypi/implementation/flask-requests-logging.svg)](https://pypi.python.org/pypi/flask-requests-logging)
[![License](https://img.shields.io/pypi/l/flask-requests-logging)](https://github.com/Dronehub/flask-requests-logging)

Log all Flask requests with varying levels depending on the severity of the result

## Installation

```bash
pip install flask
```

## Usage

```python
import flask
from flask_requests_logging import FlaskRequestsLogging

app = flask.Flask(__name__)
FlaskRequestsLogging(app)
```

Go read the [if you're interested in the details](flask_requests_logging/__init__.py).

Enjoy!

## Changelog

### v0.2

* added pass_as_extras parameter

### v0.1

* first release, wow!
