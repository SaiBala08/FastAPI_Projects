
from pydantic import BaseModel

class Account(BaseModel):
    id : str
    email : str
    hashed_password : str
    is_active : bool



class New_User(BaseModel):
    id : int
    name : str
    email : str
    hashed_password : str

    class Config():
        orm_mode = True


class ShowAccount(BaseModel):
    id : str
    email : str
    creator : New_User

    class Config():
        orm_mode = True
