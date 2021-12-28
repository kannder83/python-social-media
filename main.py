from typing import Optional
from fastapi import FastAPI
from fastapi import Body
from pydantic import BaseModel

app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


@app.get(path="/")
def root():
    return {"message": "Hello World!"}


@app.get(path="/posts")
def get_post():
    return{"data": "this is your posts"}


@app.post(path="/createposts")
def create_posts(post: Post):
    print(post)
    print(post.dict())
    return {"data": post}
