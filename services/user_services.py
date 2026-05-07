from sqlalchemy.orm import Session
from models.user import User
from schemas.user_schemas import UserCreate, UserUpdate, userdelete
import bcrypt
from datetime import datetime
from typing import Optional

def get_password_hash(password: str):
    # Truncate password to 72 bytes (bcrypt limit) and encode to bytes
    password_bytes = password.encode('utf-8')[:72]
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password_bytes, salt).decode('utf-8')
def verify_password(password: str, hashed_password: str):
    password_bytes = password.encode('utf-8')[:72]
    hashed_password_bytes = hashed_password.encode('utf-8')
    return bcrypt.checkpw(password_bytes, hashed_password_bytes)
def get_users(db: Session):
    return db.query(User).all()

def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def create_user(db: Session, user: UserCreate):
    hashed_password = get_password_hash(user.password)
    db_user = User(
        name=user.name,
        email=user.email,
        hashed_password=hashed_password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user(db: Session, user_id: int, user: UserUpdate):
    db_user = db.query(User).filter(User.id == user_id).first()
    if not verify_password(user.password, db_user.hashed_password):
        raise ValueError("Invalid password")
    if db_user:
        for key, value in user.dict().items():
            setattr(db_user, key, value)
        db.commit()
        db.refresh(db_user)
    return db_user

def delete_user(db: Session, user_id: int, user_delete: userdelete):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user and verify_password(user_delete.password, db_user.hashed_password):
        # Soft delete - set delete_ts instead of removing record
        db_user.delete_ts = datetime.utcnow()
        db.commit()
        db.refresh(db_user)
    return db_user