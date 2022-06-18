import os
import sys
sys.path.append('.')

from utils.logging import ProjectLogger
ProjectLogger.set_logger(
    logger_name=os.path.basename(__file__).replace(".py", ""),
    log_level="INFO",
    log_filepath="/Users/ankitsajwan/desktop/git/logger/p1_log.log"
)
logger = ProjectLogger.LOGGER

from helpers import divide

if __name__=="__main__":
    logger.info('Logger is working from the parent script.')
    logger.info('Performing division..')
    divide.divide(10,1)
    divide.divide(10,0)