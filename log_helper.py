from functools import wraps
import logging


_log = logging.getLogger(__name__)


def log(logger=_log):
    """a decorator add function with log context.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            logger.debug('%s(args=%s, kwargs=%s) start', func.__name__, args, kwargs)
            try:
                resp = func(*args, **kwargs)
            except Exception as e:
                logger.debug('function %s raise exception: %r', func.__name__, e)
                raise
            logger.debug('function %s return: %s', func.__name__, resp)
            return resp
        return wrapper
    return decorator
