import os

def list_directory(path):
    try:
        items = os.listdir(path)
        return "\n".join(items)
    except Exception as e:
        return f"ERROR: {e}"

def read_file(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        return f"ERROR: {e}"