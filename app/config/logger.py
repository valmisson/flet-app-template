import logging
import sentry_sdk
from loguru import logger
from sentry_sdk.integrations.logging import LoggingIntegration

from .settings import Settings

# configure loguru
logger.add(
    Settings.LOG_FILE_PATH,
    rotation="5 MB",
    level="INFO",
    backtrace=True,
    diagnose=True,
)

# configure standard logging to use loguru
class InterceptHandler(logging.Handler):
    def emit(self, record):
        try:
            level = logger.level(record.levelname).name
        except Exception:
            level = record.levelno
        logger.opt(depth=6, exception=record.exc_info).log(level, record.getMessage())

logging.basicConfig(handlers=[InterceptHandler()], level=0)

# integrate sentry
sentry_logging = LoggingIntegration(
    level=logging.INFO,
    event_level=logging.ERROR
)

if not Settings.IS_DEV and Settings.SENTRY_DSN:
    sentry_sdk.init(
        dsn=Settings.SENTRY_DSN,
        integrations=[sentry_logging],
        traces_sample_rate=1.0
    )