import cgi
from ContextHolder import ContextHolder
from log.Screenshot import ScreenshotMaker
from log.iResult import iResult
from utils.Status import Status

__author__ = 'nprikazchikov'


class Result(iResult):
    _comment = None
    _screenshot = None
    _status = None

    def __init__(self, comment="", status=True):
        self._screenshot = None
        self._comment = cgi.escape(str(comment), True)
        self.set_status(status)

    def i_passed(self):
        if self._status is Status.PASSED:
            return True
        else:
            return False

    def get_status(self):
        return self._status

    def get_comment(self):
        return self._comment

    def set_status(self, status=False, no_screenshot=False):

        if isinstance(status, bool):
            self._status = Status.PASSED if status else Status.FAILED
        else:
            self._status = status

        if Status.is_failed(self._status) and not no_screenshot:
            self._screenshot = ScreenshotMaker().take_screenshot(
                "Test suite: {}; Test case: {}; {}".format(
                    ContextHolder.get_test_suite(),
                    ContextHolder.get_test_case(),
                    self._comment
                )
            )

    def __repr__(self):
        return str(self)

    def __str__(self):
        return '{' + '"status":"{status}","comment":"{comment}",' \
                     '"images":"[{images}]"' \
            .format(
                status=self._status,
                comment=self._comment,
                images="" if self._screenshot is None else str(
                    self._screenshot)
            ) + '}'

