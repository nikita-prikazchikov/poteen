from selenium.webdriver.common.by import By
from ..bots.ActionBot import ActionBot
from ..bots.VerifyBot import VerifyBot
from ..error import ElementNotFoundException
from ..log.Result import Result
from ..log.ResultList import ResultList
from ..utils.Status import Status

__author__ = 'nprikazchikov'


class BaseElement:
    _by = By.ID
    _value = None
    _element = None
    _type = None
    _element_name = None
    _parent = None

    def __init__(self, *args, **kwargs):

        self._by = By.ID
        self._value = None
        self._element = None
        self._type = None
        self._element_name = None
        self._parent = None

        for key, value in kwargs.iteritems():
            if key in self._get_possible_set():
                self._by = key
                self._value = value
            if key == "by":
                self._by = value
            if key == "value":
                self._value = value
            if key == "element_name":
                self._element_name = value
            if key == "element":
                self._element = value
        pass

    @classmethod
    def set_parent(cls, parent):
        cls._parent = parent

    def _get_possible_set(self):
        return {By.ID, By.XPATH, By.CLASS_NAME, By.CSS_SELECTOR, By.LINK_TEXT,
                By.NAME, By.PARTIAL_LINK_TEXT, By.TAG_NAME}

    def click(self):
        return ActionBot().click(
            web_element=self.get_element(),
            name=self._element_name,
            _type=self._type
        )

    def click_and_wait(self):
        return ActionBot().click_and_wait(
            web_element=self.get_element(),
            name=self._element_name,
            _type=self._type
        )

    def click_context(self):
        return ActionBot().click_context(
            web_element=self.get_element(),
            name=self._element_name,
            _type=self._type
        )

    def click_context_and_wait(self):
        return ActionBot().click_context_and_wait(
            web_element=self.get_element(),
            name=self._element_name,
            _type=self._type
        )

    def click_dom(self):
        return ActionBot().click_dom(
            web_element=self.get_element(),
            name=self._element_name,
            _type=self._type
        )

    def click_dom_and_wait(self):
        return ActionBot().click_dom_and_wait(
            web_element=self.get_element(),
            name=self._element_name,
            _type=self._type
        )

    def double_click(self):
        return ActionBot().double_click(
            web_element=self.get_element(),
            name=self._element_name,
            _type=self._type
        )

    def double_click_and_wait(self):
        return ActionBot().double_click_and_wait(
            web_element=self.get_element(),
            name=self._element_name,
            _type=self._type
        )

    def find(self, **kwargs):
        pass

    def get_element(self):
        """
        :raise: ElementNotFoundException
        :return:
        """
        if not self.is_found():
            self._element = ActionBot().find_element(
                by=self._by,
                value=self._value,
                parent=self._parent)
            if not self.is_found():
                message = \
                    "{} [{}] not found By.{}:{}".format(
                        self._type,
                        self._element_name,
                        self._by,
                        self._value
                    )
                ResultList.add_chain_result_list(
                    Result(message, Status.FAILED)
                )
                raise ElementNotFoundException(message)
        return self._element

    def get_value(self):
        return self.get_element().get_attribute("value")

    def is_found(self):
        return not self._element is None

    def set_value(self, value):
        return ActionBot().set_value(
            web_element=self.get_element(),
            value=value,
            name=self._element_name,
            _type=self._type
        )

    def verify_value(self, value):
        return VerifyBot().verify_equal(
            expected=value,
            actual=self.get_value(),
            name=self._element_name,
            _type=self._type
        )

    def verify_value_contains(self, value):
        return VerifyBot().verify_contains(
            expected=value,
            actual=self.get_value(),
            name=self._element_name,
            _type=self._type
        )