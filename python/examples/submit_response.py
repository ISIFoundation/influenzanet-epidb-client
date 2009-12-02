#!/usr/bin/env python

import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))), 'src'))

from datetime import datetime

from epidb_client import EpiDBClient

import config

api_key = config.api_key
data = {
    'user_id': config.user_id,
    'date': datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S"),
    'survey_id': config.user_id,
    'answers': {
        'q1': 1,
        'q2': True,
        'q3': [ 1, 2, 3 ],
        'q4': 'Jakarta'
    }
}

client = EpiDBClient(api_key)
result = client.response_submit(data)

status = result['stat']

print "status:", status

if status == 'ok':
    print "id:", result['id']
else:
    print "error code:", result['code']
    print "       msg:", result['msg']



