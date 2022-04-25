from fastapi import FastAPI

# local imports
from api.api import api_router
from api.db.init_db import create_db_and_tables

app = FastAPI()

# source https://fastapi.tiangolo.com/tutorial/bigger-applications/
app.include_router(api_router, prefix="/api/v1")

@app.on_event("startup")
def on_startup():
    create_db_and_tables()
