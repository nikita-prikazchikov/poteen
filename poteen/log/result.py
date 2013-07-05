import json
from .iResult import iResult
from .screenshot import ScreenshotMaker
from ..contextHolder import ContextHolder
from ..utils.status import Status

__author__ = 'nprikazchikov'


class Result(iResult):
    _comment = None
    _files = []
    _status = None

    def __init__(self, comment="", status=True):
        self._files = []
        self._comment = str(comment)
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
        elif status is None:
            self._status = Status.FAILED
        else:
            self._status = status

        if Status.is_failed(self._status) and not no_screenshot:
            self._files.append(ScreenshotMaker().take_screenshot(
                "Test suite: {}; Test case: {}; {}".format(
                    ContextHolder.get_test_suite(),
                    ContextHolder.get_test_case(),
                    self._comment
                )
            ))

    def _get_files_as_object(self):
        res = []
        for element in self._files:
            res.append(element.json())
        return res

    def __repr__(self):
        return str(self)

    def __str__(self):
        return json.dumps(
            {
                "status": self._status,
                "comment": self._comment,
                "files": self._get_files_as_object()
            }
        )
