from sqlalchemy import desc
from sqlalchemy.orm import Session
from datetime import datetime

import app.models.posts as _models
import app.schemas.posts as _schemas


def create_post(db: Session, post: _schemas.PostCreate, username: str):
	db_post = _models.Post(**post.dict(), username=username)
	db.add(db_post)
	db.commit()
	db.refresh(db_post)
	return db_post


def get_posts(db: Session, start: int, limit: int, order: str):
	#return db.query(_models.Post).order_by(desc("id")).offset(skip).limit(limit).all()
	if start == 9999999999999:
		return db.query(_models.Post.id, _models.Post.title, _models.Post.username, _models.Post.date_last_updated).order_by(desc("id")).limit(limit).all()
	elif order == "asc":
		return db.query(_models.Post.id, _models.Post.title, _models.Post.username, _models.Post.date_last_updated).order_by("id").filter(_models.Post.id >= start).limit(limit).all()
	else:
		return db.query(_models.Post.id, _models.Post.title, _models.Post.username, _models.Post.date_last_updated).order_by(desc("id")).filter(_models.Post.id <= start).limit(limit).all()
	#return db.query(_models.Post).offset(skip).limit(limit).all()

def get_my_posts(db: Session, limit: int, username: str):
	return db.query(_models.Post.id, _model_Post.title, _models.Post.date_last_updated).filter(_models.Post.username == username).order_by(desc("id")).limit(limit).all()


def get_post(db: Session, post_id: int):
	return db.query(_models.Post).filter(_models.Post.id == post_id).first()

def get_detail(db: Session, post_id: int):
	return db.query(_models.Post.detail).filter(_models.Post.id == post_id).first()


def delete_post(db: Session, post_id: int):
	db.query(_models.Post).filter(_models.Post.id == post_id).delete()
	db.commit()


def update_post(db: Session, post_id: int, post: _schemas.PostCreate):
	db_post = db.query(_models.Post).filter(_models.Post.id == post_id).first()
	db_post.title = post.title
	db_post.detail = post.detail
	db_post.date_last_updated = datetime.now()
	db.commit()
	db.refresh(db_post)
	return db_post