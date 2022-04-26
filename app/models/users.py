from datetime import datetime
from sqlalchemy import Column, String, Integer, Boolean, DateTime

import app.database.connection as _database

class User(_database.Base):
	__tablename__ = "users"
	id = Column(Integer, primary_key=True, index=True)
	username = Column(String(255), unique=True, index=True)
	hashed_password = Column(String(255))
	is_active = Column(Boolean, default=True)

def create_users_db():
	_database.Base.metadata.create_all(_database.engine)