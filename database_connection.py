from sqlmodel import create_engine, SQLModel
from dotenv import load_dotenv
import os
load_dotenv()

database_url=os.getenv("DATABASE_URL")

if not database_url:
    raise ValueError("Database url are not found!")

engine = create_engine(
        database_url,
        echo=True,
        pool_size=10,
        max_overflow=30
    )

def create_tables():
    SQLModel.metadata.create_all(engine)

create_tables()
