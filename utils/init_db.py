import os
from sqlalchemy import text
from database.db import SessionLocal

def execute_create_scripts():
    base_path = "sql"
    db = SessionLocal()

    for root, dirs, files in os.walk(base_path):
        for file in files:
            if file == "create.sql":
                with open(os.path.join(root, file), "r", encoding="utf-8") as f:
                    sql_query = f.read()
                    try:
                        db.execute(text(sql_query))
                    except Exception as e:
                        print(f"Error executing {file}: {e}")
    db.commit()
    db.close()
