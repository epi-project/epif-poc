#!/usr/bin/env python3
from httpx import Client

payload = {
    'message': 'Hello, world!'
}

with Client() as client:
    r = client.post('http://localhost:8000/echo', json=payload)
    print(r.json())
