# Week 1 Backend Setup TODO

- [x] Set up Python virtual environment in Backend directory
- [x] Install required dependencies: fastapi, uvicorn, sqlalchemy, psycopg2-binary, python-jose[cryptography], passlib[bcrypt], python-multipart
- [x] Create requirements.txt with dependencies
- [x] Create config.py for database URL and JWT settings
- [x] Create models.py with SQLAlchemy models for Users table
- [x] Create database.py for database connection and session management
- [x] Create auth.py for JWT token creation, verification, and password hashing
- [x] Create main.py with FastAPI app, including CORS middleware
- [x] Create routers/users.py for user-related endpoints (register, login)
- [x] Update main.py to include the users router
- [x] Run the FastAPI server to verify basic setup
- [x] Test user registration and login endpoints

# Database Connection Perfection TODO

- [x] Update Backend/database.py: Export engine and SessionLocal, add logging and connection test on import
- [x] Update Backend/main.py: Fix imports to reuse from database.py, remove duplication, ensure table creation, add /health endpoint for DB check
- [x] Test server startup: Run uvicorn and confirm no import errors, tables created in bragboard.db
- [x] Verify DB connection: Access /health endpoint, confirm "healthy" status with connected database
