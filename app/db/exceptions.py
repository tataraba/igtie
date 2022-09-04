class DatabaseException(Exception):
    pass


class InvalidURIAddress(DatabaseException):
    """Exception raised for invalid MongoDB URI address.

    Attributes:
        uri -- URI address that caused the exception.
        message -- explanation of the error
    """

    def __init__(
        self,
        uri,
        message="Invalid URI address."
    ):
        self.uri = uri
        self.message = message
        super().__init__(self.message)


class DatabaseInitError(DatabaseException):
    """Exception raised for invalid database name.

    Attributes:
        db_name -- database name that caused the exception.
        message -- explanation of the error
    """

    def __init__(
        self,
        message="Database initialization failed."
    ):
        self.message = message
        super().__init__(self.message)
