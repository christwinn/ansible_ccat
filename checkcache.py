#!/usr/bin/env python3

import redis
import json

r   = redis.StrictRedis(host='localhost', port=6379, db=0)
key = 'ansible_facts' + 'node1.example.com'
val = r.get(key)

data = json.loads(val)
print (data['ansible_memfree_mb'])
