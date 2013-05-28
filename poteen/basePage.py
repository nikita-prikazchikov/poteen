from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from .contextHolder import ContextHolder
from .bots.actionBot import ActionBot
from .bots.verifyBot import VerifyBot
from .bots.waitBot import WaitBot
from .elements.baseElement import BaseElement
from .log.result import Result

__author__ = 'nprikazchikov'


class BasePage:
    url = None
    _name = None
    _action_bot = ActionBot()
    _verify_bot = VerifyBot()
    _wait_bot = WaitBot(ContextHolder.DEFAULT_WEBDRIVER_IMPLICITLY_WAIT_TIME)
    _parent = None

    def __init__(self, parent=None):
        self.url = None
        self._name = None
        self._parent = self.init_class_elements(parent)
        self.init_instance_elements(self._parent)

    @classmethod
    def get_action_bot(cls):
        return cls._action_bot

    @classmethod
    def get_wait_bot(cls):
        return cls._wait_bot

    @classmethod
    def get_verify_bot(cls):
        return cls._verify_bot

    def init_instance_elements(self, parent=None):
        if parent is None or not \
            (isinstance(parent, WebDriver) or isinstance(parent, WebElement)):
            parent = ContextHolder.get_driver()
        for element in iter(self.__dict__.iteritems()):
            if isinstance(element[1], BaseElement):
                element[1].set_parent(parent)
        return parent

    @classmethod
    def init_class_elements(cls, parent=None):
        if parent is None or not \
            (isinstance(parent, WebDriver) or isinstance(parent, WebElement)):
            parent = ContextHolder.get_driver()
        for element in iter(cls.__dict__.iteritems()):
            if isinstance(element[1], BaseElement):
                element[1].set_parent(parent)
        if len(cls.__bases__) != 0:
            for base in cls.__bases__:
                base.init_class_elements(parent=parent)
        return parent

    def navigate(self):
        if not self.url is None:
            return self._action_bot.navigate(
                ContextHolder.get_url() + self.url)
        else:
            return Result(
                "Page [{page}]URL is not provided. Can't navigate"
                .format(page=self.__class__)
                , False)