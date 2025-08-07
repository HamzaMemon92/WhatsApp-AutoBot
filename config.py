from pydantic_settings import BaseSettings

# ✅ TEMPORARY hardcoded fallback
import os
os.environ["GEMINI_API_KEY"] = "YOUR_API_KEY"  

class Settings(BaseSettings):
    GEMINI_API_KEY: str

    class Config:
        env_file = ".env"

settings = Settings()

# ✅ Debug print

print("DEBUG: Loaded GEMINI_API_KEY:", settings.GEMINI_API_KEY)
