from sqlalchemy import create_engine
from typing import Callable
import os
from dotenv import load_dotenv
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

load_dotenv()

def initialize_engine() -> Callable:
    try:
        return create_engine(os.environ["DB_URL"])
    except KeyError:
        print(
            "'DB_URL' environment variable not found,",
            "creating 'db.sql' locally...'"
            )
        return create_engine(
                            "sqlite:///../db.sql", 
                            connect_args={"check_same_thread": False}
                            )

engine = initialize_engine()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def initialize_engine2() -> Callable:
    try:
        return create_engine(os.environ["DB_URL_RELEASE"])
    except KeyError:
        print(
            "'DB_URL_RELEASE' environment variable not found,",
            "creating 'db2.sql' locally...'"
            )
        return create_engine(
                            "sqlite:///../db2.sql", 
                            connect_args={"check_same_thread": False}
                            )

engine2 = initialize_engine2()

SessionLocal2 = sessionmaker(autocommit=False, autoflush=False, bind=engine2)
Base2 = declarative_base()
