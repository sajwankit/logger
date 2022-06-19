# from utils.logging import ProjectLogger
# logger = ProjectLogger.get_logger(__name__)
import logging
logger = logging.getLogger(__name__)

def divide(a, b):
    try:
        c = a/b
        logger.info(f'{a} divided by {b} is {c}')
        return c
    except Exception as e:
        logger.error(f"Exception Occurred in divide function for ({a}, {b}) inputs.", exc_info=True)
        return None