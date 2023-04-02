import requests

# define endpoint in payload:
payload = {
    'endpoint': 'add',
    'a': 2,
    'b': 3
}

r = requests.get('http://localhost:8080', json=payload)
print(r.text)
