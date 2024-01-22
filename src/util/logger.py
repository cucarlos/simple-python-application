import logging
import sys

logging.basicConfig(stream=sys.stdout, level=logging.NOTSET, format="%(levelname)s - %(message)s")

class Logger():
    def info(self, message):
        logging.info(message)
    
    def warn(self, message):
        logging.warning(message)
