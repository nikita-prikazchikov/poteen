from selenium.webdriver.common.by import By
from ...contextHolder import ContextHolder

from .htmlElement import HtmlElement
from ..baseElement import BaseElement
from ...error import PoteenError
from ...log.result import Result
from ...log.resultList import ResultList

__author__ = 'nprikazchikov'

logger = ContextHolder.get_logger()


class Select(BaseElement):
    def __init__(self, *args, **kwargs):
        BaseElement.__init__(self, *args, **kwargs)
        self._type = "select"

    def get_value(self):
        options = self.get_element().find_elements(By.CSS_SELECTOR, "option")
        for option in options:
            if option.is_selected():
                return option.text

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
