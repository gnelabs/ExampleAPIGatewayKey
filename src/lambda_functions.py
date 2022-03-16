
__author__ = "Nathan Ward"

import logging
import json

_LOGGER = logging.getLogger()
_LOGGER.setLevel(logging.INFO)

def lambda_handler(event, context):
    print(event)
    
    return {
        "statusCode": 200,
        "body": json.dumps({'message': 'Hello World!'}),
        "headers": {
            'Content-Type': 'application/json',
        }
    }