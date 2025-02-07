class Error(Exception):
    """Base class for exceptions in this module."""

    pass


class DatasetValidationError(Error):
    """Exception raised for errors in validating the dataset agains the standards.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message):
        self.message = message


class DuplicateError(Error):
    """Exception raised for errors due to duplicates in standards

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message):
        self.message = message


class DOIDuplicateError(Error):
    """Exception raised for errors due to duplicates in standards

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message):
        self.message = message


class ColumnDifferenceError(Error):
    """Exception raised for errors due to missing/added columns

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message):
        self.message = message
