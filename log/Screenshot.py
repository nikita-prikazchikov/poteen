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
