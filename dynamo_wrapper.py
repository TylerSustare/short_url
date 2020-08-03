import os
import boto3


class DynamoWrapper:
    def __init__(self):
        self._dynamodb = boto3.resource('dynamodb')
        self._table = self._dynamodb.Table(self._get_table_name())

    def get_item(self, key):
        return self._table.get_item(
            Key={
                'pk': key
            }
        )

    def create_url_item(self, item={}):
        return self._table.put_item(
            Item=item,
            ConditionExpression="attribute_not_exists(pk)"
        )

    def _get_table_name(self):
        return os.environ['DYNAMODB_TABLE']
