from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.database import create_db_and_tables

@asynccontextmanager
async def lifespan(app : FastAPI):
    create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)

@app.get("/")
def root():
    return {"mensagem": "API da Biblioteca funcionando!"}