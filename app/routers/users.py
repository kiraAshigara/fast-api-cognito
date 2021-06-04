from fastapi import APIRouter, Depends, HTTPException, Header
from typing import Optional
from app.services.auth import Protected
from app.models.users import NewUser, Authenticate, Tokens, Me, RefreshToken
from app.models.messages import MessageNewUserCreated, MessageLogout
from app.services import users
from app.const.exception import NotAuthorizedException

router = APIRouter()
protected = Protected()


@router.post('/', status_code=201, response_model=MessageNewUserCreated)
async def new_user(user: NewUser):
    try:
        users.new_user(user)
        return MessageNewUserCreated()
    except Exception as ex:
        raise HTTPException(status_code=500, detail=str(ex))


@router.post('/login', status_code=200, response_model=Tokens)
async def login(user: Authenticate):
    try:
        tokens = users.authenticate(user)
        return tokens
    except Exception as ex:
        exception = ex.__class__.__name__

        if exception == NotAuthorizedException:
            raise HTTPException(status_code=400, detail=str(ex))
        else:
            raise HTTPException(status_code=500, detail=str(ex))


@router.get('/logout', status_code=200, dependencies=[Depends(protected)], response_model=MessageLogout)
async def logout(authorization: Optional[str] = Header(None)):
    try:
        access_token = authorization.replace('Bearer ', '')
        users.logout(access_token)
        return MessageLogout()
    except Exception as ex:
        raise HTTPException(status_code=500, detail=str(ex))


@router.get('/me', status_code=200, response_model=Me)
async def me(current_user: Me = Depends(protected)):
    return current_user


@router.post('/refresh', status_code=200, response_model=Tokens)
async def get_new_tokens(refresh_token: RefreshToken):
    try:
        new_tokens = users.get_new_tokens(refresh_token)
        return new_tokens
    except Exception as ex:
        raise HTTPException(status_code=500, detail=str(ex))
