# from fastapi import Depends
from app.main import api
from app.services.auth import Protected
from app.routers import users

protected = Protected()

api.include_router(users.router, prefix='/users', tags=['Users'])
# api.include_router(topics.router, prefix='/topics', tags=['Topics'], dependencies=[Depends(protected)])
