from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Float, DateTime, ARRAY, func
from sqlalchemy.orm import Mapped, mapped_column
from typing_extensions import Annotated

from .database import Base

intpk = Annotated[int, mapped_column(primary_key=True)]

class Product(Base):
    __tablename__ = "products"
    id: Mapped[intpk]
    title = Column(String, nullable=False)
    name = Column(String, nullable=False)
    imge = Column(String, nullable=True)
    cost = Column(Float, default=0)
    quantity = Column(Integer ,default=0)
    ordering = Column(Integer, nullable=True)
    is_active = Column(Boolean, default=False, nullable=False)
    comment = Column(String, nullable=True)

    def __str__(self):
        return self.name