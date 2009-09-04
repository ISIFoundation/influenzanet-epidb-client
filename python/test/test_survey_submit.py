#!/usr/bin/env python

import sys
sys.path += ['../']

from epidb.client import EpiDBClient

data = 'data'

client = EpiDBClient()
res = client.survey_submit(data)

print res

