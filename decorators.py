from functools import wraps
import logging.config
from inspect import currentframe, getouterframes



logger = logging.getLogger('messenger.call')


def log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        caller = getouterframes(currentframe())[1][3]
        logger.info(
            f'Функция с именем {func.__name__} вызвана, аргумент {args},'
            f'{kwargs}. Вызов из {caller}.')
        return func(*args, **kwargs)
    return wrapper