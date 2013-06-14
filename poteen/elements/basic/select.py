from selenium.webdriver.common.by import By

from .htmlElement import HtmlElement
from ..baseElement import BaseElement
from ...error import PoteenError
from ...log.result import Result
from ...log.resultList import ResultList

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
                element_name="option [{}]".format(value)
            )
            res.push(option.click())
            res.push(self.verify_value(value), False)
        except PoteenError, e:
            res.push(Result(e.message, False))
        return res
