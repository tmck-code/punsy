'Define our logging format'

import logging
import os
import sys

LOG_BASE_NAME = 'punsy'

logger = logging.getLogger(LOG_BASE_NAME)
logger.setLevel(logging.INFO)

if os.getenv('ENV', 'dev') != 'test' and not logger.handlers:
    channel = logging.StreamHandler(sys.stdout)
    channel.setLevel(logging.INFO)
    channel.setFormatter(logging.Formatter('- %(message)s'))
    logger.addHandler(channel)

def get_logger(module_name):
    'Return a new logger object for this library'
    return logging.getLogger('{}.{}'.format(LOG_BASE_NAME, module_name))

