from typing import List

from fastapi import APIRouter, Depends, Response, status, HTTPException
from sqlalchemy.orm import Session

from ecommerce import db
from . import schema
from . import services
router = APIRouter(
    tags=['cart'],
    prefix='/cart'
)


async def add_product_to_cart(product_id: int, databases: Session = Depends(db.get_db)):
    result = await services.add_to_cart(product_id, databases)
    return result
