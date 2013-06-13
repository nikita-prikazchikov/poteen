import logging
import time

from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver.support.wait import WebDriverWait

from ..contextHolder import ContextHolder
from .baseBot import BaseBot


__author__ = 'nprikazchikov'

logger = logging.getLogger("bots.WaitBot")


class WaitBot(BaseBot):
    _timeout = 5
    _actionName = ""
    _parameters = ""

    def __init__(self, timeout):
        self._timeout = timeout

    def _get_driver_wait(self, timeout=None):
        timeout = self._get_timeout(timeout)
        return WebDriverWait(ContextHolder.get_driver(), timeout)

    def _get_timeout(self, timeout=None):
        if timeout is None:
            timeout = self._timeout
        return timeout

    def _wait_for(self, condition, timeout=None):
        timeout = self._get_timeout(timeout)
        try:
            result = self._get_driver_wait(timeout).until(condition)
        except TimeoutException:
            result = None
            logger.debug(
                "Waiting for {action} failed. Timeout exception. "
                "Parameters: {parameters}".format(
                    action=self._actionName,
                    parameters=self._parameters
                )
            )
        except WebDriverException, e:
            logger.error(repr(e))
            result = None
        return result

    def _prepare_parameters(self, by, value, parent=None, timeout=None):
        self._parameters = \
            "By: {by}; Value: {value}; " \
            "Parent: {parent}; Timeout: {timeout}".format(
            by=by,
            value=value,
            parent=parent,
            timeout=self._get_timeout(timeout)
            )

    def _prepare_element_parameters(self, web_element, parent=None,
                                    timeout=None):
        self._parameters = \
            "Element: {element};Parent: {parent}; Timeout: {timeout}".format(
            element=web_element,
            parent=parent,
            timeout=self._get_timeout(timeout)
            )

    def wait_for_stop_moving(self, by, value, parent=None, timeout=None):
        self._actionName = "stop moving"
        self._prepare_parameters(by, value, parent, timeout)
        return self._wait_for(
            stop_moving(self.find_element(by, value, parent)), timeout
        )

    def wait_for_web_element_stop_moving(self, web_element, parent=None,
                                         timeout=None):
        self._actionName = "stop moving"
        self._prepare_element_parameters(web_element, parent, timeout)
        return self._wait_for(
            stop_moving(web_element), timeout
        )

    def wait_for_stop_resizing(self, by, value, parent=None, timeout=None):
        self._actionName = "stop resizing"
        self._prepare_parameters(by, value, parent, timeout)
        return self._wait_for(
            stop_resizing(self.find_element(by, value, parent)), timeout
        )

    def wait_for_web_element_stop_resizing(self, web_element, parent=None,
                                           timeout=None):
        self._actionName = "stop resizing"
        self._prepare_element_parameters(web_element, parent, timeout)
        return self._wait_for(
            stop_resizing(web_element), timeout
        )

    def wait_for_web_element(self, by, value, parent=None, timeout=None):
        self._actionName = "WebElement"
        self._prepare_parameters(by, value, parent, timeout)
        return self._wait_for(
            wait_for(
                condition=lambda by, value, parent:
                self.find_element(by, value, parent),
                by=by,
                value=value,
                parent=parent
            ),
            timeout
        )

    def wait_for_disappears(self, by, value, parent=None, timeout=None):
        self._actionName = "WebElement disappears"
        self._prepare_parameters(by, value, parent, timeout)
        return self._wait_for(
            wait_for(
                condition=lambda by, value, parent:
                not self.is_displayed(by, value, parent),
                by=by,
                value=value,
                parent=parent
            ),
            timeout
        )

    def wait_for_web_element_disappears(self, web_element, timeout=None):
        self._actionName = "WebElement disappears"
        self._prepare_element_parameters(web_element, None, timeout)
        return self._wait_for(
            wait_for(
                condition=lambda element:
                not self.is_element_displayed(element),
                element=web_element
            ),
            timeout
        )

    def wait_for_collapse(self, by, value, parent=None, timeout=None):
        self._actionName = "WebElement collapse"
        self._prepare_parameters(by, value, parent, timeout)
        return self._wait_for(
            wait_for(
                condition=lambda by, value, parent:
                not self.is_element_exists(by, value, parent),
                by=by,
                value=value,
                parent=parent
            ),
            timeout
        )

    def wait_for_displays(self, by, value, parent=None, timeout=None):
        self._actionName = "WebElement displays"
        self._prepare_parameters(by, value, parent, timeout)
        return self._wait_for(
            wait_for(
                condition=lambda by, value, parent:
                self.is_displayed(by, value, parent),
                by=by,
                value=value,
                parent=parent
            ),
            timeout
        )

    def wait_for_web_element_displays(self, web_element, timeout=None):
        self._actionName = "WebElement displays"
        self._prepare_element_parameters(web_element, None, timeout)
        return self._wait_for(
            wait_for(
                condition=lambda element:
                self.is_element_displayed(element),
                element=web_element
            ),
            timeout
        )


class wait_for(object):
    def __init__(self, condition, *args, **kwargs):
        self.condition = condition
        self.args = kwargs

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


class stop_resizing(object):
    def __init__(self, web_element):
        self.web_element = web_element

    def __call__(self, driver):
        size1 = self.web_element.size
        time.sleep(0.1)
        size2 = self.web_element.size
        return size1["width"] == size2["width"] \
            and size1["height"] == size2["height"]
