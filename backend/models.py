from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base 

class UserModel(Base): 
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)

    # relationship
    tweets = relationship("TweetsModel", back_populates="users")

class TweetsModel(Base): 
    __tablename__ = "tweets"

    id = Column(Integer, primary_key=True, index=True)
    tweet = Column(String, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), index=True)
    tags = Column(String, index=True)

    # relationship
    users = relationship("UserModel", back_populates="tweets")