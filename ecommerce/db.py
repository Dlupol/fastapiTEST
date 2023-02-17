from sqlalchemy.ext.declarative import declarative_base
from . import config
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASES_USERNAME = config.DATABASES_USERNAME
DATABASES_PASSWORD = config.DATABASES_PASSWORD
DATABASES_HOST = config.DATABASES_HOST
DATABASES_NAME = config.DATABASES_NAME

SQLALCHEMY_DATABASES_URL = f'postgresql://{DATABASES_USERNAME}:{DATABASES_PASSWORD}@{DATABASES_HOST}/{DATABASES_NAME}'

engine = create_engine(SQLALCHEMY_DATABASES_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db(db):
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
