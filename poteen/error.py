__author__ = 'nprikazchikov'


class PoteenError(Exception):
    """
    Base class for exceptions in poteen module
    """
    message = None

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return str(self.message)

    def __repr__(self):
        return str(self)


class IllegalAssignmentError(PoteenError):
    """
    Error for incorrect variable type assignment
    """

    def __init__(self, actual, expected):
        super(IllegalAssignmentError, self).__init__(
            "{} attribute must be an instance of {}"
            .format(type(actual), expected))


class ElementNotFoundException(PoteenError):
    """
    Error to define incorrect element access in case the element is not found
    Example:
    Button.click() throws this error in case element does not exist
    """

    def __init__(self, message):
        super(ElementNotFoundException, self).__init__(message)


class IllegalElementActionException(PoteenError):
    """
    Error to define incorrect element action access
    Example:
    Button.set_value()
    """

    def __init__(self, message):
        super(IllegalElementActionException, self).__init__(message)


class TestExecutionRuntimeException(PoteenError):
    """
    Error to define blocking step of test execution
    """

    def __init__(self, message):
        super(TestExecutionRuntimeException, self).__init__(message)
