#!/usr/bin/env python

import sys
sys.path += ['..']

try:
    import json
except ImportError:
    import simplejson as json

from epidb.client import EpiDBClient

api_key = 'your-epidb-api-key-here'
user_id = '1c66bb91-33fd-4c6c-9c11-8ddd94164ae8'
data = {
    'birth-place': 'Jakarta',
    'birth-day': '2009-09-09',
    'has-pets': False
}

param = json.dumps(data)

client = EpiDBClient(api_key)
res = client.profile_update(user_id, param)

result = json.loads(res)
status = result['stat']

print "status:", status

if status != 'ok':
    print "error code:", result['code']
    print "       msg:", result['msg']

