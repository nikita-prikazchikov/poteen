from ..baseElement import BaseElement
from ...contextHolder import ContextHolder

__author__ = 'nprikazchikov'

logger = ContextHolder.get_logger()


class Input(BaseElement):
    def __init__(self, *args, **kwargs):
        BaseElement.__init__(self, *args, **kwargs)
        self._type = "input (textarea)"
