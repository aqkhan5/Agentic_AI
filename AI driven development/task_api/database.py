import os
from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env file
from sqlalchemy import  create_engine
from sqlalchemy.orm import sessionmaker

# Load the database URL from the environment variable
engine_neon = create_engine(os.getenv("neon_db"))
session_neon = sessionmaker(autocommit=False, autoflush=False, bind=engine_neon)