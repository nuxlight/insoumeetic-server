# List of schema of app
account_schema = {
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
    'accounts': {
        'schema': account_schema,
        'additional_lookup':
            {
                'url': 'regex("[\w]+")',
                'field': 'username'
            },
    }
}
MONGO_HOST = '192.168.99.100'
MONGO_PORT = 27017
MONGO_DBNAME = 'insoumeetic'
RESOURCE_METHODS = ['GET', 'POST', 'DELETE']
XML = False