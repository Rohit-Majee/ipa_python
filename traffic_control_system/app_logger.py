import logging
import os
from config import LOG_DIR, LOG_FILE

os.makedirs(LOG_DIR, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    filename=os.path.join(LOG_DIR, LOG_FILE),
    format='%(asctime)s - %(levelname)s - Line:%(lineno)s - %(message)s',
)

logger = logging.getLogger(__name__)