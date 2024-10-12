import os
import openai
from langchain.globals import set_verbose
from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    name: str = os.getenv("NAME", "channel-copilot")
    debug: bool = os.getenv("DEBUG", False)

    # OpenAI
    open_ai_key: str = os.getenv("OPENAI_API_KEY")
    open_ai_organization: str = os.getenv("OPENAI_ORGANIZATION", '')
    open_ai_proxy: str = os.getenv("OPENAI_PROXY", '')


settings = Settings()

openai.api_key = settings.open_ai_key
set_verbose(settings.debug)
