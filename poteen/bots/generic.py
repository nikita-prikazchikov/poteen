import logging
import platform
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from ..contextHolder import ContextHolder
from ..error import PoteenError

__author__ = 'nprikazchikov'


def switch_to_default_content():
    ContextHolder.get_driver().switch_to_default_content()


def maximize_window():
    ContextHolder.get_driver().maximize_window()
    os = platform.uname()[0].lower()
    if os.find('windows') != -1:
        action = ContextHolder.get_action_chain()
        action \
            .send_keys(Keys.F11) \
            .perform()
        pass
    elif os.find('linux') != -1:
        pass


def reset_implicitly_wait():
    ContextHolder.get_driver().implicitly_wait(0)


def set_implicitly_wait(
        timeout=ContextHolder.DEFAULT_WEBDRIVER_IMPLICITLY_WAIT_TIME):
    ContextHolder.get_driver().implicitly_wait(timeout)


def setup_logger():
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s %(name)-12s %(levelname)-8s %('
               'message)s',
        datefmt='%m-%d %H:%M',
        # filename='/temp/myapp.log',
        # filemode='w'
    )


def start_driver():
    browser = ContextHolder.get_browser()

    def start_chrome():
        return webdriver.Chrome()

    def start_firefox():
        return webdriver.Firefox()

    def start_iexplore():
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
        ContextHolder.get_driver().quit()
        ContextHolder.set_driver(None)