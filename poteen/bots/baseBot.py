import time

from selenium.common.exceptions import NoSuchElementException, \
    WebDriverException
from selenium.webdriver.remote.webelement import WebElement

from .generic import reset_implicitly_wait, set_implicitly_wait
from ..contextHolder import ContextHolder
from ..log.result import Result


__author__ = 'nprikazchikov'

logger = ContextHolder.get_logger()


class BaseBot:
    def find_element(self, by, value, parent=None):

        element = None

        if parent is None:
            parent = ContextHolder.get_driver()
        try:
            logger.debug("Find element by: {by}; value: {value}".format(
                by=by,
                value=value
            ))
            element = parent.find_element(by, value)
        except NoSuchElementException, e:
            logger.debug("Element not found by: {by}; value: {value};"
                         " parent: {parent}".format(
                         by=by, value=value, parent=parent))
        except WebDriverException, e:
            logger.error(str(e))
        finally:
            return element

    def find_elements(self, by, value, parent=None):
        element = None

        if parent is None:
            parent = ContextHolder.get_driver()
        try:
            logger.debug("Find elements by: {by}; value: {value}".format(
                by=by,
                value=value
            ))
            element = parent.find_elements(by, value)
        except NoSuchElementException, e:
            logger.debug("Elements not found by: {by}; value: {value};"
                         " parent: {parent}".format(
                         by=by, value=value, parent=parent))
        except WebDriverException, e:
            logger.error(str(e))
        finally:

            return element

    def find_element_no_wait(self, by, value, parent=None):

        reset_implicitly_wait()
        element = self.find_element(by, value, parent)
        set_implicitly_wait()

        return element

    def find_elements_no_wait(self, by, value, parent=None):

        reset_implicitly_wait()
        elements = self.find_elements(by, value, parent)
        set_implicitly_wait()

        return elements

    def is_element_displayed(self, element=None):
        res = False
        if isinstance(element, WebElement):
            res = element.is_displayed()
        logger.debug("Element " + "visible" if res else "not visible")
        return res

    def is_displayed(self, by, value, parent=None):

        return self.is_element_displayed(
            self.find_element_no_wait(by, value, parent))

    def is_element_exists(self, by, value, parent=None):

        return not self.find_element_no_wait(by, value, parent) is None

    def wait_for_time(self, timeout):
        time.sleep(timeout)
        return Result(
            "Wait for [{timeout}] milliseconds".format(timeout=timeout))

    def wait_loading(self):
        return self.wait_for_time(0.3)
