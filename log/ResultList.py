import cgi
from log.Result import Result
from log.iResult import iResult
from utils.Status import Status

__author__ = 'nprikazchikov'


class ResultList(iResult):
    _comment = None
    _parent = None
    _elements = []

    def __init__(self, comment="", parent=None):
        self._comment = cgi.escape(comment, True)
        self._parent = parent

    def i_passed(self):
        if self.get_status() is Status.PASSED:
            return True
        else:
            return False

    def get_status(self):
        def calculate(a, b):
            return Status.get_worse_status(a, b.get_status())

        return reduce(calculate, self._elements, Status.PASSED)

    def get_comment(self):
        return self._comment

    def push(self, result):
        self._elements.append(result)
        return self

    def info(self, message):
        self._elements.append(Result(message))
        return self

    def __repr__(self):
        return str(self)

    def __str__(self):
        children = reduce(
            lambda a, b: a + "," + str(b),
            self._elements,
            ""
        )
        return '{' + '"status":"{status}","comment":"{comment}",' \
                     'children:[{children}]' \
            .format(
            status=self.get_status(),
            comment=self._comment,
            children=children[1:]
        ) + '}'