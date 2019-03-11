import os

HASURA_AUTO_TRACK_APPS = [
    'users'
]

HASURA_SAAS_ACCESS_KEY = os.getenv('HASURA_SAAS_ACCESS_KEY', 'mybigsecret')