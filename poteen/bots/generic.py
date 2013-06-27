import logging
import platform
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from ..contextHolder import ContextHolder
from ..error import PoteenError

__author__ = 'nprikazchikov'

logger = ContextHolder.get_logger()


def switch_to_default_content():
    ContextHolder.get_driver().switch_to_default_content()


def maximize_window():
    logger.info("maximize driver window")
    ContextHolder.get_driver().maximize_window()
    os = platform.uname()[0].lower()
    if os.find('windows') != -1:
        action = ContextHolder.get_action_chain()
        action.send_keys(Keys.F11).perform()
        pass
    elif os.find('linux') != -1:
        action = ContextHolder.get_action_chain()
        action.send_keys(Keys.F11).perform()
        pass


def reset_implicitly_wait():
    # logger.debug("Reset implicitly wait")
    ContextHolder.implicitly_wait = 0
    ContextHolder.get_driver().implicitly_wait(0)


def set_implicitly_wait(
        timeout=ContextHolder.DEFAULT_WEBDRIVER_IMPLICITLY_WAIT_TIME):
    # logger.debug("Set implicitly wait: {}".format(timeout))
    ContextHolder.implicitly_wait = timeout
    ContextHolder.get_driver().implicitly_wait(timeout)


def start_driver():
    browser = ContextHolder.get_browser()

    def start_chrome():
        logger.info("Start chrome")
        return webdriver.Chrome()

    def start_firefox():
        logger.info("Start firefox")
        return webdriver.Firefox()

    def start_iexplore():
        logger.info("Start IE")
        return webdriver.Ie()

    if browser == "firefox":
        driver = start_firefox()
    elif browser == "iexplore":
        driver = start_iexplore()
    elif browser == "chrome":
        driver = start_chrome()
    else:
        raise PoteenError("Unexpected browser {}".format(str(browser)))

    ContextHolder.set_driver(driver)
    maximize_window()
    driver = ContextHolder.get_driver()
    driver.set_page_load_timeout(
        ContextHolder.DEFAULT_WEBDRIVER_WAIT_LOAD_TIMEOUT)
    set_implicitly_wait(ContextHolder.DEFAULT_WEBDRIVER_IMPLICITLY_WAIT_TIME)


def close_driver():
    if not ContextHolder.get_driver() is None:
        logger.info("Close driver")
        ContextHolder.get_driver().quit()
        ContextHolder.set_driver(None)
