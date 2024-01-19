from fastapi import FastAPI
from pydantic import BaseModel


class Products(BaseModel):
    name : str
    category: str = "general"
    serial_no: str | None
    
    
class ProductDetails(BaseModel):
    """response model for product details"""
    
    product_id: int
    name : str
    
    
app = FastAPI(
    title="Intro to fastapi",
    summary="We're getting our selves started with fastapi",
)

@app.get("/")
def index(product_id) -> str:
    """this is the index"""
    
    return  "Hello world"


# path parameters
@app.get("/proucts/", response_model=ProductDetails)
def product_details(product_id: int, name: str = None) -> dict:
    """returns the id"""
    
    if not name:
        name = "sammy"
        
    return {
        "product_id": product_id,
        "name": name,
    }
    
    
@app.post("/products/create", status_code=201)
def create_products(payload: Products) -> dict:
    """creates a product"""
    
    return payload.model_dump()