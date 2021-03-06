
from cloud.response import Response

# Define the input output format of the function.
# This information is used when creating the *SDK*.
info = {
    'input_format': {
        'start_key': 'str'
    },
    'output_format': {
        'items': [{
            'id': 'str',
            'creationDate': 'int',
            'email': 'str',
            'passwordHash': 'str',
            'salt': 'str',
            'group': 'str',
            'extra': 'map',
        }, ],
        'end_key': 'str'
    }
}


def do(data, resource):
    body = {}
    params = data['params']

    start_key = params.get('start_key', None)
    limit = params.get('limit', 100)
    partition = 'user'

    items, end_key = resource.db_get_items_in_partition(partition, exclusive_start_key=start_key, limit=limit)
    body['items'] = items
    body['end_key'] = end_key
    return Response(body)
