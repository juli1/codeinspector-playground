# Get the service resource.
dynamodb = boto3.resource('dynamodb')
# Create the DynamoDB table.
table = dynamodb.create_table(
  TableName='table',
  KeySchema=[
    {
      'AttributeName': 'attribute_name',
      'KeyType': 'HASH'
    },
    {
      'AttributeName': 'attribute_name',
      'KeyType': 'RANGE'
    }
  ],
  AttributeDefinitions=[
    {
      'AttributeName': 'attribute_name',
      'AttributeType': 'S'
    },
    {
      'AttributeName': 'attribute_name',
      'AttributeType': 'S'
    },
  ],
  ProvisionedThroughput={
    'ReadCapacityUnits': 5,
    'WriteCapacityUnits': 5
  }
)
# Wait until the table exists.
table.wait_until_exists()
# Print out some data about the table.
print(table.item_count)

import requests


requests.get("woeifjwe")
