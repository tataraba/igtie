class UserException(Exception):
    pass


class UserNotFound(UserException):

    def __init__(self, uri, message="User not found."):
        self.uri = uri
        self.message = message
        super().__init__(self.message)


class UserAccessDenied(UserException):

    def __init__(self, user_id, message="Access denied."):
        self.user_id = user_id
        self.message = message
        super().__init__(self.message)
