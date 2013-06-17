from ..baseElement import BaseElement
from ...contextHolder import ContextHolder
from ...log.result import Result
from ...log.resultList import ResultList

from ...error import IllegalElementActionException

__author__ = 'nprikazchikov'

logger = ContextHolder.get_logger()


class Radio(BaseElement):
    VALUE_ON = "on"
    VALUE_OFF = "off"

    def __init__(self, *args, **kwargs):
        BaseElement.__init__(self, *args, **kwargs)
        self._type = "radiobutton"

    def __check_value(self, value):
        if isinstance(value, bool):
            value = self.VALUE_ON if value else self.VALUE_OFF

        if not (value == self.VALUE_ON or value == self.VALUE_OFF):
            IllegalElementActionException(
                "Unexpected radiobutton value. Please use {} or {} constants"
                " from checkbox class or bool".format(
                    self.VALUE_ON, self.VALUE_OFF
                )
            )
        return value

    def get_value(self):
        return self.VALUE_ON \
            if self.get_element().is_selected() \
            else self.VALUE_OFF

    def set_value(self, value):
        value = self.__check_value(value)

        res = ResultList("Set radiobutton [{}] to: [{}]".format(
            self._element_name, value
        ))
        if not self.get_value() == value:
            res.push(self.click())
        else:
            res.push(
                Result(
                    "The radiobutton [{}] already set to: [{}]".format(
                        self._element_name,
                        value
                    )
                )
            )
        return res

    def verify_value(self, value):
        value = self.__check_value(value)
        return BaseElement.verify_value(self, value)
