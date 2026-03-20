import logging
import os
from datetime import datetime

LOG_FILE = "project.log"
logs_path = os.path.join(os.path.dirname(__file__), "logs")
os.makedirs(logs_path, exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE_PATH),
        logging.StreamHandler(),
    ],
)

if __name__ == "__main__":
    logger = logging.getLogger(__name__)
    try:
        a = 5 / 0
    except Exception as e:
        logger.error(f"An error occurred: {e}")

    logger.info("Logger has started")
