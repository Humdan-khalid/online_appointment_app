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

class Staffs(SQLModel, table = True):
    id: int = Field(default=None, primary_key=True)
    name: str = Field(min_length=3, max_length=30, nullable=False)
    age: int = Field(ge=18, le=75)
    profession: str = Field(nullable=False)
    phone_number: str = Field(min_length=11, max_length=11, nullable=False, unique=True)
    email: EmailStr = Field(nullable=False, index=True)
    password: str = Field(min_length=8)

class CreateStaff(BaseModel):
    name: str = Field(min_length=3, max_length=30, nullable=False)
    age: int = Field(ge=18, le=75)
    profession: str = Field(nullable=False)
    phone_number: str = Field(min_length=11, max_length=11, nullable=False, unique=True)
    email: EmailStr = Field(nullable=False, index=True)
    password: str = Field(min_length=8)

class VerifyStaff(BaseModel):
    email: EmailStr
    password: str

class Admins(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str = Field(min_length=3, max_length=30, nullable=False)
    age: int = Field(ge=19, le=75, nullable=False)
    phone_number: str = Field(min_length=11, max_length=11, unique=True, nullable=False)
    email: EmailStr = Field(index=True, nullable=False)
    password: str = Field(min_length=8, max_length=150, nullable=False)

class CreateAdmin(BaseModel):
    name: str = Field(min_length=3, max_length=30, nullable=False)
    age: int = Field(ge=19, le=75, nullable=False)
    phone_number: str = Field(min_length=11, max_length=11, unique=True, nullable=False)
    email: EmailStr = Field(index=True, nullable=False)
    password: str = Field(min_length=8, max_length=150, nullable=False)

class VerifyAdmin(BaseModel):
    email: EmailStr
    password: str

