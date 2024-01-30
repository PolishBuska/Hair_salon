import logging
import os


class Logger:
    def __init__(self, name, level):
        self.level = level
        self.logger = logging.getLogger(name=name)
        self.logger.propagate = False
        self.logger.setLevel(level=level)
        log_file = os.path.join('logs', f'{name}_{name.lower()}.txt')
        handler = logging.FileHandler(log_file)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)

        if self.logger.hasHandlers():
            self.logger.handlers.clear()

        self.logger.addHandler(handler)

    def msg(self, message: str):
        self.logger.log(msg=message, level=self.level)

