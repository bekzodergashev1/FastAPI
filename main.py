import uvicorn
from fastapi import FastAPI, Body, Depends
from sqlalchemy import select, insert, delete, update
from sql_app.database import SessionLocal

# from sql_app.schema import PostSchema, UserSchema, UserLoginSchema
from sql_app.auth.auth_bearer import JWTBearer
from sql_app.auth.auth_handler import signJWT
from sql_app.models import Product

def get_product():
    with SessionLocal() as session:
        data = session.execute(
            select(Product)
        ).scalars().all()
    return data

def create_product(name, title, image, cost):
    with SessionLocal() as session:
        data = session.execute(
            insert(Product).values(
                name=name,
                title=title,
                imge=image,
                cost=cost
            )
        )
        session.commit()

def update_product(id, quantity):
    with SessionLocal() as session:
        session.execute(
            update(Product).where(
                Product.id == id
            ).values(
                quantity=quantity,
            )
        )
        session.commit()


def delete_product(id):
    with SessionLocal() as session:
        session.execute(
            delete(Product).where(Product.id == id)
        )
        session.commit()


def get_item_with_id(id):
    with SessionLocal() as session:
        data = session.execute(
            select(Product).where(Product.id == id)
        ).scalar()
    return data


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
def add(name: str, title: str, image: str, cost: int):
    data = create_product(name, title, image, cost)
    return {"message": "created"}


@app.put("/{id}")
def update(id: int, name: str, title: str, image: str, coast: int):
    data = update_product(id, name, title, image, coast)
    return {"message": "updated"}


@app.delete("/delete/{id}")
def delete(id: int):
    data = delete_product(id)
    return {"message": "deleted"}



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


