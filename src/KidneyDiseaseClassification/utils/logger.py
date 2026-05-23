import os
import sys
import logging
from datetime import datetime
from colorlog import ColoredFormatter

LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
LOG_FILE_PATH = os.path.join(LOG_DIR, LOG_FILE)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# ================= FILE HANDLER =================
file_handler = logging.FileHandler(LOG_FILE_PATH)

file_formatter = logging.Formatter(
    "[%(asctime)s] %(levelname)s %(module)s: %(message)s"
)

file_handler.setFormatter(file_formatter)

# ================= CONSOLE HANDLER =================
console_handler = logging.StreamHandler(sys.stdout)

color_formatter = ColoredFormatter(
    "%(log_color)s[%(asctime)s] %(levelname)s %(module)s: %(message)s",
    log_colors={
        "DEBUG": "cyan",
        "INFO": "green",
        "WARNING": "yellow",
        "ERROR": "red",
        "CRITICAL": "bold_red",
    }
)

console_handler.setFormatter(color_formatter)

# ================= ADD HANDLERS =================
logger.addHandler(file_handler)
logger.addHandler(console_handler)