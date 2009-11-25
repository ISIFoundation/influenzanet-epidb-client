from setuptools import setup

import sys
sys.path += ['src']

import epidb_client
version = epidb_client.__version__

setup(
    name = "epidb-client",
    version = version,
    url = 'http://www.epiwork.eu/',
    description = 'EPIWork Database - Client Code',
    author = 'Fajran Iman Rusadi',
    package_dir = {'': 'src'},
    packages = ['epidb_client'],
    install_requires = ['setuptools'],
)

