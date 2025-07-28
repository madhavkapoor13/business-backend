from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# ✅ Correctly import your routers
from routers import provisioning, consumption

# ✅ Import Base and engine only
from database.db import Base, engine
from routers import auth

app = FastAPI()

# ✅ Allow frontend access (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Include your routers
app.include_router(provisioning.router)
app.include_router(consumption.router)
app.include_router(auth.router)

# ✅ Create tables from your SQLAlchemy models
Base.metadata.create_all(bind=engine)
