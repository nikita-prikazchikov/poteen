from elements.BaseElement import BaseElement

__author__ = 'nprikazchikov'


class Button(BaseElement):
    def __init__(self, *args, **kwargs):
        BaseElement.__init__(self, *args, **kwargs)
        self._type = "button"