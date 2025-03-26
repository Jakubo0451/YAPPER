from fastapi import APIRouter, Depends
from typing import List
from sqlalchemy.orm import Session
from database import get_db
from models import UserModel
from schemas import UserCreate, UserResponse

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

@router.get("", response_model=List[UserResponse])
def read_users(db: Session = Depends(get_db)):
    users = db.query(UserModel).all()
    return users


@router.post("", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    user = UserModel(username=user.username, email=user.email, password=user.password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

@router.delete("/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(UserModel).filter(UserModel.id == user_id).first()
    db.delete(user)
    db.commit()
    return {"message": "User deleted successfully"}

# login and logout routes
@router.post("/login")
def login():
    return {"message": "login successful"}

@router.post("/logout")
def logout():
    return {"message": "logout successful"}