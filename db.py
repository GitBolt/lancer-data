from sqlalchemy import create_engine

from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship, DeclarativeBase

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    github_name = Column(String(40), unique=True)
    name = Column(String(100))
    email = Column(String(255))
    twitter = Column(String(50))
    website = Column(String(100))
    location = Column(String(100))

    contributions = relationship('Contribution', backref='user')

class Contribution(Base):
    __tablename__ = 'contributions'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))

    Typescript = Column(Integer)
    Javascript = Column(Integer)
    Rust = Column(Integer)
    Python = Column(Integer)
    C = Column(Integer)
    CSS = Column(Integer)
    HTML = Column(Integer)
    Golang = Column(Integer)
    Solidity = Column(Integer)
    CPP = Column(Integer)

    total_commits = Column(Integer)
    date = Column(Date)



connection_string = "mysql+mysqlconnector://bolt:bolt@localhost:3306/lancer"
engine = create_engine(connection_string, echo=True)

Base.metadata.create_all(engine)