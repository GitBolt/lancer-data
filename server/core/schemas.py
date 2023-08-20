from sqlalchemy import Column, Integer, String, Date, ForeignKey, JSON
from sqlalchemy.orm import relationship
from core.db import Base
from datetime import datetime
from sqlalchemy.sql import func

class User(Base):
    __tablename__ = 'User'

    id = Column(Integer, primary_key=True)
    githubId = Column(String(40), unique=True)
    name = Column(String(100))
    email = Column(String(255))
    twitter = Column(String(50))
    # website = Column(String(100))
    # location = Column(String(100))
    createdAt = Column(Date, default=func.now())
    contributions = relationship('Contribution', backref='User')


class Contribution(Base):
  __tablename__ = 'Contribution'

  id = Column(Integer, primary_key=True)
  user_id = Column(Integer, ForeignKey('User.id'))
  total_commits = Column(Integer)
  breakdown = Column(JSON)
  total_lines = Column(Integer)
  date = Column(Date, default=datetime.utcnow)