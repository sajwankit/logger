import logging
import sys

class ProjectLogger:
    """ Creates a custom project level logger, 
    so that the same logger created can be used by different modules, scripts across the project as required.
    """

    LOGGER = None

    @staticmethod
    def set_logger(
        logger_name,
        log_level="INFO",
        log_formatter="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        log_filepath=None,
        log_to_console=True
    ):
        logger = logging.getLogger(logger_name)
        logger.setLevel(logging.getLevelName(log_level))
        formatter = logging.Formatter(
            fmt=log_formatter,
            datefmt=datefmt
        )

        # handler to write to log file.
        if log_filepath:
            file_handler = logging.FileHandler(log_filepath)
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)

        # handler to write to console.
        if log_to_console:
            consoleHandler = logging.StreamHandler(sys.stdout)
            consoleHandler.setFormatter(formatter)
            logger.addHandler(consoleHandler)

        ProjectLogger.LOGGER = logger

    @staticmethod
    def get_logger(module_name):
        if ProjectLogger.LOGGER is None:
            # return basic logger if custom logger is not set.
            return logging.getLogger(__name__)
        else:
            # return created logger or logger child per from where get_logger is called.
            return ProjectLogger.LOGGER if module_name=="__main__" else ProjectLogger.LOGGER.getChild(module_name)

