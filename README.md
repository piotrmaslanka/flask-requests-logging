# flask-requests-logging

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

### v0.1

* first release, wow!
