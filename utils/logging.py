import logging
import sys

class ProjectLogger:

    LOGGER = None

    def set_logger(
        logger_name,
        log_level="INFO",
        log_formatter="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        log_filepath=None
    ):
        logger = logging.getLogger(logger_name)
        logger.setLevel(logging.getLevelName(log_level))
        formatter = logging.Formatter(
            fmt=log_formatter,
            datefmt=datefmt
        )

        # handler to write to log file
        if log_filepath:
            file_handler = logging.FileHandler(log_filepath)
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)

        # handler to write to console
        consoleHandler = logging.StreamHandler(sys.stdout)
        consoleHandler.setFormatter(formatter)
        logger.addHandler(consoleHandler)

        ProjectLogger.LOGGER = logger

    @staticmethod
    def get_logger(module_name):
        if ProjectLogger.LOGGER is None:
            return logging.getLogger(__name__)
        else:
            return ProjectLogger.LOGGER.getChild(module_name)

