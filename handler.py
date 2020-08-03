from responder import Responder
from dynamo_wrapper import DynamoWrapper
from url_mapper import UrlMapper
import json
from nanoid import generate
import logging


def shorten(event, context):
    if event['body'] == None or event['body'] is None:
        logging.warning("Validation Failed")
        return Responder(statusCode=400, body={'error': 'missing body'}).respond()

    data = json.loads(event['body'])

    if 'url' not in data:
        logging.warning("Validation Failed")
        return Responder(statusCode=400, body={'error': 'url is required'}).respond()

    domain_name = event['requestContext']['domainName']
    path = event['requestContext']['path']

    item = UrlMapper().create_url_map_item(
        long_url=data['url'],
        domain_name=domain_name,
        path=path
    )

    DynamoWrapper().create_url_item(item=item)

    body = {
        'shortUrl': item['short_url'],
    }

    return Responder(statusCode=200, body=body).respond()


def redirect(event, context):
    pathParams = event['pathParameters']

    data = DynamoWrapper().get_item(pathParams['id'])

    if 'Item' not in data:
        logging.warn("Short URL Not Found")
        return Responder(statusCode=404)

    destination = data['Item']['long_url']

    headers = {
        'Location': destination,
        'Content-Type': 'text/plain'
    }
    return Responder(statusCode=302, body=destination, headers=headers).respond()
