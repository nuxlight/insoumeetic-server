# List of schema of app
people_schema = {
    'username': {
        'type': 'string',
        'required': True,
        'minlength': 2,
    },
    'password': {
        'type': 'string',
        'required': True,
        'minlength': 8,
    },
    'age': {
        'type': 'integer',
        'required': True
    }
}
# EVE configurations
DOMAIN = {
    'people': {
        'schema': people_schema,
        'additional_lookup': {
                'url': 'regex("[\w]+")',
                'field': 'username'
            },
    }
}
MONGO_HOST = 'localhost'
MONGO_PORT = 27017
MONGO_DBNAME = 'insoumeetic'
RESOURCE_METHODS = ['GET', 'POST', 'DELETE']
XML = False