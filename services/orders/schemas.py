from pydantic import BaseModel
from typing import Optional
import uuid
from services.orders.models import OrderStatus

class OrderItemCreate(BaseModel):
    product_id: uuid.UUID
    quantity: int

class OrderCreate(BaseModel):
    items: list[OrderItemCreate]

class OrderItemResponse(BaseModel):
    id: uuid.UUID
    product_id: uuid.UUID
    product_name: str
    quantity: int
    unit_price: float

    model_config = {"from_attributes": True}

class OrderResponse(BaseModel):
    id: uuid.UUID
    user_id: uuid.UUID
    status: OrderStatus
    total: float
    items: list[OrderItemResponse]

    model_config = {"from_attributes": True}

class OrderStatusUpdate(BaseModel):
    status: OrderStatus