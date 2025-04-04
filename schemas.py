from pydantic import BaseModel
from typing import Optional

class UserCreate(BaseModel):
    email: str
    password: str

class UserLogin(BaseModel):
    email: str
    password: str

class AddressCreate(BaseModel):
    user_id: int
    address: str
    is_default: Optional[bool] = False