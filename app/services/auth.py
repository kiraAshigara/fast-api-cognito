from fastapi import HTTPException, Request
from fastapi.security import HTTPBearer
from app.tools.logger import logger
from app.models.users import Me
from app.services.users import get_user_info


class Protected(HTTPBearer):

    async def __call__(self, request: Request) -> Me:
        try:
            access_token = request.headers['Authorization'].replace('Bearer ', '')
            return get_user_info(access_token)
        except Exception as ex:
            logger.error(str(ex))
            raise HTTPException(status_code=403, detail='Unauthorized :(')
