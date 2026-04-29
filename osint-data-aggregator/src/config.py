import os

class Settings:
    DATALAKE_BUCKET = os.getenv("DATALAKE_BUCKET", "osint-datalake-bucket")

settings = Settings()
