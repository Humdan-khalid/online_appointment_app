from fastapi import FastAPI, Depends, HTTPException, status
from sqlmodel import Session, select
from database_connection import engine
from database import Users, CreateUser, VerifyUser, CreateStaff, Staffs, VerifyStaff, Admins, CreateAdmin, VerifyAdmin
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
        name=user.name.capitalize(),
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

@app.post("/staff", status_code=status.HTTP_201_CREATED)
def create_staff(staff: CreateStaff, session: Session=Depends(get_session)):
    db_staff=session.exec(select(Staffs).where(Staffs.email == staff.email)).first()
    
    if db_staff:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="already account exist at this email.")
    
    new_staff=Staffs(
        name=staff.name.capitalize(),
        profession=staff.profession.capitalize(),
        age=staff.age,
        phone_number=staff.phone_number,
        email=staff.email,
        password=create_hash_password(staff.password)        
    )

    session.add(new_staff)
    session.commit()

    return{
        "id": new_staff.id,
        "name": new_staff.name,
        "profession": new_staff.profession
        }

@app.post("/staffs/login", status_code=status.HTTP_200_OK)
def staff_login(staff: VerifyStaff, session: Session=Depends(get_session)):
    db_staff = session.exec(select(Staffs).where(Staffs.email == staff.email)).first()
    
    if not db_staff:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid email or password!")

    if not verify_hash_password(staff.password, db_staff.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid email or password!")
    
    payload=create_token(
        {"id": db_staff.id,
         "email": db_staff.email}
    )
    return{"access_token": payload,
           "token_type": "Bearer"}

@app.post("/admin", status_code=status.HTTP_201_CREATED)
def create_admin(admin: CreateAdmin, session: Session=Depends(get_session)):
    db_admin = session.exec(select(Admins).where(Admins.email == admin.email)).first()

    if db_admin:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="already account exist at this email.")
    
    new_admin = Admins(
        name = admin.name.capitalize(),
        age = admin.age,
        phone_number=admin.phone_number,
        email=admin.email,
        password=create_hash_password(admin.password)
    )
    session.add(new_admin)
    session.commit()

    return{
        "id": new_admin.id,
        "name": new_admin.name
        }


@app.post("/admin/login", status_code=status.HTTP_200_OK)
def create_login(admin: VerifyAdmin, session: Session=Depends(get_session)):
    db_admin = session.exec(select(Admins).where(Admins.email == admin.email)).first()
    if not db_admin:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid email or password!")
    if not verify_hash_password(admin.password, db_admin.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid email or password!")
    
    payload = create_token(
        {
            "id": db_admin.id,
            "email": db_admin.email
        }
    )

    return{"access_token": payload,
           "token_type": "Bearer"}
