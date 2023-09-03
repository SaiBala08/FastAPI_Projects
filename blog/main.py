from fastapi import FastAPI, Depends, status, Response, HTTPException
from . import schemas
from .database import engine, Base, SessionLocal, Blog
from sqlalchemy.orm import session
import logging
from typing import List

Base.metadata.create_all(engine)
app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



@app.post('/blog')
def Create(request : schemas.Account, db : session = Depends(get_db)):
    new_blog = Blog(id = request.id, email = request.email, hashed_password = request.hashed_password, is_active = request.is_active)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog



@app.get('/blog', response_model = List[schemas.ShowAccount])
def Get_All_Data(db : session = Depends(get_db)):
    blogs = db.query(Blog).all()
    return blogs


@app.get('/blog/{id}',status_code = status.HTTP_200_OK, response_model = schemas.ShowAccount)
def Show_id(id, response : Response, db : session = Depends(get_db)):
    blog = db.query(Blog).filter(Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail = f"Blog with id {id} not found")
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'detail' : f"Blog with id {id} not found"}

    return blog


@app.delete('/blog/{id}',status_code=status.HTTP_204_NO_CONTENT)
def Delete(id, db : session = Depends(get_db)):
    blog = db.query(Blog).filter(Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail = f"Blog with id {id} not found")
    blog.delete(synchronize_session = False)
    db.commit()
    return 'Done'


@app.put('/blog/{id}',status_code=status.HTTP_202_ACCEPTED)
def update(id, request : schemas.Account, db : session = Depends(get_db)):
    blog = db.query(Blog).filter(Blog.id == id)

    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail = f"Blog with id {id} not found")

    blog.update(vars(request))
    db.commit()
    return 'Updated'



