from functools import lru_cache
from pydantic import SecretStr, Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env',
        extra='ignore'
    )
    
    cohere_api_key: SecretStr
    chat_model: str = "command-a-03-2025"
    temperature: float = Field(ge=0, le=1, default=0.0)
    max_retries: int = Field(ge=0, default=3)
    timeout: float = Field(gt=0, default=30.0)
    
    
@lru_cache
def get_settings() -> Settings:
    return Settings()
