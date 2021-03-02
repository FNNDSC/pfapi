from fastapi import FastAPI
from pfapi.router import router

app = FastAPI()
app.include_router(router)
