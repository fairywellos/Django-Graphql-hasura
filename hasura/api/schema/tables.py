import json

from django.conf import settings

from hasura.api import Hasura

hasura = Hasura()


def table_util(query, schema):
    headers = {
        'X-Hasura-Access-Key': settings.HASURA_SAAS_ACCESS_KEY,
        'X-HASURA-TARGET-SCHEMA': schema,
        'Content-Type': 'application/json'
    }
    query_str = json.dumps(query)
    resp_data = hasura.request('post', json.loads(query_str), headers=headers)
    return resp_data


def untrack(schema, table):
    query = {
        "type": "untrack_table",
        "args": {
            "table": {
                "schema": f"{schema}",
                "name": f"{table}"
            },
            "cascade": True
        }
    }
    return table_util(query, schema)


def track(schema, table):
    query = {
        "type": "track_table",
        "args": {
            "schema": f"{schema}",
            "name": f"{table}"
        }
    }
    return table_util(query, schema)
