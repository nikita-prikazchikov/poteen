import cgi
from .iResult import iResult
from .result import Result
from ..error import TestExecutionRuntimeException
from ..utils.status import Status

__author__ = 'nprikazchikov'


class ResultList(iResult):
    __chain = []

    _comment = None
    _parent = None
    _elements = []

    @classmethod
    def add_chain_result_list(cls, i_result):
        cls.__chain.append(i_result)

    @classmethod
    def clear_chain_result_list(cls):
        cls.__chain = []

    @classmethod
    def get_chain_result_list(cls):
        return cls.__chain

    def __init__(self, comment="", parent=None):
        if not isinstance(comment, str):
            comment = str(comment)
        self._comment = cgi.escape(comment, True)
        self._parent = parent
        self._elements = []
        ResultList.add_chain_result_list(self)

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

    def push(self, result, blocking=True):
        self._elements.append(result)
        if blocking and Status.is_failed(result.get_status()):
            raise TestExecutionRuntimeException(str(result))
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
        _str = '"status":"{status}","comment":"{comment}", ' \
               '"children":[{children}]'.format(
               status=self.get_status(),
               comment=self._comment,
               children=children[1:]
               )
        return '{' + _str + '}'
