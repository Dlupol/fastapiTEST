from fastapi import Depends, status, HTTPException
from sqlalchemy.orm import Session

from ecommerce import db
from .models import Cart, CartItems
from ecommerce.products.models import Product
from ecommerce.user.models import User


async def add_to_cart(product_id, databases: Session = Depends(db.get_db)):
    product_info = databases.query(Product).get(product_id)
    if not product_id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Data not found')

    if product_info.quntity <= 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Item out of stock')

    # user_info = databases.query(User).