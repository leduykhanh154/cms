import os
import logging
import datetime

class LoggerConfig:
    log_dir = "logs"
    log_filename = None
    logger = None
    @staticmethod
    def get_logger():
        if LoggerConfig.logger:
            return LoggerConfig.logger
         
        if not os.path.exists(LoggerConfig.log_dir):
            os.makedirs(LoggerConfig.log_dir)

        LoggerConfig.log_filename = os.path.join(LoggerConfig.log_dir, f"test_results_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.log")

        logger = logging.getLogger("test_logger")

        logger.setLevel(logging.INFO)

        if logger.hasHandlers():
            logger.handlers.clear()

        file_handler = logging.FileHandler(LoggerConfig.log_filename, mode="w", encoding="utf-8")

        file_formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

        file_handler.setFormatter(file_formatter)

        console_handler = logging.StreamHandler()

        console_formatter = logging.Formatter("[%(levelname)s] %(message)s")

        console_handler.setFormatter(console_formatter)

        logger.addHandler(file_handler)

        logger.addHandler(console_handler)

        LoggerConfig.logger = logger
        
        return logger
