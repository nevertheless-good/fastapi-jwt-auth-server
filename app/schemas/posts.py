from typing import List
from datetime import datetime
from pydantic import BaseModel

class _PostBase(BaseModel):
	title: str
	content: str


class PostCreate(_PostBase):
	#email: str
	pass


class Post(_PostBase):
	id: int
	email: str
	title: str
	content: str
	date_created: datetime
	date_last_updated: datetime

	class Config:
		orm_mode = True