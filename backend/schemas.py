from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    email: str
    password: str

class User(BaseModel):
    id: int
    username: str
    email: str
    password: str

    class Config:
        orm_mode = True

class UserResponse(BaseModel):
    id: int
    username: str
    email: str
   # password: str

    class Config:
        orm_mode = True

class TweetCreate(BaseModel):
    tweet: str
    user_id: int
    tags: str

class Tweet(BaseModel):
    id: int
    tweet: str
    user_id: int
    tags: str

    class Config:
        orm_mode = True

class TweetResponse(BaseModel):
    id: int
    tweet: str
    user_id: int
    tags: str

    class Config:
        orm_mode = True