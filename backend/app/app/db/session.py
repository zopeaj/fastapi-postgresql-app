from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


POSTGRESQL_DATABASE_URL = "postgresql+psycopg2://postgres:admin1234@localhost:5432/postgres"
engine = create_engine(POSTGRESQL_DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


