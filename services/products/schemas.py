from pydantic import BaseModel
from typing import Optional
import uuid

class ProductCreate(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    stock: int = 0

class ProductUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    is_active: Optional[bool] = None

class StockUpdate(BaseModel):
    quantity: int

class ProductResponse(BaseModel):
    id: uuid.UUID
    name: str
    description: Optional[str]
    price: float
    stock: int
    is_active: bool

    model_config = {"from_attributes": True}

class ProductListResponse(BaseModel):
    items: list[ProductResponse]
    total: int
    page: int
    page_size: int