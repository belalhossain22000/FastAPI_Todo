try:
    # pydantic v2 provides a separate pydantic_settings package for Settings
    from pydantic_settings import BaseSettings
    class Settings(BaseSettings):
        DATABASE_URL: str
        JWT_SECRET: str
        jwt_algorithm: str = "HS256"
        jwt_expiration: int = 3600

        class Config:
            env_file = ".env"

    settings = Settings()
except Exception:
    # If pydantic-settings (or BaseSettings) isn't available in the environment,
    # provide a lightweight fallback that reads from environment variables.
    import os

    class Settings:
        DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite+aiosqlite:///./test.db")
        JWT_SECRET: str = os.getenv("JWT_SECRET", "change-me")
        jwt_algorithm: str = os.getenv("JWT_ALGORITHM", "HS256")
        jwt_expiration: int = int(os.getenv("JWT_EXPIRATION", "3600"))

    settings = Settings()
