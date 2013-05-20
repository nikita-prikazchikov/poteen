from BasePage import BasePage
from elements.basic.Button import Button
from elements.basic.Input import Input

__author__ = 'nprikazchikov'


class GooglePage(BasePage):
    search = Input(id="gbqfq", element_name="Search")

    button = Button(id="gbqfb", element_name="Search")

    def __init__(self):
        BasePage.__init__(self)
        self.url = "https://www.google.ru/"