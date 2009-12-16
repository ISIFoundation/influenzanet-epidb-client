from setuptools import setup

import sys
sys.path += ['src']

setup(
    name = "epidb-client",
    version = '0.1.5-alpha-1',
    url = 'http://www.epiwork.eu/',
    description = 'EPIWork Database - Client Code',
    author = 'Fajran Iman Rusadi',
    package_dir = {'': 'python/src'},
    packages = ['epidb_client'],
    install_requires = ['simplejson'],
    test_suite = 'epidb_client.tests',
)

