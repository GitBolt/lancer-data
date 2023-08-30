from sqlalchemy import Column, Integer, String, Date, ForeignKey, JSON, Boolean, DateTime
from sqlalchemy.orm import relationship
from db import Base, Base2
from datetime import datetime
from sqlalchemy.sql import func

class User(Base):
    __tablename__ = 'User'

    id = Column(Integer, primary_key=True)
    githubId = Column(String(40), unique=True)
    name = Column(String(100))
    email = Column(String(255))
    profileWalletId = Column(String(50))
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


"""RELEASE 1 DATABASE"""

class User1(Base2):
    __tablename__ = 'User'

    id = Column(Integer, primary_key=True, autoincrement=True)
    isAdmin = Column(Boolean)
    verified = Column(Boolean)
    hasProfileNFT = Column(Boolean)
    githubId = Column(String(24))
    githubLogin = Column(String(64))
    name = Column(String(128))
    discord = Column(String(64))
    twitter = Column(String(64))
    instagram = Column(String(64))
    email = Column(String(128), unique=True)
    profileWalletId = Column(Integer, unique=True)
    createdAt = Column(String(24), nullable=False)
    refferralTreasuryKey = Column(String(128))
    referralId = Column(String(128))
    googleId = Column(String(64))
    picture = Column(String(2000))
    hasFinishedOnboarding = Column(Boolean, default=0)
    bio = Column(String(2000))
    company = Column(String(128))
    linkedin = Column(String(64))
    position = Column(String(128))
    website = Column(String(128))
    github = Column(String(64))
  
    badges = relationship("UnclaimedBadge", backref="User")


class UnclaimedBadge(Base2):
    __tablename__ = 'UnclaimedBadge'

    id = Column(Integer, primary_key=True, autoincrement=True)
    details = Column(JSON)
    dateCreated = Column(DateTime(timezone=True), server_default=func.now())

    user_id = Column(Integer, ForeignKey('User.id'))


class Wallet(Base):
    __tablename__ = 'Wallet'

    id = Column(Integer, primary_key=True, autoincrement=True)
    publicKey = Column(String(64), unique=True)
    isDefault = Column(Boolean)
    userid = Column(Integer, nullable=False)
    hasProfileNFT = Column(Boolean)
    hasBeenInitialized = Column(Boolean)