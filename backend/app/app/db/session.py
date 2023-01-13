from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

POSTGRESQL_DATABASE_URL = "psycopg+postgresql://"
engine = create_engine(POSTGRESQL_DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoFlush=False)


