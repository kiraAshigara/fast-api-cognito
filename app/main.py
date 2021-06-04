import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from app.tools.logger import logger

api = FastAPI(
    title="Fast Api Cognito",
    description="This is a very fancy project, with auto docs for the API and everything",
    version="1.0.0",
)


@api.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(content={
        'message': str(exc.detail)
    }, status_code=exc.status_code)


@api.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return JSONResponse(content={
        'message': str(exc)
    }, status_code=400)


origins = [
    "*"
]

api.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    logger.info('Fast Api Cognito v1')

    uvicorn.run(
        "app.main:api",
        host="127.0.0.1",
        port=3000
    )
