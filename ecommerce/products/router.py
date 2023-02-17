from typing import List

from fastapi import APIRouter, Depends, Response, status, HTTPException
from sqlalchemy.orm import Session

from ecommerce import db
from . import schema
from . import services
from . import validator
router = APIRouter(
    tags=['products'],
    prefix='/products'
)


@router.post('/category', status_code=status.HTTP_201_CREATED)
async def create_category(request: schema.Category, databases: Session = Depends(db.get_db)):
    new_category = await services.create_new_category(request, databases)
    return new_category


@router.get('/category', response_model=List[schema.ListCategory])
async def get_all_categories(databases: Session = Depends(db.get_db)):
    return await services.get_all_categories(databases)


@router.get('/category/{category_id}', response_model=schema.ListCategory)
async def get_category_by_id(category_id: int, databases: Session = Depends(db.get_db)):
    return await services.get_category_by_id(category_id, databases)


@router.delete('/category/{category_id/}', status_code=status.HTTP_204_NO_CONTENT, response_class=Response)
async def remove_category_by_id(category_id: int, databases: Session = Depends(db.get_db)):
    return await services.delete_category_by_id(category_id, databases)


@router.post('/product', status_code=status.HTTP_201_CREATED)
async def create_product(request: schema.Product, databases: Session = Depends(db.get_db)):
    category = await validator.verify_category_exist(request.category_id, databases)
    if not category:
        raise HTTPException(
            status_code=400,
            detail='You have provided invalid category id.'
        )
    product = await services.create_new_product(request, databases)
    return product


async def get_all_products(databases: Session = Depends(db.get_db)):
    products = await services.get_all_products(databases)
    return products
