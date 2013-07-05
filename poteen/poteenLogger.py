import glob
import hashlib
import json
import os
import time
import datetime
from .contextHolder import ContextHolder
from .utils.status import Status
from .log.resultList import ResultList
from .error import TestExecutionRuntimeException

__author__ = 'nprikazchikov'
logger = ContextHolder.get_logger()


class PoteenLogger:
    __testSuiteName = ""
    __testCaseName = ""
    __execution_log = []
    __current_test_cases = []
    __current_log = []
    __startTime = None

    def __init__(self):
        pass

    @classmethod
    def add_test_suite(cls, name):
        logger.info("Add test suite: {}".format(name))
        suite = {"name": name, "test_cases": []}
        cls.__current_test_cases = suite["test_cases"]
        cls.__testSuiteName = name
        cls.__execution_log.append(suite)
        ContextHolder.set_test_suite(name)

    @classmethod
    def add_test_case(cls, name):
        logger.info("Add test case: {}".format(name))
        case = {"name": name, "log": []}
        cls.__current_log = case["log"]
        cls.__testCaseName = name
        cls.__current_test_cases.append(case)
        cls.__startTime = time.time()

        ContextHolder.set_test_case(name)

    @classmethod
    def info(cls, result, blocking=True):
        logger.info("Test step result: {}".format(result))
        cls.__current_log.append(result)
        ResultList.clear_chain_result_list()
        if blocking and Status.is_failed(result.get_status()):
            raise TestExecutionRuntimeException(str(result))

    @classmethod
    def save_test_case_to_file(cls):
        def calculate(a, b):
            return Status.get_worse_status(a, b.get_status())

        status = reduce(calculate, cls.__current_log, Status.PASSED)
        name = hashlib.sha1()
        name.update(cls.__testSuiteName)
        name.update(cls.__testCaseName)
        name.update(str(cls.__startTime))

        resultFile = open(
            os.path.dirname(os.path.abspath(__file__))
            + "/../result/data/source/{name}.json".format(
                name=name.hexdigest()
            ), "w")
        resultFile.write(
            json.dumps(
                {
                    "id": name.hexdigest()[:8],
                    "test_suite_name": cls.__testSuiteName,
                    "name": cls.__testCaseName,
                    "status": status,
                    "log": str(cls.__current_log),
                    "start_time": datetime.datetime.fromtimestamp(
                        cls.__startTime).strftime('%Y-%m-%d %H:%M:%S'),
                    "end_time": str(
                        datetime.datetime.fromtimestamp(time.time())
                        .strftime('%Y-%m-%d %H:%M:%S')),
                    "execution_time": time.time() - cls.__startTime
                }
            )
        )
        resultFile.close()

    @classmethod
    def collect_test_result(cls):
        path = os.path.dirname(os.path.abspath(__file__)) + "/../result/data/"
        sourcePath = path + "source/"
        files = glob.glob1(sourcePath, "*.json")
        resultFilePath = path + "data.json"
        resultFile = open(resultFilePath, "w")
        resultFile.write("[")
        for i, fileName in enumerate(files):
            _file = open(sourcePath + fileName, "r")
            resultFile.write(_file.read())
            if i != len(files)-1:
                resultFile.write(",")
            _file.close()
        resultFile.write("]")
        resultFile.close()
