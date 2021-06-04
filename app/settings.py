import os
import json
import boto3
import logging

AWS_SECRET_KEY = os.environ['AWS_SECRET_KEY']


def get_config():
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name='us-east-1'
    )

    try:
        secret_value = client.get_secret_value(
            SecretId=AWS_SECRET_KEY
        )

        return json.loads(secret_value['SecretString'])
    except Exception as ex:
        raise ex


logging.basicConfig(level=10)
logger = logging.getLogger(__name__)
config = get_config()
