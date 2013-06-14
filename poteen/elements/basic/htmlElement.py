from ..baseElement import BaseElement
from ...error import IllegalElementActionException

__author__ = 'nprikazchikov'


class HtmlElement(BaseElement):
    def __init__(self, *args, **kwargs):
        BaseElement.__init__(self, *args, **kwargs)
        self._type = "html element"

    def get_value(self):
        return self.get_element().text

    def set_value(self, value):
        raise IllegalElementActionException(
            "Unable to set value for {}".format(self._element_name)
        )
