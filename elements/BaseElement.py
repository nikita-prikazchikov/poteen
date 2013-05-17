from selenium.webdriver.common.by import By

__author__ = 'nprikazchikov'


class BaseElement:
    _by = By.ID
    _element = None
    _name = str
    _parent = None

    def __init__(self, *args, **kwargs):
        pass

    def get_element(self):
        if self._element is None:
            # self._element = self._parent
            pass

    @classmethod
    def set_parent(cls, parent):
        cls._parent = parent

    def click(self):
        self.get_element().click()