import os
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
from error import IllegalAssignmentError

__author__ = 'nprikazchikov'


class ContextHolder:
    DEFAULT_WEBDRIVER_IMPLICITLY_WAIT_TIME = 5
    DEFAULT_WEBDRIVER_WAIT_LOAD_TIMEOUT = 30

    # Global flag to make or not to make screenshots
    _doScreenshot = bool
    # Single presentation of driver for tests
    _driver = WebDriver
    # Single presentation of driver for tests
    _actions = ActionChains
    # Name of current Test Suite
    _testSuite = str
    # Name of current Test Case
    _testCase = str
    # Name of Browser to run the tests on
    _browser = str
    #Path to current working folder
    _workspacePath = None

    @classmethod
    def get_workspace_path(cls):
        if not cls._workspacePath:
            cls._workspacePath = os.path.dirname(__file__)
        return cls._workspacePath

    @classmethod
    def set_workspace_path(cls, value):
        if isinstance(value, str):
            cls._workspacePath = value
        else:
            raise IllegalAssignmentError(value, str)

    @classmethod
    def get_do_screenshot(cls):
        return cls._doScreenshot

    @classmethod
    def set_do_screenshot(cls, value):
        if isinstance(value, bool):
            cls._doScreenshot = value
        else:
            raise IllegalAssignmentError(value, bool)

    @classmethod
    def get_driver(cls):
        return cls._driver

    @classmethod
    def set_driver(cls, value):
        if isinstance(value, WebDriver):
            cls._driver = value
            cls._actions = ActionChains(value)
        else:
            raise IllegalAssignmentError(value, WebDriver)

    @classmethod
    def get_test_suite(cls):
        return cls._testSuite

    @classmethod
    def set_test_suite(cls, value):
        if isinstance(value, str):
            cls._testSuite = value
        else:
            raise IllegalAssignmentError(value, str)

    @classmethod
    def get_test_case(cls):
        return cls._testCase

    @classmethod
    def set_test_case(cls, value):
        if isinstance(value, str):
            cls._testCase = value
        else:
            raise IllegalAssignmentError(value, str)

    @classmethod
    def get_action_chain(cls):
        return cls._actions

    @classmethod
    def get_browser(cls):
        return cls._browser

    @classmethod
    def set_browser(cls, value):
        if isinstance(value, str):
            cls._browser = value
        else:
            raise IllegalAssignmentError(value, str)
