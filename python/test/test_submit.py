#!/usr/bin/env python

import sys
sys.path += ['../']

from epidb.client import EpiDBClient

client = EpiDBClient()
client.submit('{ "data": "client" }', 'epidb-client')

