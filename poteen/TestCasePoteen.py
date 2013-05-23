from unittest import TestCase
from .log.ResultList import ResultList
from .PoteenLogger import PoteenLogger
from .bots.generic import start_driver, close_driver

__author__ = 'nprikazchikov'


class TestCasePoteen(TestCase):

    def __init__(self, methodName='runTest'):
        super(TestCasePoteen, self).__init__(methodName)
        self.addCleanup(self.clean_up_log)

    def clean_up_log(self):
        if len(ResultList.get_chain_result_list()):
            PoteenLogger.info(
                reduce(
                    lambda a, b: a.push(b, False),
                    ResultList.get_chain_result_list()
                )
            )

    def setUp(self):
        super(TestCasePoteen, self).setUp()
        start_driver()

    def tearDown(self):
        super(TestCasePoteen, self).tearDown()
        close_driver()

    @classmethod
    def setUpClass(cls):
        super(TestCasePoteen, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(TestCasePoteen, cls).tearDownClass()