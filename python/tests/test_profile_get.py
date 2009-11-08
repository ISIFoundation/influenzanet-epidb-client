#!/usr/bin/env python

import sys
sys.path += ['../']

from epidb_client import EpiDBClient
import config

key = config.key

client = EpiDBClient(key)
client.server = config.server
res = client.profile_get(config.user_id)

print res

# vim: ts=4 sts=4 expandtab

