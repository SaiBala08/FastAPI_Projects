
from pydantic import BaseModel

class Account(BaseModel):
    id : str
    email : str
    hashed_password : str
    is_active : bool


class ShowAccount(BaseModel):
    email : str
    hashed_password : str

    class Config():
        orm_mode = True
