from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from db.main import engine
from db.schema import Base
from routers.main import router

Base.metadata.create_all(bind=engine)

app = FastAPI(
  title='give_me_snack'
)

app.add_middleware(
  CORSMiddleware,
  allow_credentials=True,
  allow_origins=['*'],
  allow_methods=['*'],
  allow_headers=['*'],
)

app.include_router(router, prefix='/api/v1')
