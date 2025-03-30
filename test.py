import requests


params = {'target': 'Test'}

request = requests.get(
    'http://localhost:8000/simple_app',
    params=params
    )

print(request.json())
