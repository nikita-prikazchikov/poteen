import logging
import platform
from selenium.webdriver.common.keys import Keys
from ..ContextHolder import ContextHolder

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
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(name)-12s %(levelname)-8s %('
                               'message)s',
                        datefmt='%m-%d %H:%M',
                        # filename='/temp/myapp.log',
                        # filemode='w'
    )