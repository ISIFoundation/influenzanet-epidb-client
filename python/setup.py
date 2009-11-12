from setuptools import setup

import epidb_client
version = epidb_client.__version__

setup(
    name = "epidb-client",
    version = version,
    url = 'http://www.epiwork.eu/',
    description = 'EPIWork Database - Client Code',
    author = 'Fajran Iman Rusadi',
    packages = ['epidb_client'],
    install_requires = ['setuptools'],
)

