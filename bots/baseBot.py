from datetime import datetime
import logging
import time

from selenium.common.exceptions import NoSuchElementException, \
    WebDriverException
from selenium.webdriver.remote.webelement import WebElement

from bots.generic import reset_implicitly_wait, set_implicitly_wait
from ContextHolder import ContextHolder
from elements.BaseElement import BaseElement
from log.Result import Result
from log.Screenshot import Screenshot


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
        elif isinstance(element, BaseElement):
            try:
                return element.get_element().is_displayed()
            except NoSuchElementException:
                pass

        return False

    def is_displayed(self, by, value, parent=None):

        return self.is_element_displayed(
            self.find_element_no_wait(by, value, parent))

    def is_element_exists(self, by, value, parent=None):

        return not self.find_element_no_wait(by, value, parent) is None

    def take_screenshot(self, message=""):
        """
        :param message: comment for screenshot to display. DO screenshot
        flag has to be set to True in ContextHolder
        :return: Screenshot|None
        """
        if ( ContextHolder.get_do_screenshot() ):
            working_dir = ContextHolder.get_workspace_path()
            path = "{path}{name}.png".format(
                path="/result/images/",
                name=datetime.now().strftime("%Y_%m_%d__%H_%M_%S"))
            if ContextHolder.get_driver().save_screenshot(working_dir + path):
                return Screenshot(
                    "Test suite {}; Test case {}; {}".format(
                        ContextHolder.get_test_suite(),
                        ContextHolder.get_test_case(),
                        message
                    ),
                    path)
            else:
                return None
        else:
            return None

    def wait_for_time(self, timeout):
        time.sleep(timeout)
        return Result(
            "Wait for [{timeout}] milliseconds".format(timeout=timeout))

    def wait_loading(self):
        return self.wait_for_time(0.3)