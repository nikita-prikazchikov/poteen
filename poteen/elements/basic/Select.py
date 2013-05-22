from selenium.webdriver.common.by import By

from .HtmlElement import HtmlElement
from ..BaseElement import BaseElement
from ...error import PoteenError
from ...log.Result import Result
from ...log.ResultList import ResultList

__author__ = 'nprikazchikov'


class Select(BaseElement):
    def __init__(self, *args, **kwargs):
        BaseElement.__init__(self, *args, **kwargs)
        self._type = "select"

    def get_value(self):
        return self.get_element().find_element(
            By.CSS_SELECTOR, "option:checked"
        ).text

    def set_value(self, value):
        res = ResultList("Set select [{}] value: [{}]".format(
            self._element_name, value
        ))
        try:
            option = HtmlElement(element=self.get_element().find_element(
                By.XPATH, "//option[contains(text(),'{}')]".format(value)),
                                 element_name="option [{}]".format(value))
            res.push(option.click())
            res.push(self.verify_value(value), False)
        except PoteenError, e:
            res.push(Result(e.message, False))
        return res
        
    