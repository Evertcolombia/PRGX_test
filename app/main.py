from fastapi import FastAPI

# local imports
from api.api import api_router


app = FastAPI()

# source https://fastapi.tiangolo.com/tutorial/bigger-applications/
app.include_router(api_router, prefix="/api/v1")
