from datetime import datetime
from sqlalchemy import Column, String, Integer, Boolean, DateTime

import app.database.connection as _database

class Post(_database.Base):
	__tablename__ = "posts"
	id = Column(Integer, primary_key=True, index=True)
	title = Column(String(255), index=True)
	detail = Column(String(1024), index=False)
	username = Column(String(255), index=False)
	date_created = Column(DateTime, default=datetime.utcnow)
	date_last_updated = Column(DateTime, default=datetime.utcnow)


def create_posts_db():
	_database.Base.metadata.create_all(_database.engine)