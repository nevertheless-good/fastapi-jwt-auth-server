from sqlalchemy.orm import Session


import app.models.users as _models
import app.schemas.users as _schemas


def get_user_by_email(db: Session, email: str):
	return db.query(_models.User).filter(_models.User.email == email).first()


def create_user(db: Session, user: _schemas.UserCreate):
	db_user = _models.User(email=user.email, hashed_password=user.password)
	db.add(db_user)
	db.commit()
	db.refresh(db_user)
	return db_user


def get_users(db: Session, skip: int, limit: int):
	return db.query(_models.User).offset(skip).limit(limit).all()


def get_user(db: Session, user_id: int):
	return db.query(_models.User).filter(_models.User.id == user_id).first()