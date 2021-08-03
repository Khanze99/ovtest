from typing import Optional

from pydantic import BaseSettings


class Settings(BaseSettings):
    DB_USER: Optional[str]
    DB_NAME: Optional[str]
    DB_HOST: Optional[str]
    DB_PASS: Optional[str]
    PSQL_DATABASE_URL: Optional[str]
    ORIGINAL_IMAGE_URL: Optional[str]
    NEGATIVE_IMAGE_URL: Optional[str]

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


settings = Settings()

