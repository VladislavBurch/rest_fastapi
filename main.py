from typing import List

from fastapi import Depends, FastAPI, HTTPException, Response
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/products/", response_model=schemas.Product)
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    db_product = crud.get_product_by_name(db, name=product.name)
    if db_product:
        raise HTTPException(status_code=400, detail="Product with this name already exists")
    return crud.create_product(db=db, product=product)


@app.get("/products/", response_model=List[schemas.Product])
def read_products(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    products = crud.get_products(db, skip=skip, limit=limit)
    return products


@app.put("/products/{product_id}", response_model=schemas.Product)
def update_product(product_id, product: schemas.Product, db: Session = Depends(get_db)):
    update_product_encoded = jsonable_encoder(product)
    return crud.update_product(db=db, product=update_product_encoded)


@app.get("/products/{product_id}", response_model=schemas.Product)
def read_product(product_id: int, db: Session = Depends(get_db)):
    db_product = crud.get_product(db, product_id=product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product


@app.get("/products/{product_id}/json", response_model=schemas.Product)
def read_product_json(product_id: int, db: Session = Depends(get_db)):
    db_product = crud.get_product(db, product_id=product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product


@app.get("/users/{product_id}/xml", response_model=schemas.Product)
def read_product_xml(product_id: int, db: Session = Depends(get_db)):
    db_product = crud.get_product(db, product_id=product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    data = f"""<?xml version="1.0"?>
    <product>
    <heading>product id= {db_product.id}</heading>
    <body>
        name: {db_product.name}
        is_available: {db_product.is_available}
        description: {db_product.description}
    </body>
</product>
    """
    return Response(content=data, media_type="application/xml")
