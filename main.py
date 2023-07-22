import fastapi
import uvicorn
from fastapi import FastAPI, Body
from app.model import PostSchame, UserSchema, UserLoginSchema
from app.auth.jwt_handler import signJWT


    
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

# User Signup [create a new user]
@app.post("user/signin", tags=["user"])
def user_signup(user : UserSchema = Body(defould=None)):
    users.append(user)
    return signJWT(user.email)

def Check_user(data : UserLoginSchema):
    for user in users:
        if user.email == data.email and user.password == data.passwod:
            return True
        return False
    
@app.post("/user/login", tags=["user"])
def user_login(user: UserLoginSchema = Body(default=None)):
    if Check_user(user):
        return signJWT(user.email)
    else:
        return{
            "eror":"Invalit login datails"
        }
    
