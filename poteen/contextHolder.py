import os
import logging
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
from .error import IllegalAssignmentError

__author__ = 'nprikazchikov'


class ContextHolder:
    DEFAULT_WEBDRIVER_IMPLICITLY_WAIT_TIME = 5
    DEFAULT_WEBDRIVER_WAIT_LOAD_TIMEOUT = 30

    LOG_LEVEL = logging.INFO

    # Base site URL for testing
    __base_url = None
    # Global flag to make or not to make screenshots
    __doScreenshot = bool
    # Global flag to make or not to make screenshots
    __do_html_report = False
    # Single presentation of driver for tests
    __driver = None
    # Single presentation of ActionChains for current driver
    __actions = None
    # Name of current Test Suite
    __testSuite = None
    # Name of current Test Case
    __testCase = None
    # Name of Browser to run the tests on
    __browser = None
    #Path to current working folder
    __workspacePath = None
    # URL for connecting to remote WebDriver
    __remote_executor = 'http://127.0.0.1:4444/wd/hub'

    implicitly_wait = 5

    logger = None

    @classmethod
    def get_workspace_path(cls):
        if not cls.__workspacePath:
            cls.__workspacePath = os.path.dirname(__file__)
        return cls.__workspacePath

    @classmethod
    def set_workspace_path(cls, value):
        if isinstance(value, str):
            cls.__workspacePath = value
        else:
            raise IllegalAssignmentError(value, str)

    @classmethod
    def get_do_screenshot(cls):
        return cls.__doScreenshot

    @classmethod
    def set_do_screenshot(cls, value):
        if isinstance(value, bool):
            cls.__doScreenshot = value
        else:
            raise IllegalAssignmentError(value, bool)

    @classmethod
    def get_do_report(cls):
        return cls.__do_html_report

    @classmethod
    def set_do_report(cls, value):
        if isinstance(value, bool):
            cls.__do_html_report = value
        else:
            raise IllegalAssignmentError(value, bool)

    @classmethod
    def get_driver(cls):
        return cls.__driver

    @classmethod
    def set_driver(cls, value):
        if isinstance(value, WebDriver):
            cls.__driver = value
            cls.__actions = ActionChains(value)
        elif value is None:
            cls.__driver = None
            cls.__actions = None
        else:
            raise IllegalAssignmentError(value, WebDriver)

    @classmethod
    def get_test_suite(cls):
        return cls.__testSuite

    @classmethod
    def set_test_suite(cls, value):
        if isinstance(value, str):
            cls.__testSuite = value
        else:
            raise IllegalAssignmentError(value, str)

    @classmethod
    def get_test_case(cls):
        return cls.__testCase

    @classmethod
    def set_test_case(cls, value):
        if isinstance(value, str):
            cls.__testCase = value
        else:
            raise IllegalAssignmentError(value, str)

    @classmethod
    def get_action_chain(cls):
        return cls.__actions

    @classmethod
    def get_browser(cls):
        return cls.__browser

    @classmethod
    def set_browser(cls, value):
        if isinstance(value, str):
            cls.__browser = value
        else:
            raise IllegalAssignmentError(value, str)

    @classmethod
    def get_url(cls):
        return cls.__base_url

    @classmethod
    def set_url(cls, value):
        if isinstance(value, str):
            cls.__base_url = value
        else:
            raise IllegalAssignmentError(value, str)

    @classmethod
    def load_defaults(cls):
        cls.__browser = "firefox"
        cls.__doScreenshot = True

    @classmethod
    def get_logger(cls):

        if cls.logger is None:
            formatter = logging.Formatter(
                fmt='%(asctime)s - %(levelname)s %(filename)s:'
                    '%(lineno)d -- %(message)s')

            handler = logging.StreamHandler()
            handler.setFormatter(formatter)

            logger = logging.getLogger("poteen")
            logger.setLevel(cls.LOG_LEVEL)
            logger.addHandler(handler)
            cls.logger = logger
        return cls.logger

    @classmethod
    def get_remote_executor(cls):
        return cls.__remote_executor

    @classmethod
    def set_remote_executor(cls, value):
        if isinstance(value, str):
            cls.__remote_executor = value
        else:
            raise IllegalAssignmentError(value, str)
