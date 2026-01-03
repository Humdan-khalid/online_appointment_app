# from sqlmodel import SQLModel, Field
# from pydantic import EmailStr

# class Users(SQLModel, table = True):
#     id: int = Field(default=None, primary_key=True)
#     name: str = Field(min_length=3, max_length=40, nullable=False)
#     age: int = Field(le=95, ge=17, nullable=False)
#     phone_number: int = Field(min_length=11, max_length=11, nullable=False)
#     email: EmailStr = Field(nullable=False)
#     password: str = Field(min_length=8, max_length=40)
#     account_type: str = ("User")