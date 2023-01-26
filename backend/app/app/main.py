import sys
import os
from dotenv import load_dotenv
load_dotenv()
path = os.environ["FILE_PATH"]
sys.path.append(path)

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from app.app.config.settings import Settings
from app.app.db.base import Base
from app.app.db.base import engine
from typing import Dict
# from app.api.api_v1.api import api_router

Base.metadata.create_all(engine)

# app = FastAPI(
#     title=Settings.PROJECT_NAME, openapi_url=f"{Settings.API_V1_STR}/openapi.json"
# )

app = FastAPI()

@app.get("/")
def get_hello() -> Dict[str, str]:
    return {"hello": "world"}

# # Set all CORS enabled origins
# if settings.BACKEND_CORS_ORIGINS:
#     app.add_middleware(
#         CORSMiddleware,
#         allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
#         allow_credentials=True,
#         allow_methods=["*"],
#         allow_headers=["*"],
#     )

# app.include_router(api_router, prefix=settings.API_V1_STR)
