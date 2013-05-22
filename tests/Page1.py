from selenium.webdriver.common.by import By
from BasePage import BasePage
from elements.basic.Button import Button
from elements.basic.Input import Input
from elements.basic.Link import Link

__author__ = 'nprikazchikov'


class GooglePage(BasePage):
    search = Input(id="gbqfq", element_name="Search")

    button = Button(id="gbqfb", element_name="Search")

    def __init__(self):
        BasePage.__init__(self)
        self.url = "/"


class FuelWebPage(BasePage):
    newEnvironment = Link(
        xpath="//div[@id='content']//div[@class='cluster-list']//div["
              "contains(@class, 'clusterbox create-cluster')]",
        element_name="New environment")

    errorElement = Link(
        xpath="//div[@id='content']//div[@class='cluster-list']//div["
              "contains(@class, 'clusterbox create-clusterdsfdfsfds')]",
        element_name="Error element name")

    def __init__(self):
        BasePage.__init__(self)
        self.url = ""


class AbstractView(BasePage):
    button_apply = Button(
        xpath=".//div[contains(@class, 'btn-apply')]",
        element_name="Apply"
    )
    button_cancel = Button(
        xpath=".//div[contains(@class, 'btn-discard')]",
        element_name="Cancel"
    )

    def __init__(self, parent):
        BasePage.__init__(self, parent)


class AbstractDialog(AbstractView):
    XPATH_DIALOG = "/html/body/div[contains(@class,'modal ')]"

    def __init__(self):
        AbstractView.__init__(self, self.get_control_dialog())
        self.wait_loading()

    def get_control_dialog(self):
        return self.get_wait_bot().wait_for_web_element(
            by=By.XPATH,
            value=self.XPATH_DIALOG
        )

    def wait_loading(self):
        return self.get_wait_bot().wait_for_stop_moving(
            by=By.XPATH,
            value=self.XPATH_DIALOG
        )


class CreateEnvironmentDialog(AbstractDialog):
    def __init__(self):
        AbstractDialog.__init__(self)

    def close(self):
        return self.get_wait_bot().wait_for_disappears(
            by=By.XPATH,
            value=self.XPATH_DIALOG
        )