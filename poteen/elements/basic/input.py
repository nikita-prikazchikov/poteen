from ..baseElement import BaseElement

__author__ = 'nprikazchikov'


class Input(BaseElement):
    def __init__(self, *args, **kwargs):
        BaseElement.__init__(self, *args, **kwargs)
        self._type = "input (textarea)"
