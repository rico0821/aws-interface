from cloud.response import Response

# Define the input output format of the function.
# This information is used when creating the *SDK*.
info = {
    'input_format': {
        'session_id': 'str',

        'event_source': 'str?',
        'event_name': 'str?',
        'user_id': 'str?',
        'start_key': 'str?',
    },
    'output_format': {
        'success': 'bool',
        'end_key': 'str',
        'items': 'list',
    }
}


def do(data, resource):
    partition = 'log'
    body = {}
    params = data['params']

    event_source = params.get('event_source', None)
    event_name = params.get('event_name', None)
    user_id = params.get('user_id', None)
    start_key = params.get('start_key', None)

    operation = None
    instructions = []
    for field_name, value in (('event_source', event_source), ('event_name', event_name), ('user_id', user_id)):
        if value:
            instructions.append((operation, (field_name, 'eq', value)))
            operation = 'and'
    if len(instructions) > 0:
        items, end_key = resource.db_query(partition, instructions, start_key)
    else:
        items, end_key = resource.db_get_items_in_partition(partition, start_key)
    body['end_key'] = end_key
    body['items'] = items
    return Response(body)
