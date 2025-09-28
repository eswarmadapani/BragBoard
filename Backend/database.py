from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import DATABASE_URL
import logging

# Set up logging for database connection
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

engine = create_engine(DATABASE_URL, echo=False)  # Set echo=True for SQL logging if needed
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Test connection on import
try:
    with engine.connect() as conn:
        logger.info("Database connection successful.")
except Exception as e:
    logger.error(f"Database connection failed: {e}")
    raise

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
