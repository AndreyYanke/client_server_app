import logging
from logging.handlers import TimedRotatingFileHandler


formatter = logging.Formatter(
    '%(asctime)-5s %(levelname)-5s %(module)s %(message)s')

log_handler = TimedRotatingFileHandler('server.log', when='midnight',
                                       backupCount=7)
log_handler.setFormatter(formatter)

logger = logging.getLogger('messenger.server')
logger.setLevel(logging.INFO)
logger.addHandler(log_handler)

