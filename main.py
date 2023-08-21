

from fastapi import FastAPI
from . import schemas
# import uvicorn



app = FastAPI()


@app.get('/')
def index():
    return 'Hey'


@app.get('/{id}')
def about(id : int):
    return {'this' : {'about':id}}



@app.post('/blog')
def post(request:schemas.Blog):
    return {request.title:request.body} 


# if __name__ == '__main__':
#     uvicorn.run(app, host="127.0.0.1", port = 9000)