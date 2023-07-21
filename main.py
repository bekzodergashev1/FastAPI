import fastapi
import uvicorn
from fastapi import FastAPI
from app.model import PostSchame




posts = [
    {
        "id" : 1,
        "title" : "Dog1 🐶",
        "text" : "Text here"
    },
    {
        "id" : 2,
        "title" : "Dog2 🐶",
        "text" : "Text here"
    },
    {
        "id" : 3,
        "title" : "Dog3 🐶",
        "text" : "Text here"
    }
]

users = []

app = FastAPI()

# Get - for testing
@app.get("/", tags=["test"])
def greet():
    return {"Hello":"World"}

# Get Post
@app.get("/post", tags=["posts"])
def get_posts():
    return {"data" : posts}

# Get single post{id}
@app.get("/post/{id}", tags=["posts"])
def get_one_post(id : int):
    if id > len(posts):
        return {
            "eror":"Post with thir ID does not exist"
        }
    for post in posts:
        if post["id"] == id:
            return {
                "data" : post
            }

# Post a blog post
@app.post("/posts", tags=["posts"])
def add_post(post : PostSchame):
    post.id = len(posts) + 1
    posts.append(post.dict())
    return {
        "info":"Post Added!"
    }
