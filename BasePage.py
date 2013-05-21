from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from ContextHolder import ContextHolder
from bots.ActionBot import ActionBot
from bots.VerifyBot import VerifyBot
from bots.WaitBot import WaitBot
from elements.BaseElement import BaseElement
from log.Result import Result

__author__ = 'nprikazchikov'


class BasePage:
    url = None
    name = None
    _action_bot = ActionBot()
    _verify_bot = VerifyBot()
    _wait_bot = WaitBot(ContextHolder.DEFAULT_WEBDRIVER_IMPLICITLY_WAIT_TIME)

    def __init__(self, parent=None):
        self.init_elements(parent)

    @classmethod
    def get_action_bot(cls):
        return cls._action_bot

    @classmethod
    def get_wait_bot(cls):
        return cls._wait_bot

    @classmethod
    def get_verify_bot(cls):
        return cls._verify_bot

    @classmethod
    def init_elements(cls, parent=None):
        if parent is None \
            or not isinstance(parent, WebDriver) \
            or not isinstance(parent, WebElement):
            parent = ContextHolder.get_driver()
        for element in iter(cls.__dict__.iteritems()):
            if isinstance(element[1], BaseElement):
                element[1].set_parent(parent)

    def navigate(self):
        if not self.url is None:
            return self._action_bot.navigate(
                ContextHolder.get_url() + self.url)
        else:
            return Result(
                "Page [{page}]URL is not provided. Can't navigate"
                .format(page=self.__class__)
                , False)