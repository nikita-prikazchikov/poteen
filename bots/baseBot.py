import logging
import time

from selenium.common.exceptions import NoSuchElementException, \
    WebDriverException
from selenium.webdriver.remote.webelement import WebElement

from bots.generic import reset_implicitly_wait, set_implicitly_wait
from ContextHolder import ContextHolder
from log.Result import Result


__author__ = 'nprikazchikov'

logger = logging.getLogger("bots.baseBot")


class BaseBot:
    def find_element(self, by, value, parent=None):

        element = None

        if parent is None:
            parent = ContextHolder.get_driver()
        try:
            element = parent.find_element(by, value)
        except NoSuchElementException, e:
            logger.debug("Element not found")
        except WebDriverException, e:
            logger.error(str(e))
        finally:
            return element

    def find_elements(self, by, value, parent=None):
        element = None

        if parent is None:
            parent = ContextHolder.get_driver()
        try:
            element = parent.find_elements(by, value)
        except NoSuchElementException, e:
            logger.debug("Element not found")
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

        if isinstance(element, WebElement):
            return element.is_displayed()
        return False

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