from pydantic import BaseModel, Field, EmailStr

# class ProductSchema(BaseModel):
#     name: int = Field(default=None)
#     title: str = Field(...)
#     image: str = Field(...)
#     cost: int = Field(...)
#     quantity: int = Field(...)
#     ordering: int = Field(...)
#     is_activate: bool = Field(...)
#     comment: str = Field(...)

#     class Config:
#         schema_extra = {
#             "example": {
#                 "title": "Post title.",
#                 "content": "Post contend"
#             }
#         }


# # class UserSchema(BaseModel):
# #     fullname: str = Field(...)
# #     email: EmailStr = Field(...)
# #     password: str = Field(...)

# #     class Config:
# #         schema_extra = {
# #             "example": {
# #                 "fullname": "Joe Doe",
# #                 "email": "joe@xyz.com",
# #                 "password": "any"
# #             }
# #         }

# class UserLoginSchema(BaseModel):
#     email: EmailStr = Field(...)
#     password: str = Field(...)

#     class Config:
#         schema_extra = {
#             "example": {
#                 "email": "joe@xyz.com",
#                 "password": "any"
#             }
#         }


class ProductQuantitySchema(BaseModel):
    quantity: int
