from app.config.settings import settings
from app.utils.logger import setup_logger


logger = setup_logger()


def startup():

    print("=" * 50)
    print(f"🚀 {settings.APP_NAME} v{settings.APP_VERSION}")
    print("=" * 50)

    logger.info("Loading Configuration...")
    logger.info("Logger Initialized")
    logger.info("Starting Core Engine...")
    logger.info("Tool Registry Loaded")
    logger.info("JARVIS AI OS Ready.")

    print("=" * 50)