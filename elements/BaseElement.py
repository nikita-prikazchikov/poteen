from selenium.webdriver.common.by import By
from bots.ActionBot import ActionBot

__author__ = 'nprikazchikov'


class BaseElement:
    _by = By.ID
    _value = None
    _element = None
    _type = None
    _element_name = None
    _parent = None

    def __init__(self, *args, **kwargs):
        for key, value in kwargs.iteritems():
            if key in self._get_possible_set():
                self._by = key
                self._value = value
            if key == "by":
                self._by = value
            if key == "value":
                self._value = value
            if key == "element_name":
                self._element_name = value
        pass

    def _get_possible_set(self):
        return {By.ID, By.XPATH, By.CLASS_NAME, By.CSS_SELECTOR, By.LINK_TEXT,
                By.NAME, By.PARTIAL_LINK_TEXT, By.TAG_NAME}

    def get_element(self):
        if self._element is None:
            self._element = ActionBot().find_element(
                by=self._by,
                value=self._value,
                parent=self._parent)
        return self._element

    def find(self, **kwargs):
        pass

    @classmethod
    def set_parent(cls, parent):
        cls._parent = parent

    def click(self):
        return ActionBot().click(
            web_element=self.get_element(),
            name=self._element_name,
            _type=self._type)

    def get_value(self):
        self.get_element().get_attribute("value")

    def set_value(self, value):
        return ActionBot().set_value(
            web_element=self.get_element(),
            value=value,
            name=self._element_name,
            _type=self._type
        )