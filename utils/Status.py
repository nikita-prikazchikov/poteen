__author__ = 'nprikazchikov'


class Status:
    PASSED = "passed"
    FAILED = "failed"

    @staticmethod
    def is_passed(value):
        return value == Status.PASSED

    @staticmethod
    def is_failed(value):
        return value == Status.FAILED

    @staticmethod
    def get_status(value):
        return Status.PASSED if value else Status.FAILED

    @staticmethod
    def get_worse_status(value1, value2):
        if value1 is None and value2 is None:
            status = None
        elif value1 is None:
            status = value2
        elif value2 is None:
            status = value1
        elif value1 is Status.FAILED or value2 is Status.FAILED:
            status = Status.FAILED
        elif value1 is Status.PASSED or value2 is Status.PASSED:
            status = Status.PASSED
        else:
            status = None
        return status
