#!/usr/bin/env python

import sys
sys.path += ['../']

from epidb.client import EpiDBClient

data = 'data'

client = EpiDBClient()
client.submit(data)

