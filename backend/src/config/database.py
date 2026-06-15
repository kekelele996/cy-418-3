import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from src.utils.logger import logger
from src.constants.log_templates import LOG_TEMPLATES

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./legalscan.db")
if DATABASE_URL.startswith("sqlite"):
    engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
else:
    engine = create_engine(DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

class Base(DeclarativeBase):
    pass

def get_db():
    logger.info(LOG_TEMPLATES["DB_CONNECT"].format(url=DATABASE_URL.split("@")[-1]))
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
