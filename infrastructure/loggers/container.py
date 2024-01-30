
import logging

from infrastructure.loggers.logger import Logger


class LoggerContainer:
    def __init__(self):

        self._info = Logger(name="INFO", level=logging.INFO)
        self._warning = Logger(name="WARNING", level=logging.WARNING)
        self._critical = Logger(name="CRITICAL", level=logging.CRITICAL)

    def get_logger(self, name: str) -> Logger:
        if name == "INFO":
            return self._info
        elif name == "WARNING":
            return self._warning
        elif name == "CRITICAL":
            return self._critical
        else:
            raise NameError(f"No such logger: {name}")
