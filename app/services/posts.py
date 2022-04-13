from sqlalchemy.orm import Session
from datetime import datetime

import app.models.posts as _models
import app.schemas.posts as _schemas


def create_post(db: Session, post: _schemas.PostCreate, email: str):
	db_post = _models.Post(**post.dict(), email=email)
	db.add(db_post)
	db.commit()
	db.refresh(db_post)
	return db_post


def get_posts(db: Session, skip: int, limit: int):
	return db.query(_models.Post).offset(skip).limit(limit).all()

def get_my_posts(db: Session, skip: int, limit: int, email: str):
	return db.query(_models.Post).filter(_models.Post.email == email).offset(skip).limit(limit).all()


def get_post(db: Session, post_id: int):
	return db.query(_models.Post).filter(_models.Post.id == post_id).first()


def delete_post(db: Session, post_id: int):
	db.query(_models.Post).filter(_models.Post.id == post_id).delete()
	db.commit()


def update_post(db: Session, post_id: int, post: _schemas.PostCreate):
	db_post = get_post(db=db, post_id=post_id)
	db_post.title = post.title
	db_post.content = post.content
	db_post.date_last_updated = datetime.now()
	db.commit()
	db.refresh(db_post)
	return db_post