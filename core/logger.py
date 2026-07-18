import logging
import sys


class CustomFormatter(logging.Formatter):
    FORMATS = {
        logging.DEBUG: "[DEBUG] %(message)s",
        logging.INFO: "[INFO] %(message)s",
        logging.WARNING: "[WARNING] %(message)s",
        logging.ERROR: "[ERROR] %(message)s",
        logging.CRITICAL: "[CRITICAL] %(message)s",
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)


logger = logging.getLogger("Kayumi")
logger.setLevel(logging.INFO)

handler = logging.StreamHandler(sys.stdout)
handler.setFormatter(CustomFormatter())

logger.addHandler(handler)
