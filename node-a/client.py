#!/usr/bin/env python3
from httpx import Client
from json import dumps

payload = {
    'message': 'Hello, world!'
}

with Client() as client:
    r = client.post('https://httpbin.org/post', json=payload)
    print(dumps(r.json(), indent=2))
