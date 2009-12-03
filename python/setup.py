from setuptools import setup

import sys
sys.path += ['src']

setup(
    name = "epidb-client",
    version = '0.1.2',
    url = 'http://www.epiwork.eu/',
    description = 'EPIWork Database - Client Code',
    author = 'Fajran Iman Rusadi',
    package_dir = {'': 'src'},
    packages = ['epidb_client'],
    requires = ['simplejson'],
    test_suite = 'epidb_client.tests',
)

