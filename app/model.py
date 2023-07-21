from pydantic import BaseModel, Field, EmailStr

class PostSchame(BaseModel):
    id : int = Field(defould=None)
    title : str = Field(defould=None)
    content : str = Field(defould=None)
    class Config:
        schema_extra = {
            "post_demo" : {
                "title" : "post texti yoziladi",
                "content" : "content texti yoziladi"
            }
        }
    
class UserSchema(BaseModel):
    fullname : str = Field(defauld=None)  
    email : EmailStr = Field(default=None)
    password : str = Field(default=None)
    class Config:
        the_schema = {
            "user_demo" : {
                "name" : "Bekzod",
                "email" : "bkzod@gmail.com",
                "password" : "123"
            }
        }

class UserSchema(BaseModel):
    email : EmailStr = Field(default=None)
    password : str = Field(default=None)
    class Config:
        the_schema = {
            "user_demo" : {
                "email" : "bkzod@gmail.com",
                "password" : "123"
            }
        }

