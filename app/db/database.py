import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#evita fallos de ruta
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_DIR = os.path.join(BASE_DIR, "sqlite_base")

if not os.path.exists(DB_DIR):
    os.makedirs(DB_DIR)



url=f"sqlite:///{os.path.join(DB_DIR, 'databsearn.db')}"
motor = create_engine(url, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=motor)

Base = declarative_base()





