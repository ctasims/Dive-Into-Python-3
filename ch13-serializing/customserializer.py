def to_json(python_object):
    """ Convert bytes object into dictionary. """
    if isinstance(python_object, bytes):
        return {'__class__': 'bytes',
                '__value__': list(python_object)}
    raise TypeError(repr(python_object) + ' is not JSON serializable')

def from_json(json_object):
    """ Convert dict back into bytes object. """
    if '__class__' in json_object:
        if json_object['__class__'] == 'bytes':
            return bytes(json_object['__value__'])
    return json_object
