import logging
import logging.config
  
logging.config.fileConfig('shared/logger.conf')

def getLogger(name="app"):
    logger = logging.getLogger(name)
    logger.setLevel(0)
    return logger