"""
Basic script to show utility of custom project level logger.
"""

import os
import sys
sys.path.append('.')

# import custom logger class.
from utils.logging import ProjectLogger
# set required logging configurations, using set_logger function, this creates the required logger object.
ProjectLogger.set_logger(
    logger_name=os.path.basename(__file__).replace(".py", ""), # setting current script name as logger name.
    log_level="INFO",
    log_filepath="/Users/ankitsajwan/desktop/git/logger/demo_script.log"
)
# defined logger for current script.
logger = ProjectLogger.get_logger(__name__)

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