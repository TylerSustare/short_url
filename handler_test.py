from unittest import mock
from dynamo_wrapper import DynamoWrapper
from url_mapper import UrlMapper
import unittest
import json
import handler


class TestHandlerMethods(unittest.TestCase):
    @mock.patch.object(DynamoWrapper, '_get_table_name', return_value='CoffeeTable')
    @mock.patch.object(DynamoWrapper, 'get_item', return_value={'Item': {'long_url': 'http://test.co'}})
    def test_redirect(self, mock_get_item, mock__get_table_name):
        event = {'pathParameters': {
            'id': 'abc123'
        }}
        result = handler.redirect(event, None)
        mock_get_item.assert_called_with('abc123')
        self.assertEqual(result['body'], 'http://test.co')

    def test_shorten_validation(self):
        result = handler.shorten({'body': None}, None)
        self.assertEqual(result, {
            'statusCode': 400,
            'body': '{"error": "missing body"}'
        })

        result = handler.shorten({'body': '{}'}, None)
        self.assertEqual(result, {
            'statusCode': 400,
            'body': '{"error": "url is required"}'
        })

    @mock.patch.object(UrlMapper, 'get_random_chars', return_value='abc12')
    @mock.patch.object(DynamoWrapper, '_get_table_name', return_value='CoffeeTable')
    @mock.patch.object(DynamoWrapper, 'create_url_item')
    def test_shorten(self, mock_create_url_item, mock__get_table_name, mock_get_random_chars):
        event = {
            'body': '{ "url": "http://localhost" }',
            'requestContext': {
                'domainName': 'not-bitly',
                'path': '/s/'
            }
        }
        result = handler.shorten(event, None)
        self.assertEqual(result, {
            'statusCode': 200, 'body': '{"shortUrl": "https://not-bitly/s/abc12"}'
        })


if __name__ == '__main__':
    unittest.main()
