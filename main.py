from fastapi import FastAPI, Depends, HTTPException, status
from sqlmodel import Session, select
from database_connection import engine
from database import Users, CreateUser, VerifyUser
from password_hashing import create_hash_password, verify_hash_password
from jwt_tokens import create_token, verify_token

def get_session():
    with Session(engine) as session:
        yield session

app = FastAPI()

@app.post("/users", status_code=status.HTTP_201_CREATED)
def create_user(user: CreateUser, session: Session=Depends(get_session)):
    db_email=session.exec(select(Users).where(Users.email == user.email)).first()

    if db_email:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="already account exist at this email.")
    
    new_user = Users(
        name=user.name,
        age=user.age,
        phone_number=user.phone_number,
        email=user.email,
        password=create_hash_password(user.password)
    )

    session.add(new_user)
    session.commit()

    return{"id": new_user.id,
           "name": new_user.name,
           "age": new_user.age}


@app.post("/users/login", status_code=status.HTTP_200_OK)
def user_login(user: VerifyUser, session: Session=Depends(get_session)):
    db_email = session.exec(select(Users).where(Users.email == user.email)).first()
    if not db_email:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid email or password!")
    
    db_password = verify_hash_password(user.password, db_email.password)

    if not db_password:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid email or password!")
    
    payload=create_token(
        {"id": db_email.id,
         "email": db_email.email} 
    )
    return{"access_token": payload,
           "token_type": "Bearer"}