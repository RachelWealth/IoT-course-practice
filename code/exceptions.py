class mainFieldBothEmpty(Exception):
    pass


class unexpectedError(Exception):
    pass


class traversalError(Exception):
    """
        traversal database error
    """
    pass


# cannot found trained face data
class TrainingDataNotFoundError(FileNotFoundError):
    pass


# cannot found database related data
class DatabaseNotFoundError(FileNotFoundError):
    pass


class OperationCancel(Exception):
    pass


class RecordDisturbance(Exception):
    pass


class RecordNotFound(Exception):
    pass


