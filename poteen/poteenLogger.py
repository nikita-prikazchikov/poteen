from .contextHolder import ContextHolder
from .utils.status import Status
from .log.resultList import ResultList
from .error import TestExecutionRuntimeException

__author__ = 'nprikazchikov'
logger = ContextHolder.get_logger()


class PoteenLogger:
    __execution_log = []
    __current_test_cases = []
    __current_log = []

    def __init__(self):
        pass

    @classmethod
    def add_test_suite(cls, name):
        logger.info("Add test suite: {}".format(name))
        suite = {"name": name, "test_cases": []}
        cls.__current_test_cases = suite["test_cases"]
        cls.__execution_log.append(suite)

    @classmethod
    def add_test_case(cls, name):
        logger.info("Add test case: {}".format(name))
        case = {"name": name, "log": []}
        cls.__current_log = case["log"]
        cls.__current_test_cases.append(case)

    @classmethod
    def info(cls, result, blocking=True):
        logger.info("Test step result: {}".format(result))
        cls.__current_log.append(result)
        ResultList.clear_chain_result_list()
        if blocking and Status.is_failed(result.get_status()):
            raise TestExecutionRuntimeException(str(result))
