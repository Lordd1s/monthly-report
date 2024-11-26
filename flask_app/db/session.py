import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

from flask_app.config.settings import DATABASE

engine = create_engine(DATABASE)
SessionLocal = scoped_session(
    sessionmaker(bind=engine, autoflush=False, autocommit=False)
)
