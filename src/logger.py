import logging as logger
from datetime import datetime
import os

LOG_FILE = f"{datetime.now().strftime('%m_%d_%y_%H_%M_%S')}.log"

log_dir = os.path.join(os.getcwd(), "logs")
os.makedirs(log_dir, exist_ok=True)

LOG_FILE_PATH = os.path.join(log_dir, LOG_FILE)

logger.basicConfig(
    filename=LOG_FILE_PATH,
    level=logger.INFO,
    format="[ %(asctime)s ] %(lineno)d %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    force=True
)

if __name__ == "__main__":
    logger.info("Logging has started.")