from selenium.common.exceptions import StaleElementReferenceException
from .contextHolder import ContextHolder

logger = ContextHolder.get_logger()


def catch_stale_error(func):
    def wrapped(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
        except StaleElementReferenceException:
            logger.debug(
                "StaleElementReferenceException "
                "catched during call {} function. Recall".format(
                    func.__name__
                ))
            result = func(*args, **kwargs)
        return result

    return wrapped
