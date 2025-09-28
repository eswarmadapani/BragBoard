import os
from datetime import timedelta

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./bragboard.db")
SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key-here")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
REFRESH_TOKEN_EXPIRE_DAYS = 7
