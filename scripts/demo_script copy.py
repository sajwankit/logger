"""
Basic script to show utility of custom project level logger.
"""

import os
import sys
sys.path.append('.')

# import custom logger class.
import logging
import logging.config
from utils.logging import LOGGING_CONFIG
# set required logging configurations, using set_logger function, this creates the required logger object.
logging.config.dictConfig(LOGGING_CONFIG)
# defined logger for current script.
logger = logging.getLogger(__name__)

# NOTE: Make sure to set your logger before importing other modules,
# so that logger object is created and will be used by other imported modules.
# importing divide module from helper (defined under the demo project).
from helpers import divide

if __name__=="__main__":
    logger.info("Task Started.")
    logger.info("Performing division, 10 divided by 3.")
    d1 = divide.divide(10,3)
    logger.info("Performing division, 10 divided by 0.")
    d2 = divide.divide(10,0)
    logger.info("Task Completed.")