from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys
from .baseBot import BaseBot
from .generic import switch_to_default_content
from ..contextHolder import ContextHolder
from ..error import IllegalElementActionException
from ..log.result import Result
from ..utils.status import Status

__author__ = 'nprikazchikov'

logger = ContextHolder.get_logger()


class ActionBot(BaseBot):
    def _clear(self, web_element, invisible=False):
        status = Status.FAILED
        try:
            logger.debug("Clean web element")
            if invisible or self.is_element_displayed(web_element):
                web_element.clear()
                status = Status.PASSED
        except WebDriverException, e:
            logger.error(str(e))
        return status

    def _clear_ctrl_a_del(self, web_element, invisible=False):
        status = Status.FAILED
        try:
            logger.debug("Clean web element with Ctrl+A -> Delete")
            if invisible or self.is_element_displayed(web_element):
                ContextHolder.get_action_chain() \
                    .key_down(Keys.CONTROL, web_element) \
                    .send_keys_to_element(web_element, "a") \
                    .key_up(Keys.CONTROL, web_element) \
                    .send_keys_to_element(web_element, Keys.DELETE) \
                    .perform()
                status = Status.PASSED
        except WebDriverException, e:
            logger.error(str(e))
        return status

    def _click(self, web_element, invisible=False):
        """
        :param web_element: Web element
        :return: string from Status
        """
        status = Status.FAILED
        try:
            logger.debug("Click web element")
            if invisible or self.is_element_displayed(web_element):
                web_element.click()
                status = Status.PASSED
        except WebDriverException, e:
            logger.error(str(e))
        return status

    def _click_dom(self, web_element, invisible=False):
        status = Status.FAILED
        try:
            logger.debug("Click DOM web element")
            if invisible or self.is_element_displayed(web_element):
                ContextHolder.get_action_chain().click(web_element).perform()
                status = Status.PASSED
        except WebDriverException, e:
            logger.error(str(e))
        return status

    def _click_context(self, web_element, invisible=False):
        status = Status.FAILED
        try:
            logger.debug("Context click web element")
            if invisible or self.is_element_displayed(web_element):
                ContextHolder.get_action_chain().context_click(
                    web_element).perform()
                status = Status.PASSED
        except WebDriverException, e:
            logger.error(str(e))
        return status

    def _double_click(self, web_element, invisible=False):
        status = Status.FAILED
        try:
            logger.debug("Double click web element")
            if invisible or self.is_element_displayed(web_element):
                ContextHolder.get_action_chain().double_click(
                    web_element).perform()
                status = Status.PASSED
        except WebDriverException, e:
            logger.error(str(e))
        return status

    def _drag_and_drop(self, web_element_source, web_element_target,
                       invisible=False):
        status = Status.FAILED
        try:
            logger.debug("Drad and drop {element} on {element2}".format(
                element=web_element_source,
                element2=web_element_target
            ))
            if invisible or (
                    self.is_element_displayed(web_element_source) and
                    self.is_element_displayed(web_element_target)):
                ContextHolder.get_action_chain().drag_and_drop(
                    web_element_source, web_element_target).perform()
                status = Status.PASSED
        except WebDriverException, e:
            logger.error(str(e))
        return status

    def _drag_and_drop_by_offset(self, web_element_source, x_offset, y_offset,
                                 invisible=False):
        status = Status.FAILED
        try:
            logger.debug("Drag {element} on x:{x} y:{y}".format(
                element=web_element_source,
                x=x_offset,
                y=y_offset
            ))
            if invisible or self.is_element_displayed(web_element_source):
                ContextHolder.get_action_chain() \
                    .drag_and_drop_by_offset(web_element_source, x_offset,
                                             y_offset).perform()
                status = Status.PASSED
        except WebDriverException, e:
            logger.error(str(e))
        return status

    def _set_value(self, web_element, value, invisible=False):
        status = Status.FAILED
        try:
            if invisible or self.is_element_displayed(web_element):
                web_element.clear()
                web_element.send_keys(value)
                status = Status.PASSED
        except WebDriverException, e:
            logger.error(str(e))
        return status

    def _is_selected(self, web_element, invisible=False):
        status = None
        try:
            if invisible or self.is_element_displayed(web_element):
                status = web_element.is_selected()
        except WebDriverException, e:
            logger.error(str(e))
        return status

    def _send_keys(self, web_element, value, invisible=False):
        status = Status.FAILED
        try:
            logger.debug("Send keys {value}".format(
                value=value
            ))
            if invisible or self.is_element_displayed(web_element):
                web_element.send_keys(value)
                status = Status.PASSED
        except WebDriverException, e:
            logger.error(str(e))
        return status

    def alert_accept(self):
        status = Status.FAILED
        try:
            self.wait_for_time(0.5)
            logger.debug("Alert accept")
            alert = ContextHolder.get_driver().switch_to_alert()
            text = "Accept: {}".format(alert.text())
            alert.accept()
            self.wait_loading()
            status = Status.PASSED
        except WebDriverException, e:
            logger.error(str(e))
            text = "Unable to accept alert"
        finally:
            switch_to_default_content()

        return Result(text, status)

    def alert_dismiss(self):
        status = Status.FAILED
        try:
            self.wait_for_time(0.5)
            logger.debug("Alert dismiss")
            alert = ContextHolder.get_driver().switch_to_alert()
            text = "Dismiss: {}".format(alert.text())
            alert.dismiss()
            self.wait_loading()
            status = Status.PASSED
        except WebDriverException, e:
            logger.error(str(e))
            text = "Unable to dismiss alert"
        finally:
            switch_to_default_content()

        return Result(text, status)

    def clear(self, web_element, name, invisible=False):
        return Result(
            "Clear element [{name}]".format(name=name),
            self._clear(web_element, invisible)
        )

    def clear_ctrl_a_del(self, web_element, name, invisible=False):
        return Result(
            "Clear element [{name}] by pressing {}"
            .format("{CTRL}+A -> {DELETE}", name=name),
            self._clear_ctrl_a_del(web_element, invisible)
        )

    def click(self, web_element, name, _type="element", invisible=False):
        return Result(
            "Click {type} [{name}]".format(type=_type, name=name),
            self._click(web_element, invisible)
        )

    def click_and_wait(self, web_element, name, _type="element",
                       invisible=False):
        res = Result(
            "Click {type} [{name}] and wait loading"
            .format(type=_type, name=name),
            self._click(web_element, invisible)
        )
        self.wait_loading()
        return res

    def click_dom(self, web_element, name, _type="element", invisible=False):
        return Result(
            "DOM Click {type} [{name}]".format(type=_type, name=name),
            self._click_dom(web_element, invisible)
        )

    def click_dom_and_wait(self, web_element, name, _type="element",
                           invisible=False):
        res = Result(
            "DOM Click {type} [{name}] and wait loading"
            .format(type=_type, name=name),
            self._click_dom(web_element, invisible)
        )
        self.wait_loading()
        return res

    def click_context(self, web_element, name, _type="element",
                      invisible=False):
        return Result(
            "Context click {type} [{name}]".format(type=_type, name=name),
            self._click_context(web_element, invisible)
        )

    def click_context_and_wait(self, web_element, name, _type="element",
                               invisible=False):
        res = Result(
            "Context click {type} [{name}] and wait loading"
            .format(type=_type, name=name),
            self._click_context(web_element, invisible)
        )
        self.wait_loading()
        return res

    def double_click(self, web_element, name, _type="element",
                     invisible=False):
        return Result(
            "Click {type} [{name}]".format(type=_type, name=name),
            self._double_click(web_element, invisible)
        )

    def double_click_and_wait(self, web_element, name, _type="element",
                              invisible=False):
        res = Result(
            "Click {type} [{name}] and wait loading"
            .format(type=_type, name=name),
            self._double_click(web_element, invisible)
        )
        self.wait_loading()
        return res

    def drag_and_drop(self, web_element_source, web_element_target,
                      source_name, target_name, invisible=False):
        return Result(
            "Drag and drop element [{source}] on [{target}]"
            .format(source=source_name, target=target_name),
            self._drag_and_drop(
                web_element_source, web_element_target, invisible)
        )

    def drag_and_drop_by_offset(self, web_element_source, x_offset, y_offset,
                                source_name, target_name="target",
                                invisible=False):
        return Result(
            "Drag and drop element [{source}] on [{target}] X:{x} Y:{y}"
            .format(
                source=source_name,
                target=target_name,
                x=x_offset,
                y=y_offset
            ),
            self._drag_and_drop_by_offset(web_element_source, x_offset,
                                          y_offset, invisible)
        )

    def is_selected(self, web_element, name, invisible=False):
        """
        :param web_element:
        :param name:
        :return: bool
        :raise: IllegalElementActionException
        """
        res = self._is_selected(web_element, invisible)
        if res is None:
            raise IllegalElementActionException(
                "Checkbox [{name}] has illegal value or invisible value"
                .format(
                    name=name))
        return res

    def navigate(self, url):
        status = Status.FAILED
        message = "Navigate to [{url}]".format(url=url)
        logger.info(message)
        try:
            ContextHolder.get_driver().get(url)
            status = Status.PASSED
        except WebDriverException, e:
            logger.error("{} {}".format(repr(e), str(e)))
        return Result(message, status)

    def set_value(self, web_element, value, name, _type="element",
                  invisible=False):
        return Result(
            "Set {type} [{name}] value [{value}]"
            .format(type=_type, name=name, value=value),
            self._set_value(web_element, value, invisible)
        )

    def send_keys(self, web_element, value, name, _type="element",
                  invisible=False):
        return Result(
            "Send to {type} keys [{name}]".format(type=_type, name=name),
            self._send_keys(web_element, value, invisible)
        )
