import boto3
from app.tools.conf import config
from app.tools.logger import logger
from app.models.users import NewUser, Authenticate, Me, RefreshToken

client = boto3.client('cognito-idp', region_name='us-east-1')


def new_user(user: NewUser):
    try:
        client.sign_up(
            ClientId=config['COGNITO_CLIENT_ID'],
            Username=user.email,
            Password=user.password,
            UserAttributes=[
                {
                    'Name': 'nickname',
                    'Value': user.nickname
                }
            ]
        )

        client.admin_confirm_sign_up(
            UserPoolId=config['COGNITO_POOL_ID'],
            Username=user.email
        )

    except Exception as ex:
        logger.error(str(ex))
        raise ex


def authenticate(user: Authenticate):
    try:
        response = client.initiate_auth(
            AuthFlow='USER_PASSWORD_AUTH',
            AuthParameters={
                'USERNAME': user.email,
                'PASSWORD': user.password
            },
            ClientId=config['COGNITO_CLIENT_ID']
        )

        tokens = {
            'access_token': response['AuthenticationResult']['AccessToken'],
            'refresh_token': response['AuthenticationResult']['RefreshToken']
        }

        return tokens
    except Exception as ex:
        logger.error(str(ex))
        raise ex


def get_user_info(access_token: str):
    try:
        response = client.get_user(
            AccessToken=access_token
        )

        user_id = None
        nickname = None

        for item in response['UserAttributes']:
            if item['Name'] == 'sub':
                user_id = item['Value']

            if item['Name'] == 'nickname':
                nickname = item['Value']

        return Me(id=user_id, nickname=nickname)
    except Exception as ex:
        logger.error(str(ex))
        raise ex


def logout(access_token: str):
    try:
        client.global_sign_out(
            AccessToken=access_token
        )
    except Exception as ex:
        logger.error(str(ex))
        raise ex


def get_new_tokens(refresh_token: RefreshToken):
    try:
        response = client.initiate_auth(
            AuthFlow='REFRESH_TOKEN_AUTH',
            AuthParameters={
                'REFRESH_TOKEN': refresh_token.refresh_token
            }
        )

        new_tokens = {
            'access_token': response['AuthenticationResult']['AccessToken'],
            'refresh_token': response['AuthenticationResult']['RefreshToken']
        }

        return new_tokens
    except Exception as ex:
        logger.error(str(ex))
        raise ex


def delete_user(user_id: str):
    try:
        client.admin_delete_user(
            UserPoolId=config['COGNITO_POOL_ID'],
            Username=user_id
        )
    except Exception as ex:
        logger.error(str(ex))
        raise ex
