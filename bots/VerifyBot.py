import logging
from bots.baseBot import BaseBot
from log.Result import Result
from utils.Status import Status

__author__ = 'nprikazchikov'

logger = logging.getLogger("bots.VerifyBot")


class VerifyBot(BaseBot):
    def _not(self, value):
        return "" if value else " not"

    def _verify_web_element_visibility(self, expected, actual, name,
                                       _type="element"):
        return Result(
            "{type} [{name}] is{status} visible".format(
                type=_type,
                name=name,
                status=self._not(actual)
            ),
            Status.get_status(actual == expected)
        )

    def verify_contains(self, expected, actual, name, _type="element"):
        status = actual.find(expected) != -1
        if status:
            return Result(
                "{type} {name} value is{status} correct. Expected: [{"
                "expected}] ".format(
                    type=_type,
                    name=name,
                    status=self._not(status),
                    expected=expected,
                )
            )
        else:
            return Result(
                "{type} {name} value is{status} correct. Expected: [{"
                "expected}] contains in: [{actual}]".format(
                    type=_type,
                    name=name,
                    status=self._not(status),
                    expected=expected,
                    actual=actual
                )
            )

    def verify_equal(self, expected, actual, name, _type="element"):
        status = actual == expected
        if status:
            return Result(
                "{type} {name} value is{status} correct. Expected: "
                "[{expected}] ".format(
                    type=_type,
                    name=name,
                    status=self._not(status),
                    expected=expected
                )
            )
        else:
            return Result(
                "{type} {name} value is{status} correct. Expected: [{"
                "expected}] current: [{actual}]".format(
                    type=_type,
                    name=name,
                    status=self._not(status),
                    expected=expected,
                    actual=actual
                )
            )

    def verify_visibility(self, web_element, displayed, name, _type="element"):
        return self._verify_web_element_visibility(
            displayed,
            self.is_element_displayed(web_element),
            name,
            _type
        )
