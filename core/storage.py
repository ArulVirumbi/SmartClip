import json
import os
# from dotenv import load_dotenv

# load_dotenv(dotenv_path=".env.local")
# store_path = os.getenv("STORE_PATH")

store_path = "" #Use this when running pyinstaller

def _load_store():
    if not os.path.exists(store_path):
        return {}
    try:
        with open(store_path, 'r', encoding='utf-8') as f:
            content = f.read().strip()
            if not content:
                return {}
            return json.loads(content)
    except (json.JSONDecodeError, ValueError):
        return {}


def _save_store(data):
    with open(store_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)

def save_entry(key, value):
    data = _load_store()
    data[key] = value
    _save_store(data)

def get_entry(key):
    data = _load_store()
    return data.get(key)

def get_all_keys():
    data = _load_store()
    return list(data.keys())
