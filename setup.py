from setuptools import find_packages
from distutils.core import setup
from flask_requests_logging import __version__

setup(version=__version__,
      packages=find_packages(include=['smok', 'smok.*', 'ngtt', 'ngtt.*']),
      )
