# 🛒 E-commerce API

A modular REST API for e-commerce built with **FastAPI**, **PostgreSQL** and **Redis**, designed with scalability and clean architecture in mind.

> 🔗 **Live demo:** https://ecommerce-api-rsy4.onrender.com/docs

---

## 🏗️ Architecture

The project follows a **modular service-based architecture**, where each business domain (auth, products, orders) is fully isolated with its own models, schemas, and routes.

ecommerce-api/
├── services/
│   ├── auth/        # JWT authentication
│   ├── products/    # Product catalog & stock
│   └── orders/      # Order management
├── core/
│   ├── config.py    # Settings via Pydantic
│   ├── database.py  # Async SQLAlchemy engine
│   ├── redis.py     # Redis connection
│   └── security.py  # JWT helpers & password hashing
├── main.py
├── Dockerfile
└── docker-compose.yml
---

## 🚀 Tech Stack

| Technology | Purpose |
|---|---|
| **FastAPI** | Async REST framework |
| **PostgreSQL** | Primary relational database |
| **Redis** | Session cache & future queue support |
| **SQLAlchemy (async)** | ORM with async support |
| **Docker & Docker Compose** | Containerization |
| **JWT (python-jose)** | Stateless authentication |
| **Pydantic v2** | Data validation & settings |

---

## 📦 Features

- ✅ JWT authentication (register, login, refresh token)
- ✅ Product catalog with pagination and search
- ✅ Stock management
- ✅ Order creation with **atomic transaction** (order + stock decrement in a single DB transaction)
- ✅ Order status flow: `pending → confirmed → shipped → delivered`
- ✅ Async database access throughout
- ✅ Auto-generated OpenAPI documentation

---

## 🔌 API Endpoints

### Auth
| Method | Endpoint | Description |
|---|---|---|
| POST | `/auth/register` | Create new user |
| POST | `/auth/login` | Login and get tokens |
| POST | `/auth/refresh` | Refresh access token |

### Products
| Method | Endpoint | Description |
|---|---|---|
| GET | `/products` | List products (paginated) |
| POST | `/products` | Create product |
| GET | `/products/{id}` | Get product by ID |
| PATCH | `/products/{id}` | Update product |
| PATCH | `/products/{id}/stock` | Update stock |

### Orders
| Method | Endpoint | Description |
|---|---|---|
| POST | `/orders` | Create order |
| GET | `/orders/{id}` | Get order by ID |
| PATCH | `/orders/{id}/status` | Update order status |

---

## ⚙️ Running locally

### Prerequisites
- Docker & Docker Compose
- Git

### Steps

```bash
# Clone the repository
git clone https://github.com/AllanTrautm4nn/ecommerce-api.git
cd ecommerce-api

# Create the environment file
cp .env.example .env

# Start all services
docker-compose up --build
```

API will be available at **http://localhost:8000/docs**

---

## 🧠 Architecture Decisions

**Why modular structure instead of monolith?**  
Each service can evolve independently. Adding a new domain (e.g. payments) requires no changes to existing services.

**Why PostgreSQL + Redis together?**  
PostgreSQL handles persistent relational data. Redis is used for session management and is already in place for future async task queuing (e.g. order confirmation emails).

**Why async SQLAlchemy?**  
FastAPI is async-first. Using sync ORM would block the event loop and defeat the purpose of an async framework.

**Why atomic transaction on order creation?**  
Creating an order and decrementing stock must succeed or fail together. A partial failure (order created but stock not updated) would cause data inconsistency.

---

## 👨‍💻 Author

**Allan Trautmann**  
[GitHub](https://github.com/AllanTrautm4nn) · [LinkedIn](#)

---

## 📄 License

MIT

