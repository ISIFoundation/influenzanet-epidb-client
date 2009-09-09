#!/usr/bin/env python

import sys
sys.path += ['../']

from epidb.client import EpiDBClient
import config

key = config.key
data = 'data'

client = EpiDBClient(key)
client.server = config.server
res = client.submit_response(data)

print res

# vim: ts=4 sts=4 expandtab

