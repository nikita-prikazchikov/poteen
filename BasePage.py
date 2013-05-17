from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from ContextHolder import ContextHolder
from elements import BaseElement

__author__ = 'nprikazchikov'


class BasePage:
    _element = BaseElement(**{By.XPATH: "//input", BaseElement.NAME: "Input"})

    _element2 = BaseElement(xpath="//input2", name="Input2")

    def __init__(self):
        self.init_elements()
        pass

    def get_element(self):
        t = self._element.click()
        x = 1

    @classmethod
    def init_elements(cls, parent=None):
        if parent is None \
            or not isinstance(parent, WebDriver) \
            or not isinstance(
                parent, WebElement):
            parent = ContextHolder.get_driver()
        for element in iter(cls.__dict__.iteritems()):
            if isinstance(element[1], BaseElement):
                element[1].set_parent(parent)