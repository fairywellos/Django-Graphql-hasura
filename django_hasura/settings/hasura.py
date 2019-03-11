import os

HASURA_AUTO_TRACK_APPS = [
    'users',
    'nonesne'
]

HASURA_SAAS_ACCESS_KEY = os.getenv('HASURA_SAAS_ACCESS_KEY', 'mybigsecret')