from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# ✅ Correctly import your existing routers
from routers import provisioning, consumption, auth

# ✅ Import Base and engine only
from database.db import Base, engine

# ✅ New imports for master data routers
from routers import (
    entity,
    financial_year,
    financial_quarter,
    item_category,
    item_type,
    item_expense_type,
    gl_code,
    department,
    item
)

app = FastAPI()

# ✅ Allow frontend access (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Include your existing routers
app.include_router(provisioning.router)
app.include_router(consumption.router)
app.include_router(auth.router)

# ✅ Include new master data routers
app.include_router(entity.router)
app.include_router(financial_year.router)
app.include_router(financial_quarter.router)
app.include_router(item_category.router)
app.include_router(item_type.router)
app.include_router(item_expense_type.router)
app.include_router(gl_code.router)
app.include_router(department.router)
app.include_router(item.router)


# ✅ Create tables from your SQLAlchemy models
# This line should be present and will create tables for all models
# that inherit from Base and are imported somewhere in your application.
Base.metadata.create_all(bind=engine)

# You can optionally add a root endpoint for basic testing
@app.get("/")
def read_root():
    return {"message": "Welcome to the Business Budget Management API"}