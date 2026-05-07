from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from services.user_services import get_users, get_user, create_user, update_user, delete_user
from schemas.user_schemas import UserCreate, UserUpdate, UserResponse, userdelete

router = APIRouter(
    prefix="/users",
    tags=["users"],
)

@router.get("/", response_model=list[UserResponse])
def get_all_users(db: Session = Depends(get_db)):
    return get_users(db)

@router.get("/{user_id}", response_model=UserResponse)
def get_user_by_id(user_id: int, db: Session = Depends(get_db)):
    user = get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.post("/", response_model=UserResponse)
def create_new_user(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user)

@router.put("/{user_id}", response_model=UserResponse)
def update_existing_user(user_id: int, user: UserUpdate, db: Session = Depends(get_db)):
    updated_user = update_user(db, user_id, user)
    if not updated_user:
        raise HTTPException(status_code=404, detail="User not found")
    return updated_user

@router.delete("/{user_id}")
def delete_existing_user(user_id: int, user_delete: userdelete, db: Session = Depends(get_db)):
    user = delete_user(db, user_id, user_delete)
    if not user:
        raise HTTPException(status_code=404, detail="User not found or invalid password")
    return {"message": "User deleted successfully"}
