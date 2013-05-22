__author__ = 'nprikazchikov'


class iResult(object):
    def i_passed(self):
        raise NotImplementedError("Should have implemented this")

    def get_status(self):
        raise NotImplementedError("Should have implemented this")

    def get_comment(self):
        raise NotImplementedError("Should have implemented this")
