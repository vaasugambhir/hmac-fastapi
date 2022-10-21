import requests
from constants import BASE_URL

# res = requests.get(BASE_URL)
# print(res.json())

obj = {
    'key': 'k1h23b2e21jeg1j2fej12he',
    'source': 'vaasugambhir',
    'message': 'My PS4 will be burried with me',
    'digest': ''
}
res = requests.post(f'{BASE_URL}/get-digest', json=obj)
res = res.json()
print(f'Digest generated is: {res["digest"]}')

print('\nPassing the right digest:')
obj['digest'] = res['digest']
res = requests.post(f'{BASE_URL}/verify-digest', json=obj)
res = res.json()
print(res['message'])

print('\nPassing the wrong digest:')
obj['digest'] = 'd213bdo1bd1'
res = requests.post(f'{BASE_URL}/verify-digest', json=obj)
res = res.json()
print(res['message'])
