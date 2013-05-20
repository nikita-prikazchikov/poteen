from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from ContextHolder import ContextHolder
from bots.ActionBot import ActionBot
from bots.VerifyBot import VerifyBot
from elements.BaseElement import BaseElement
from log.Result import Result

__author__ = 'nprikazchikov'


class BasePage:
    url = None
    name = None
    action_bot = None
    verify_bot = None

    # _element = BaseElement(**{By.XPATH: "//input",
    # BaseElement.NAME: "Input"})
    #
    # _element2 = BaseElement(xpath="//input2", name="Input2")

    def __init__(self):
        self.init_elements()
        self.action_bot = ActionBot()
        self.verify_bot = VerifyBot()
        pass

    def get_element(self):
        t = self._element.click()
        x = 1

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
            return self.action_bot.navigate(self.url)
        else:
            return Result(
                "Page [{page}]URL is not provided. Can't navigate"
                .format(page = self.__class__)
                , False)