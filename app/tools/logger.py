import logging
from app.tools.conf import config

logging.basicConfig(level=config['LOG_LEVEL'])
logger = logging.getLogger(__name__)
