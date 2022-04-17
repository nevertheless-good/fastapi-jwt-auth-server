from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

import app.database.connection as _database
import app.services.posts as _posts
import app.services.users as _users
import app.schemas.posts as _schemas
import app.auth.authenticate as _auth


auth_handler = _auth.AuthHandler()

conn_db = Depends(_database.get_db)

router = APIRouter()


@router.get("/posts", response_model=List[_schemas.Post])
def read_posts(skip: int = 0, limit: int = 10, db: Session=conn_db, username=Depends(auth_handler.auth_access_wrapper)):
	db_posts = _posts.get_posts(db=db, skip=skip, limit=limit)
	return db_posts


@router.post("/posts", status_code=201, response_model=_schemas.Post)
def create_post(post: _schemas.PostCreate, db: Session=conn_db, username=Depends(auth_handler.auth_access_wrapper)):
#	db_user = _users.get_user_by_email(db=db, email=username)
#	if db_user is None:
#		raise HTTPException(status_code=401, detail="Unauthorized")
	return _posts.create_post(db=db, post=post, email=username)


@router.get("/posts/my_post", response_model=List[_schemas.Post])
def read_my_post(skip: int = 0, limit: int = 10, db: Session=conn_db, username=Depends(auth_handler.auth_access_wrapper)):
	db_posts = _posts.get_my_posts(db=db, skip=skip, limit=limit, email=username)
	return db_posts

@router.get("/posts/{post_id}", response_model=_schemas.Post)
def read_post(post_id: int, db: Session=conn_db, username=Depends(auth_handler.auth_access_wrapper)):
	db_post = _posts.get_post(db=db, post_id=post_id)
	if db_post is None:
		raise HTTPException(status_code=404, detail="This post does not exist")
	return db_post


@router.delete("/posts/{post_id}")
def delete_post(post_id: int, db: Session=conn_db, username=Depends(auth_handler.auth_access_wrapper)):
	db_post = _posts.get_post(db=db, post_id=post_id)
	if db_post is None:
		raise HTTPException(status_code=404, detail="This post does not exist") 
	if db_post.email != username:
		raise HTTPException(status_code=401, detail="Unauthorized")
	_posts.delete_post(db=db, post_id=post_id)
	return {"message" : f"successfully deleted post with id: {post_id}"}


@router.put("/posts/{post_id}", response_model=_schemas.Post)
def update_post(post_id: int, post: _schemas.PostCreate, db: Session=conn_db, username=Depends(auth_handler.auth_access_wrapper)):
	db_post = _posts.get_post(db=db, post_id=post_id)
	if db_post is None:
		raise HTTPException(status_code=404, detail="This post does not exist") 
	if db_post.email != username:
		raise HTTPException(status_code=401, detail="Unauthorized")
	return _posts.update_post(db=db, post_id=post_id, post=post)