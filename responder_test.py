import unittest
import json
import handler
from responder import Responder


class TestResponderClass(unittest.TestCase):

    def test_default_values(self):
        responder = Responder()
        self.assertEqual(responder.body, {})
        self.assertEqual(responder.headers, None)
        self.assertEqual(responder.statusCode, 0)

    def test_response_no_headers(self):
        responder = Responder(statusCode=200, body={'url': 'http://test.com'})
        response = responder.respond()
        self.assertEqual(200, response['statusCode'])
        self.assertEqual('{"url": "http://test.com"}', response['body'])

        # expect 'headers' not in response dict
        error = False
        try:
            response['headers']
        except:
            error = True
        self.assertEqual(error, True)

    def test_redirect_with_headers(self):
        responder = Responder(
            statusCode=302, body='http://test.com', headers={'test': 'val'})
        response = responder.respond()
        self.assertEqual(response['statusCode'], 302)
        self.assertEqual(response['body'], 'http://test.com')
        self.assertEqual(response['headers'], {'test': 'val'})


if __name__ == '__main__':
    unittest.main()
