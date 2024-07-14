import os

from fastapi import HTTPException, Security
from fastapi.security.api_key import APIKeyHeader

# Define the static token
API_KEY_NAME = "Authorization"
API_KEY = os.getenv("API_SECRET_KEY", "engipper13")  # This is the static token we'll use

# Created an APIKeyHeader security scheme
api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)


# verify the token
def get_api_key(api_key_header: str = Security(api_key_header)):
    if api_key_header == API_KEY:
        return api_key_header
    else:
        raise HTTPException(status_code=401, detail="Invalid API Key")
