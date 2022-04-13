from fastapi import FastAPI
import uvicorn

from app.models.users import create_users_db
from app.models.posts import create_posts_db

import app.database as _database
import app.routers.users as _users
import app.routers.posts as _posts

app = FastAPI()

create_users_db()
create_posts_db()

app.include_router(_users.router)
app.include_router(_posts.router)

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8080, reload=True)