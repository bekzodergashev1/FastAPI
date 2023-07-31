import uvicorn
from fastapi import FastAPI, Body, Depends
from sql_app.schema import ProductQuantitySchema
from sqlalchemy import select, insert
from sqlalchemy import update as func_update
from sql_app.database import SessionLocal
from sql_app.models import Product

def get_product():
    with SessionLocal() as session:
        data = session.execute(
            select(Product)
        ).scalars().all()
    return data

def create_product(name, title, image, cost, quantity, ordering, is_active, comment):
    with SessionLocal() as session:
        data = session.execute(
            insert(Product).values(
                name=name,
                title=title,
                imge=image,
                cost=cost,
                quantity=quantity,
                ordering=ordering,
                is_active=is_active,
                comment=comment
            )
        )

        session.commit()

def update_product(product_id, data: dict):
    try:
        with SessionLocal() as session:
            session.execute(
            func_update(Product).where(Product.id == product_id).values(dict(data)))
            session.commit()
            return True
        

    except Exception as exc:
        return str(exc)


def delete_product(id):
    try:
        with SessionLocal() as session:
            product = session.query(Product).filter(Product.id == id).first()
            if product:
                session.delete(product)
                session.commit()
                return True
            else:
                return False
    except Exception as exc:
        return str(exc)



def get_item_with_id(id):
    with SessionLocal() as session:
        data = session.execute(
            select(Product).where(Product.id == id)
        ).scalar()
    return data

