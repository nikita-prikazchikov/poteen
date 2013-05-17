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
