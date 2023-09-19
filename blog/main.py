from fastapi import FastAPI, Depends, status, Response, HTTPException
from . import schemas
from .database import engine, Base, SessionLocal, Blog, User, get_db
from sqlalchemy.orm import session
import logging
from typing import List
from passlib.context import CryptContext
from .routers import blog, user

Base.metadata.create_all(engine)
app = FastAPI()

app.include_router(blog.router)
app.include_router(user.router)



# pass_cnxt = CryptContext(schemes=['bcrypt'],deprecated='auto')







