from contextlib import contextmanager

from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from core.main import app
from core.database import Base
from ov.config import test_settings

SQLALCHEMY_DATABASE_URL = test_settings.PSQL_DATABASE_URL

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base.metadata.create_all(bind=engine)


@contextmanager
def override_get_db():
    db = TestingSessionLocal()
    yield db
    db.close()


# app.dependency_overrides[get_db] = override_get_db()  TODO ?
client = TestClient(app)
