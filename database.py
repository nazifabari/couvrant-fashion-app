from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
import os
from dotenv import load_dotenv

load_dotenv()
URL = os.getenv("URL")

engine = create_engine(URL)
SessionLocal = sessionmaker(engine)

class Base(DeclarativeBase):
    pass