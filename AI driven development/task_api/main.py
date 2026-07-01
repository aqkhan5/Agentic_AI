from itertools import product

from fastapi import Depends, FastAPI
from model import Product
from database import session_neon
import database_model
from sqlalchemy.orm import Session

def get_db():
    db = session_neon()
    try:
        yield db
    finally:
        db.close()

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Task API")

# Enable CORS for frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins for development
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

database_model.Base.metadata.create_all(bind=session_neon().get_bind())  # Create tables if they don't exist


@app.get("/API")
def read_root():
    return {"message": "Task API is running", "version": "1.0.0"}


products = [
    Product(id=1, name="Floor Lamp", description="Description of Product 1", price=29.99, quantity=10),
    Product(id=2, name="Table Lamp", description="Description of Product 2", price=19.99, quantity=5),
    Product(id=3, name="Desk Lamp", description="Description of Product 3", price=39.99, quantity=8),
    Product(id=4, name="Chair", description="Description of Product 4", price=49.99, quantity=12)

]

# putting the data in the database
def init_db():
    db = session_neon()
    for product in products:
        # Check if a product with this ID already exists
        exists = db.query(database_model.Product).filter_by(id=product.id).first()
        if not exists:
            db.add(database_model.Product(**product.model_dump()))
    db.commit()
    db.close()


# get all products endpoint
@app.get("/products")
def get_products(db: Session = Depends(get_db)):
    db_products =db.query(database_model.Product).all()
    return db_products

# get product endpoint
@app.get("/product/{id}")
def get_product(id: int, db: Session = Depends(get_db)):
    db_product = db.query(database_model.Product).filter(database_model.Product.id == id).first()
    if db_product:
            return db_product
    return {"error": "Product not found"}

@app.post("/product")
def create_product(product: Product, db: Session = Depends(get_db)):
    db_product = (database_model.Product(**product.model_dump()))
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


# update product endpoint
@app.put("/product/{id}")
def update_product(id: int, product: Product, db: Session = Depends(get_db)):
    db_product = db.query(database_model.Product).filter(database_model.Product.id == id).first()
    if not db_product:
        return {"error": "Product not found"}
    
    db_product.name = product.name
    db_product.description = product.description
    db_product.price = product.price
    db_product.quantity = product.quantity
    
    db.commit()
    db.refresh(db_product)
    return db_product

# delete product endpoint
@app.delete("/product/{id}")
def delete_product(id: int, db: Session = Depends(get_db)):
    db_product = db.query(database_model.Product).filter(database_model.Product.id == id).first()
    if not db_product:
        return {"error": "Product not found"}
    
    db.delete(db_product)
    db.commit()
    return db_product
