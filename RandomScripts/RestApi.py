__author__ = 'pmacharl'

import requests,json

response = requests.get('https://api.github.com/users/machzqcq/repos')

assert response.status_code == 200

print(response.content)

json_hash = json.loads(response.text)

print(json_hash[0]['id'])

# for repo in response.json():
#     print('[{}] {}'.format(repo['language'], repo['name']))

