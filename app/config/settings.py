"""
Application configuration settings
"""
import os
from enum import Enum
from dotenv import load_dotenv

load_dotenv()

class Settings(Enum):
    # Application metadata
    APP_NAME = "Flet App Template"
    APP_VERSION = "0.1.0"

    # UI settings
    DEFAULT_WINDOW_WIDTH = 1024
    DEFAULT_WINDOW_HEIGHT = 768

    # Environment settings
    IS_DEV = os.getenv("APP_ENV", "development") == "development"

    # Logging settings
    LOG_LEVEL = "DEBUG"
    LOG_FILE_PATH = "logs/app.log"
    SENTRY_DSN = os.getenv("SENTRY_DSN")

    def __str__(self):
        return self.value
    
    def __get__(self, instance, owner):
        return self.value