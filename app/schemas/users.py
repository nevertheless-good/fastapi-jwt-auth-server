from typing import List
from datetime import datetime
from pydantic import BaseModel


class _UserBase(BaseModel):
	username: str


class UserCreate(_UserBase):
	password: str


class User(_UserBase):
	id: int
	is_active: bool

	class Config:
		orm_mode = True

class UpdateToken(BaseModel):
    access_token: str = None


class LoginToken(BaseModel):
	access_token: str = None
	refresh_token: str = None