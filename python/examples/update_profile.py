#!/usr/bin/env python

import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))), 'src'))

from epidb_client import EpiDBClient

import config

api_key = config.api_key
user_id = config.user_id
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

