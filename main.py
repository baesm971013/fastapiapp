from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
import models
from database import engine
from domain.question import question_router


models.Base.metadata.create_all(bind=engine)

app=FastAPI()
origins =[
    "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(question_router.router)