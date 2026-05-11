from fastapi import FastAPI
from contextlib import asynccontextmanager
from core.database import engine, Base
from services.auth.routes import router as auth_router
from services.products.routes import router as products_router
from services.orders.routes import router as orders_router
from services.auth.models import User
from services.products.models import Product
from services.orders.models import Order, OrderItem

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield

app = FastAPI(
    title="E-commerce API",
    description="Modular e-commerce REST API built with FastAPI, PostgreSQL and Redis",
    version="1.0.0",
    lifespan=lifespan
)

app.include_router(auth_router)
app.include_router(products_router)
app.include_router(orders_router)

@app.get("/health")
async def health():
    return {"status": "ok", "version": "1.0.0"}