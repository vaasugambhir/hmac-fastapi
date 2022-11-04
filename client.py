import requests
from constants import BASE_URL

# res = requests.get(BASE_URL)
# print(res.json())

obj = {
    'key': 'k1h23b2e21jeg1j2fej12he',
    'source': 'vaasugambhir',
    'message': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
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
