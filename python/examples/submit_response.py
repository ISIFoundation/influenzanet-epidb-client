#!/usr/bin/env python

import sys
sys.path += ['..']

try:
    import json
except ImportError:
    import simplejson as json

from epidb.client import EpiDBClient

api_key = 'your-epidb-api-key-here'
data = {
    'user_id': '1c66bb91-33fd-4c6c-9c11-8ddd94164ae8',
    'date': '2009-09-09 09:09:09',
    'answers': {
        'q1': 1,
        'q2': True,
        'q3': [ 1, 2, 3 ],
        'q4': 'Jakarta'
    }
}

param = json.dumps(data)

client = EpiDBClient(api_key)
result = client.response_submit(param)

status = result['stat']

print "status:", status

if status == 'ok':
    print "id:", result['id']
else:
    print "error code:", result['code']
    print "       msg:", result['msg']



