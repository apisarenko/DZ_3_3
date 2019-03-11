from urllib.parse import urlencode
import requests

OAUTH_URL = 'https://oauth.vk.com/authorize'
USER_URL = 'https://vk.com/id'
APP_ID = 10799607

auth_data = {
    'client_id': APP_ID,
    'display': 'page',
    'scope': 'friends',
    'response_type': 'token',
    'v': 5.92
}

TOKEN = 'a52db6c5763f3e243d8921577d4643aec1dc5ad9883492658223426df3a750a164237920476c01a3558ce'

print('?'.join((OAUTH_URL, urlencode(auth_data))))

class User:
    def __init__(self, id):
        self.id = id

    def get_params(self):
        return {
            'user_id': self.id,
            'user_ids': self.id,
            'access_token': TOKEN,
            'v': 5.92
        }

    def get_friends(self):
        params = self.get_params()
        response = requests.get(
            'https://api.vk.com/method/friends.get',
            params
        )
        return response.json()

    def get_users(self):
        params = self.get_params()
        response = requests.get(
            'https://api.vk.com/method/users.get',
            params
        )
        return response.json()

    def __str__(self):
        return (USER_URL + str(self.get_users()['response'][0]['id']))

    def __and__(self, other):
        return list(set(self.get_friends()['response']['items'])& set(other.get_friends()['response']['items']))


user1 = User(10799607)
user2 = User(92370527)

print(user1 & user2)
print(user1)
