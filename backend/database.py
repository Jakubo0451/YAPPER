from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# db url
DATABASE_URL = "postgresql://postgres:2345@localhost/Yapper"

# sqlalchemy enging
engine = create_engine(DATABASE_URL)

# session maker
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# create base class for our models
Base = declarative_base()

# get db session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()