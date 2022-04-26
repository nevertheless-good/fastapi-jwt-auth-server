from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

import app.database.connection as _database
import app.services.users as _users
import app.schemas.users as _schemas
import app.auth.authenticate as _auth


auth_handler = _auth.AuthHandler()

conn_db = Depends(_database.get_db)

router = APIRouter()


@router.post("/register", status_code=201, response_model=_schemas.User)
def create_user(user: _schemas.UserCreate, db: Session=conn_db):
	db_user = _users.get_user_by_username(db=db, username=user.username)
	if db_user:
		raise HTTPException(status_code=400, detail="The E-Mail is already used")
	user.password = auth_handler.get_password_hash(user.password)
	return _users.create_user(db=db, user=user)

@router.post("/login", response_model=_schemas.LoginToken)
def login_user(user: _schemas.UserCreate, db: Session=conn_db):
	db_user = _users.get_user_by_username(db=db, username=user.username)
	if db_user is None:
		raise HTTPException(status_code=401, detail="The E-Mail is not exist")
	is_verified = auth_handler.verify_password(user.password, db_user.hashed_password)
	if not is_verified:
		raise HTTPException(status_code=401, detail="Password does not matched")
	return auth_handler.encode_login_token(user.username)


@router.get("/users", response_model=List[_schemas.User])
def read_user(skip: int=0, limit: int=10, db: Session=conn_db, username=Depends(auth_handler.auth_access_wrapper)):
	if username is None:
		raise HTTPException(status_code=401, detail="not authorization")
	db_users = _users.get_users(db=db, skip=skip, limit=limit)
	return db_users

@router.get("/update_token", response_model=_schemas.UpdateToken)
def update_token(username=Depends(auth_handler.auth_refresh_wrapper)):
	if username is None:
		raise HTTPException(status_code=401, detail="not authorization")
	return auth_handler.encode_login_token(username)