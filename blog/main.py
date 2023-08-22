from fastapi import FastAPI
from . import schemas

app = FastAPI()

@app.post('/blog')
def Print(request : schemas.Blog):
    return "Printing"