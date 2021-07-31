from pydantic import BaseSettings


class Settings(BaseSettings):
    DB_USER: str
    DB_NAME: str
    DB_HOST: str
    DB_PASS: str
    PSQL_DATABASE_URL: str
    ORIGINAL_IMAGE_URL: str
    NEGATIVE_IMAGE_URL: str

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


settings = Settings()
