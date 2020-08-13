from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_NAME = "mydb"
DATABASE_USERNAME = "postgres"
DATABASE_USER_PASSWORD = "1"
DATABASE_ADDRESS = "localhost:5432"
SQLALCHEMY_DATABASE_URL = f"postgresql://{DATABASE_USERNAME}:{DATABASE_USER_PASSWORD}" \
                          f"@{DATABASE_ADDRESS}/{DATABASE_NAME}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
