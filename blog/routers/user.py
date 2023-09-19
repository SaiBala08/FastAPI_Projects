from fastapi import APIRouter, Depends, status, Response, HTTPException
from .. import schemas
from ..database import Blog, get_db, User
from typing import List
from sqlalchemy.orm import session


router = APIRouter()



@router.post('/user', tags=['user'])
def create_user(request : schemas.New_User, db : session = Depends(get_db)):
    #hash_password = pass_cnxt.hash(request.hashed_password)
    new_user = User(id = request.id, name = request.name, email = request.email, hashed_password = request.hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user



@router.post('/user/{id}', tags=['user'])
def create_user(id, db : session = Depends(get_db)):
    user = db.query(User).filter(User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail = f"User with id {id} not found")

    return user