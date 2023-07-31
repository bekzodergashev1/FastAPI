import uvicorn
from fastapi import FastAPI
from sql_app.schema import ProductQuantitySchema
from sqlalchemy import select, insert
from sqlalchemy import update as func_update
from crud import get_product, get_item_with_id, create_product, update_product, delete_product

from sql_app.auth.auth_bearer import JWTBearer
from sql_app.auth.auth_handler import signJWT
from sql_app.models import Product


users = []

app = FastAPI()



# testing
@app.get("/", tags=["test"])
def greet():
    data = get_product()
    # result = []
    # for i in data:
    #     result.append({
    #         'id': i.id,
    #         'name': i.name,
    #         'title': i.title,
    #         'image': i.imge,
    #         'cost': i.cost            
    #     })
    return data


@app.get("/{id}")
def getitem(id:int):
    data = get_item_with_id(id)
    return data


@app.post("/create")
def add(name: str, title: str, image: str, cost: int, quantity: int, ordering: int, is_active: bool, comment: str):
    data = create_product(name, title, image, cost, quantity, ordering, is_active, comment)
    return {"message": "created"}


@app.patch("/{product_id}")
def update(product_id: int, data: ProductQuantitySchema):
    return update_product(product_id=product_id, data=data)


@app.delete("/delete/{id}")
def delete(id: int):
    data = delete_product(id)
    return {"message": data}



# @app.post("/user/signup", tags=["user"])
# def create_user(user: UserSchema = Body(...)):
#     users.append(user)  # replace with db call, making sure to hash the password first
#     return signJWT(user.email)


# @app.post("/user/login", tags=["user"])
# def user_login(user: UserLoginSchema = Body(...)):
#     if check_user(user):
#         return signJWT(user.email)
#     return {
#         "error": "Wrong login details!"
#     }


