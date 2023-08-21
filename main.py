

from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


@app.get('/')
def index():
    return 'Hey'


@app.get('/{id}')
def about(id : int):
    return {'this' : {'about':id}}



class Blog(BaseModel):
    title : str
    body : str

@app.post('/blog')
def post(request:Blog):
    return {request.title:request.body} 