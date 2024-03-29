import logging


# Custom Formatter to add colors to log levels
class CustomFormatter(logging.Formatter):
    """Logging Formatter to add colors and count warning / errors"""

    pink = "\033[95m"
    green = "\x1b[32;21m"
    yellow = "\x1b[33;21m"
    red = "\x1b[31;21m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"
    # Include file name and line number in the format
    format = "%(asctime)s - %(name)s - %(levelname)s - [%(filename)s:%(lineno)d] - %(message)s"

    FORMATS = {
        logging.DEBUG: pink + format + reset,
        logging.INFO: green + format + reset,
        logging.WARNING: yellow + format + reset,
        logging.ERROR: red + format + reset,
        logging.CRITICAL: bold_red + format + reset,
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt, "%Y-%m-%d %H:%M:%S")
        return formatter.format(record)


# Configure Logger
logger = logging.getLogger("logger")
logger.setLevel(logging.DEBUG)

# Terminal Handler with Color
terminal_handler = logging.StreamHandler()
terminal_handler.setFormatter(CustomFormatter())
logger.addHandler(terminal_handler)
