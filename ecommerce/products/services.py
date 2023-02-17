from typing import List

from fastapi import HTTPException
from starlette import status

from . import models


async def create_new_category(request, databases) -> models.Category:
    new_category = models.Category(name=request.name)
    databases.add(new_category)
    databases.commit()
    databases.refresh(new_category)
    return new_category


async def get_all_categories(databases) -> List[models.Category]:
    categories = databases.query(models.Category).all()
    return categories


async def get_category_by_id(category_id, databases) -> models.Category:
    category_info = databases.query(models.Category).get(category_id)
    if not category_info:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Data not found')
    return category_info


async def delete_category_by_id(category_id, databases) -> models.Category:
    databases.query(models.Category).filter(models.Category.id == category_id).delete()
    databases.commit()


async def create_new_product(request, databases) -> models.Product:
    new_product = models.Product(name=request.name,
                                 quantity=request.quantity,
                                 description=request.description,
                                 price=request.price,
                                 category_id=request.category_id)
    databases.add(new_product)
    databases.commit()
    databases.refresh(new_product)
    return new_product


async def get_all_products(databases) -> List[models.Product]:
    products = databases.query(models.Product).all()
    return products
