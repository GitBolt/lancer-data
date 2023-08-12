from sqlalchemy import Column, Integer, String, Date, ForeignKey, JSON
from sqlalchemy.orm import relationship
from core.db import Base
from datetime import datetime


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    github_name = Column(String(40), unique=True)
    name = Column(String(100))
    email = Column(String(255))
    twitter = Column(String(50))
    website = Column(String(100))
    location = Column(String(100))

    contributions = relationship('Contribution', backref='user')


class Contribution(Base):
  __tablename__ = 'contribution'

  id = Column(Integer, primary_key=True)
  user_id = Column(Integer, ForeignKey('user.id'))
  total_commits = Column(Integer)
  breakdown = Column(JSON)
  date = Column(Date, default=datetime.utcnow)