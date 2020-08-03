import json


class Responder:
    def __init__(self, statusCode=0, body={}, headers=None):
        self.body = body
        self.statusCode = statusCode
        self.headers = headers
        return

    def respond(self):
        response = {
            'statusCode': self.statusCode
        }

        if isinstance(self.body, dict):
            response['body'] = json.dumps(self.body)
        else:
            response['body'] = self.body

        if self.headers is not None:
            response['headers'] = self.headers

        return response
