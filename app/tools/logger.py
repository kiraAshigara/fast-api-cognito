import logging
from app.tools.conf import config

logging.basicConfig(level=int(config['LOG_LEVEL']))
logger = logging.getLogger(__name__)
