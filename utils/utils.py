from logging import handlers

import logging


def init_logger(name: str = 'main') -> logging.Logger:
    logger = logging.getLogger(name)
    # logger = multiprocessing.get_logger()
    logger.setLevel(logging.INFO)
    FORMAT = '%(asctime)s - %(levelname)s - %(message)s'
    formatter = logging.Formatter(FORMAT, datefmt='%Y-%m-%d %H:%M:%S')
    sh = logging.StreamHandler()
    sh.setFormatter(formatter)
    sh.setLevel(logging.DEBUG)
    fh = logging.handlers.RotatingFileHandler(f'{name}.log', maxBytes=10485760, backupCount=5)
    fh.setFormatter(formatter)
    fh.setLevel(logging.DEBUG)
    logger.addHandler(sh)
    logger.addHandler(fh)
    logger.info('Logger initialized')
    logger.debug('Logger initialized')
    return logger