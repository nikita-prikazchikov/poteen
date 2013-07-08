from datetime import datetime
import json
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
        return json.dumps(self.json())

    def json(self):
        return {
            "type": "image",
            "name": self.name,
            "url": self.url
        }


class ScreenshotMaker:
    def take_screenshot(self, message=""):
        """
        :param message: comment for screenshot to display. DO screenshot
        flag has to be set to True in ContextHolder
        :return: Screenshot|None
        """
        if ContextHolder.get_do_screenshot():
            working_dir = ContextHolder.get_workspace_path()
            name = datetime.now().strftime("%Y_%m_%d__%H_%M_%S")
            path = "{path}{name}.png".format(
                path="/../result/images/",
                name=name)
            if ContextHolder.get_driver().save_screenshot(working_dir + path):
                return Screenshot(message, "images/{name}.png".format(
                    name=name
                ))
            else:
                return None
        else:
            return None
