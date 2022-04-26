from typing import List
from datetime import datetime
from pydantic import BaseModel

class _PostBase(BaseModel):
	title: str
	detail: str


class PostCreate(_PostBase):
	#email: str
	pass


class Post(_PostBase):
	id: int
	username: str
	date_created: datetime
	date_last_updated: datetime

	class Config:
		orm_mode = True


class PostsList(BaseModel):
	id: int
	title: str
	username: str
	date_last_updated: datetime

	class Config:
		orm_mode = True

class Content(BaseModel):
	detail: str

	class Config:
		orm_mode = True

class PostResult(BaseModel):
	title: str

	class Config:
		orm_mode = True