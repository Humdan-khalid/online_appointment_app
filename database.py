from sqlmodel import SQLModel, Field
from pydantic import EmailStr, BaseModel
from datetime import datetime

class Users(SQLModel, table = True):
    id: int = Field(default=None, primary_key=True)
    name: str = Field(min_length=3, max_length=40, nullable=False)
    age: int = Field(le=95, ge=17, nullable=False)
    phone_number: str = Field(unique=True, min_length=11, max_length=11, nullable=False)
    email: EmailStr = Field(index=True, nullable=False)
    password: str = Field(min_length=8, max_length=100)
    account_type: str = ("User")
    created_at: datetime = Field(default_factory=datetime.utcnow)

class CreateUser(BaseModel):
    name: str = Field(min_length=3, max_length=40, nullable=False)
    age: int = Field(le=95, ge=17, nullable=False)
    phone_number: str = Field(min_length=11, max_length=11, nullable=False)
    email: EmailStr = Field(nullable=False)
    password: str = Field(min_length=8, max_length=100)

class VerifyUser(SQLModel, BaseModel):
    email: EmailStr
    password: str