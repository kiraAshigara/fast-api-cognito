## FAST-API-COGNITO

#### Run server:

``uvicorn app.main:api --reload``

#### Environment variables:

```
AWS_SECRET_KEY={aws_secret_manager_path}
```

#### Secret content:

```
{
  "LOG_LEVEL": 10,
  "COGNITO_CLIENT_ID": "",
  "COGNITO_POOL_ID": ""
}
```

#### Testing:

```
pytest app/test
```
