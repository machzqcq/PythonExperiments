__author__ = 'pmacharl'

import requests,json

response = requests.get('https://api.github.com/users/jaimegildesagredo/repos')

assert response.status_code == 200

for repo in response.json():
    print('[{}] {}'.format(repo['language'], repo['name']))

