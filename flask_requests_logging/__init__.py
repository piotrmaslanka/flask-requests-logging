import typing as tp
import logging

from flask import Response, request

logger = logging.getLogger(__name__)
__version__ = '0.1a1'


def FlaskRequestsLogging(app, default_level_mapping: tp.Optional[tp.Dict[int, int]] = None,
                         log_template: str = 'Request {url} finished with {status_code}'):
    """
    Instantiate Flask-Requests-Logging

    :param app: app to use
    :param default_level_mapping: a mapping of either leftmost digit to error code, or entire
        error code to level mapping. Default is log 2xx and 3xx with INFO, 4xx with WARN
        and 5xx with ERROR. If not given, request will be logged with INFO.
    :param log_template: a string template that will be used with logging. It will take two format-level
        arguments called {url} and {status_code}
    """
    default_level_mapping = default_level_mapping or {2: logging.INFO,
                                                      3: logging.INFO,
                                                      4: logging.WARN,
                                                      5: logging.ERROR}

    @app.after_request
    def after_request(r: Response):
        url = str(request.url_rule)

        level = logging.INFO
        if r.status_code in default_level_mapping:
            level = default_level_mapping[r.status_code]
        else:
            p = r.status_code // 100
            if p in default_level_mapping:
                level = default_level_mapping[p]

        logger.log(level, log_template, url=url, status_code=r.status_code)

        return r

