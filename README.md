# onesocket

Object-oriented, single-socket API library with CORS support by default.

### initializing API:

```python
import onesocket

# create handler object:
class Add:

    # create handler method, take json data:
    def handle(self, json_data):
        a = float(json_data['a'])
        b = float(json_data['b'])
        return a + b

# define handler object instance and endpoint map:
add_obj = Add()
endpoint_map = {
    'add': add_obj
}

# initialize api with port and endpoint object mappings:
api = onesocket.OneSocketAPI(8080, endpoint_map)
```

```python
output: Serving HTTP on PORT: 8080
```

### HTTP request from client:

```python
import requests

# define endpoint in payload:
payload = {
    'endpoint': 'add',
    'a': 2,
    'b': 3
}

r = requests.get('http://localhost:8080', json=payload)
print(r.text)
```

```python
output: 5.0
```
