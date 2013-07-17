import logging
from .baseBot import BaseBot
from ..contextHolder import ContextHolder
from engine.poteen.error import ElementNotFoundException
from ..log.result import Result
from ..utils.status import Status

__author__ = 'nprikazchikov'

logger = ContextHolder.get_logger()


class VerifyBot(BaseBot):
    def _not(self, value):
        return "" if value else " not"

    def _verify_web_element_visibility(self, expected, actual, name,
                                       _type="element"):
        logger.debug("Verify {type} [{name}] is {status} visible".format(
            type=_type,
            name=name,
            status=self._not(actual)
        ))
        return Result(
            "{type} [{name}] is{status} visible".format(
                type=_type,
                name=name,
                status=self._not(actual)
            ),
            Status.get_status(actual == expected)
        )

    def verify_contains(self, expected, actual, name, _type="element"):
        logger.debug("Verify {type} {name} value. Expected: "
                     "[{expected}] contains in: [{actual}]".format(
                         type=_type,
                         name=name,
                         expected=expected,
                         actual=actual
                     ))
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
                ),
                Status.FAILED
            )

    def verify_equal(self, expected, actual, name, _type="element"):
        logger.debug("Verify {type} {name} value. Expected: "
                     "[{expected}] equals: [{actual}]".format(
                         type=_type,
                         name=name,
                         expected=expected,
                         actual=actual
                     ))
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
                ),
                Status.FAILED
            )

    def verify_visibility(self, web_element, displayed, name, _type="element"):
        return self._verify_web_element_visibility(
            displayed,
            self.is_element_displayed(web_element),
            name,
            _type
        )

    def verify_exists_and_visible(self, element, exists_and_visible, name, _type="element"):
        try:
            web_element = element.get_element()
        except ElementNotFoundException:
            pass
        return self._verify_web_element_visibility(
            exists_and_visible,
            'web_element' in locals() and self.is_element_displayed(web_element),
            name,
            _type
        )

    def verify_contains_attribute(self, web_element, attribute_name,
                                  attribute_value, name, _type="element"):
        logger.debug("Verify {type} {name} has attribute {attr}:{val}".format(
            type=_type,
            name=name,
            attr=attribute_name,
            val=attribute_value
        ))
        status = web_element.get_attribute(attribute_name) == attribute_value
        return Result(
            "{type} {name} have attribute {attr}:{val}"
            .format(
                type=_type,
                name=name,
                attr=attribute_name,
                val=attribute_value
            ),
            status
        )
