from fastapi import FastAPI
import schemas
from database import engine, Base

Base.metadata.create_all(engine)
app = FastAPI()


@app.post('/blog')
def Print(request : schemas.Blog):
    return "Printing"