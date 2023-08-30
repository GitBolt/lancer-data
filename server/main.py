from fastapi import FastAPI
from routes import ranking
from dotenv import load_dotenv
from core.db import engine, Base
from fastapi.param_functions import Depends
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(ranking.router)

@app.on_event("startup")
async def startup() -> None:
    Base.metadata.create_all(bind=engine)


@app.get("/")
async def root() -> dict:
    return {"message": "Welcome"}
