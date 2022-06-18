from utils.logging import ProjectLogger
logger = ProjectLogger.get_logger(__name__)

def divide(a, b):
    try:
        return a/b
    except Exception as e:
        logger.error("Exception Occurred", exc_info=True)