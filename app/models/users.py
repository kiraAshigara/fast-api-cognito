from pydantic import BaseModel


class NewUser(BaseModel):
    nickname: str
    email: str
    password: str


class Authenticate(BaseModel):
    email: str
    password: str


class Tokens(BaseModel):
    access_token: str
    refresh_token: str


class Me(BaseModel):
    id: str
    nickname: str


class RefreshToken(BaseModel):
    refresh_token: str
