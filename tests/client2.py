# FLASK

import requests
import time

payload = {
    'a': 2,
    'b': 3
}

for i in range(50):
    tick = time.perf_counter()
    r = requests.get('http://127.0.0.1:5000', json=payload)
    tock = time.perf_counter()
    print(tock - tick)
    time.sleep(0.5)