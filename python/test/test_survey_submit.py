#!/usr/bin/env python

import sys
sys.path += ['../']

from epidb.client import EpiDBClient

key = '0123456789abcdef0123456789abcdef01234567'
data = 'data'

client = EpiDBClient(key)
res = client.survey_submit(data)

print res

