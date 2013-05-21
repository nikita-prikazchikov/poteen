import logging
from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver.support.wait import WebDriverWait
import time
from ContextHolder import ContextHolder
from bots.baseBot import BaseBot

__author__ = 'nprikazchikov'

logger = logging.getLogger("bots.WaitBot")


class WaitBot(BaseBot):
    _timeout = 5

    def __init__(self, timeout):
        self._timeout = timeout

    def _get_driver_wait(self, timeout=None):
        if timeout is None:
            timeout = self._timeout
        return WebDriverWait(ContextHolder.get_driver(), timeout)

    def _wait_for1(self, condition, timeout=5):
        try:
            result = self._get_driver_wait(timeout).until(condition)
        except TimeoutException:
            result = None
            logger.debug("Waiting for event failed. Timeout exception")
        except WebDriverException, e:
            logger.error(repr(e))
            result = None
        return result

    def _wait_for(self, condition, by=None, value=None, parent=None,
                  timeout=5):
        result = None

        arguments = {}

        if not by is None:
            arguments["by"] = by
        if not value is None:
            arguments["value"] = value

        arguments["parent"] = parent

        try:
            result = self._get_driver_wait(timeout).until(
                wait_for(condition, arguments)
            )
        except TimeoutException:
            result = None
            logger.debug("Waiting for event failed. Timeout exception")
        except WebDriverException, e:
            logger.error(repr(e))
            result = None
        return result

    def _wait_for_element(self, condition, element=None, timeout=5):
        result = None

        arguments = {"element": element}

        try:
            result = self._get_driver_wait(timeout).until(
                wait_for(condition, arguments)
            )
        except TimeoutException:
            result = None
            logger.debug("Waiting for event failed. Timeout exception")
        except WebDriverException, e:
            logger.error(repr(e))
            result = None
        return result

    def wait_for_stop_moving(self, by, value, parent=None):
        return self._wait_for1(
            stop_moving(self.find_element(by, value, parent))
        )

    def wait_for_web_element(self, by, value, parent=None):
        return self._wait_for(
            condition=lambda by, value, parent:
            self.find_element(by, value, parent),
            by=by,
            value=value,
            parent=parent
        )

    def wait_for_disappears(self, by, value, parent=None):
        return self._wait_for(
            condition=lambda by, value, parent:
            not self.is_displayed(by, value, parent),
            by=by,
            value=value,
            parent=parent
        )

    def wait_for_web_element_disappears(self, web_element):
        return self._wait_for_element(
            condition=lambda element:
            not self.is_element_displayed(element),
            element=web_element
        )

    def wait_for_collapse(self, by, value, parent=None):
        return self._wait_for(
            condition=lambda by, value, parent:
            not self.is_element_exists(by, value, parent),
            by=by,
            value=value,
            parent=parent
        )

    def wait_for_displays(self, by, value, parent=None):
        return self._wait_for(
            condition=lambda by, value, parent:
            self.is_displayed(by, value, parent),
            by=by,
            value=value,
            parent=parent
        )

    def wait_for_web_element_displays(self, web_element):
        return self._wait_for_element(
            condition=lambda element:
            self.is_element_displayed(element),
            element=web_element
        )


class wait_for(object):
    def __init__(self, condition, arguments):
        self.condition = condition
        self.args = arguments

    def __call__(self, driver):
        return self.condition(**self.args)


class stop_moving(object):
    def __init__(self, web_element):
        self.web_element = web_element

    def __call__(self, driver):
        point1 = self.web_element.location
        time.sleep(0.1)
        point2 = self.web_element.location
        return point1["x"] == point2["x"] and point1["y"] == point2["y"]