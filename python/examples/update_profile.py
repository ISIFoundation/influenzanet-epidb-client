#!/usr/bin/env python

import sys
sys.path += ['../src']

from epidb_client import EpiDBClient

api_key = 'your-epidb-api-key-here'
user_id = '1c66bb91-33fd-4c6c-9c11-8ddd94164ae8'
data = {
    'birth-place': 'Jakarta',
    'birth-day': '2009-09-09',
    'has-pets': False
}

client = EpiDBClient(api_key)
result = client.profile_update(user_id, data)

status = result['stat']

print "status:", status

if status != 'ok':
    print "error code:", result['code']
    print "       msg:", result['msg']

