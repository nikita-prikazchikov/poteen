from datetime import datetime
from ..contextHolder import ContextHolder

__author__ = 'nprikazchikov'


class Screenshot(object):
    name = str
    url = str

    def __init__(self, name, url):
        self.name = name
        self.url = url

    def __repr__(self):
        return str(self)

    def __str__(self):
        return '{' + '"name":"{name}","url":"{url}"'.format(name=self.name,
                                                            url=self.url) + '}'


class ScreenshotMaker:
    def take_screenshot(self, message=""):
        """
        :param message: comment for screenshot to display. DO screenshot
        flag has to be set to True in ContextHolder
        :return: Screenshot|None
        """
        if (ContextHolder.get_do_screenshot()):
            working_dir = ContextHolder.get_workspace_path()
            path = "{path}{name}.png".format(
                path="/../result/images/",
                name=datetime.now().strftime("%Y_%m_%d__%H_%M_%S"))
            if ContextHolder.get_driver().save_screenshot(working_dir + path):
                return Screenshot(
                    "Test suite {}; Test case {}; {}".format(
                        ContextHolder.get_test_suite(),
                        ContextHolder.get_test_case(),
                        message
                    ),
                    path)
            else:
                return None
        else:
            return None
