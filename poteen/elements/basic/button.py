from ..baseElement import BaseElement
from ...error import IllegalElementActionException

__author__ = 'nprikazchikov'


class Button(BaseElement):
    def __init__(self, *args, **kwargs):
        BaseElement.__init__(self, *args, **kwargs)
        self._type = "button"

    def set_value(self, value):
        raise IllegalElementActionException(
            "Unable to set value for {} {}"
            .format(self._type, self._element_name)
        )
