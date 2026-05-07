from pydantic import BaseModel, Field, EmailStr
from datetime import datetime
from typing import Optional
from .base_schemas import BaseSchema

class UserBase(BaseModel):
    name: str = Field(example="John Doe")
    email: EmailStr = Field(example="john@example.com")
    password: str = Field(..., min_length=8, max_length=72)

class UserCreate(UserBase):
    pass

class UserUpdate(UserBase):
    pass

class userdelete(BaseModel):
    password: str = Field(..., min_length=8, max_length=72)

class UserResponse(BaseModel):
    id: int = Field(example=1)
    name: str = Field(example="John Doe")
    email: str = Field(example="john@example.com")
    create_ts: Optional[datetime] = Field(default=None, example="2024-04-22T10:30:00")
    update_ts: Optional[datetime] = Field(default=None, example=None)
    delete_ts: Optional[datetime] = Field(default=None, example=None)
    
    class Config:
        from_attributes = True
