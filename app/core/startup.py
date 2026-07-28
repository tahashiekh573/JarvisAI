from app.config.settings import settings
from app.utils.logger import setup_logger
from app.services.desktop_service import register_desktop_tools

logger = setup_logger()


def startup():

    print("=" * 60)
    print(f"🚀 {settings.APP_NAME} v{settings.APP_VERSION}")
    print("=" * 60)

    logger.info("Loading Configuration...")
    logger.info("Initializing Logger...")

    logger.info("Loading Desktop Tools...")

    register_desktop_tools()

    logger.info("Desktop Tools Loaded.")
    logger.info("System Ready.")

    print("=" * 60)