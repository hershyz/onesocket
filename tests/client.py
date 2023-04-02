# SOCKETAPI

import requests
import time

payload = {
    'endpoint': 'add',
    'a': 2,
    'b': 3
}

for i in range(50):
    tick = time.perf_counter()
    r = requests.get('http://localhost:8080', json=payload)
    tock = time.perf_counter()
    print(tock - tick)
    time.sleep(0.5)