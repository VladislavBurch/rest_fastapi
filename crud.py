from sqlalchemy.orm import Session

from . import models, schemas


def get_product(db: Session, product_id: int):
    return db.query(models.Product).filter(models.Product.id == product_id).first()


def get_product_by_name(db: Session, name: str):
    return db.query(models.Product).filter(models.Product.name == name).first()


def get_products(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Product).offset(skip).limit(limit).all()


def create_product(db: Session, product: schemas.ProductCreate):
    db_product = models.Product(name=product.name, description=product.description)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


def update_product(db: Session, product):
    db_product = models.Product(name=product['name'], id=product['id'],
                                description=product['description'], is_available=product['is_available'])
    obj = db.query(models.Product).filter(models.Product.id == product['id']).first()
    db.delete(obj)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product
