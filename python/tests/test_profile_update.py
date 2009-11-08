#!/usr/bin/env python

import sys
sys.path += ['../']

from epidb_client import EpiDBClient
import config

key = config.key
data = {
    'name': 'John Doe',
    'address': 'Jakarta'
}

client = EpiDBClient(key)
client.server = config.server
res = client.profile_update(config.user_id, data)

print res

# vim: ts=4 sts=4 expandtab

