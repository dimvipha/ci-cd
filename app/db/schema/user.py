from pydantic import BaseModel
from typing import Union
from datetime import datetime

class CreatUser(BaseModel):
    username: Union[str,None] = "KoKo"
    email: str
    password: str

class UpdateUser(BaseModel):
    username: Union[str,None] = None
    email: Union[str,None] = None
    password: Union[str,None] = None
    profile: Union[str,None] = None

class ResponseUser(BaseModel):
    uuid: str
    username: str
    email: str
    is_deleted: bool
    is_verified: bool
    created_date: datetime
    profile: Union[str,None] = None
    updated_date: Union[datetime,None] = None
    
