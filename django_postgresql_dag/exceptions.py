"""Provides exceptions relevant to graphs"""


class NodeNotReachableException(Exception):
    """
    Exception for node distance and path
    """

    pass


class GraphModelsCannotBeParsedException(Exception):
    """
    Exception for node distance and path
    """

    pass


class IncorrectUsageException(Exception):
    """
    Exception for node distance and path
    """

    pass

class IncorrectQuerysetTypeException(Exception):
    """
    Exception for mismatch between helper method and queryset arg
    """

    pass
