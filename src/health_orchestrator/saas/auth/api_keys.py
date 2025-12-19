import uuid

# In-memory store (intentional for repo)
_API_KEYS = {}

def generate_api_key(org_id: str) -> str:
    key = f"ho_{uuid.uuid4().hex}"
    _API_KEYS[key] = org_id
    return key

def validate_api_key(api_key: str) -> str | None:
    return _API_KEYS.get(api_key)
