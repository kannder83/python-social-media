
from fastapi import FastAPI
from . import models
from .database import engine
from .routes import user, post, auth
from .config import settings

# configuration DB
models.Base.metadata.create_all(bind=engine)

app: FastAPI = FastAPI()


app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)


@app.get(path="/")
def root():
    return {"message": "Hello World!"}
