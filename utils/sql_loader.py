def load_query(path: str) -> str:
    with open(path, "r", encoding="utf-8") as file:
        return file.read()
