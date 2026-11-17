from langchain_core.language_models import BaseChatModel
from langchain_cohere import ChatCohere

from app.config import get_settings


def get_chat_model(chat_model: str | None = None, 
                   temperature: float | None = None,
                   ) -> BaseChatModel:
    
    """Build the app's chat model. Arguments left as None fall back to the settings."""
    
    app_settings = get_settings()
    
    chat_model = chat_model if chat_model is not None else app_settings.chat_model
    temperature = temperature if temperature is not None else app_settings.temperature
    
    return ChatCohere(
        model=chat_model,
        cohere_api_key=app_settings.cohere_api_key,
        temperature=temperature,
        timeout_seconds= app_settings.timeout
    )
