import os

# App settings
APP_NAME = "Business Budget Management API"
VERSION = "1.0.0"

# Database config (currently using SQLite)
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://madhav:M%4013dhav@34.131.223.245:3306/budgetdb"



# CORS settings (allow frontend React app to call API)
ALLOWED_ORIGINS = os.getenv("ALLOWED_ORIGINS", "*").split(",")

# Upload folder for PO & Invoice files
UPLOAD_DIR = os.getenv("UPLOAD_DIR", "static/uploads")
