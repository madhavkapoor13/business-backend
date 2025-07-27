import os

# App settings
APP_NAME = "Business Budget Management API"
VERSION = "1.0.0"

# Database config (currently using SQLite)
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./budget.db")

# CORS settings (allow frontend React app to call API)
ALLOWED_ORIGINS = os.getenv("ALLOWED_ORIGINS", "*").split(",")

# Upload folder for PO & Invoice files
UPLOAD_DIR = os.getenv("UPLOAD_DIR", "static/uploads")
