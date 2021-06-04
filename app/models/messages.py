from pydantic import BaseModel


class MessageNewUserCreated(BaseModel):
    message: str = 'New user created!'


class MessageLogout(BaseModel):
    message: str = 'Bye see you later :)'
