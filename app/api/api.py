from fastapi import APIRouter

# local imports
from api.endpoints import pdfs


api_router = APIRouter()
api_router.include_router(pdfs.router, tags=["pdfs"])