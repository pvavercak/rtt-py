from enum import Enum


class ResultType(Enum):
    """Enum for recognizing result types.
    This enum makes it easier to check a type of the result obtained from a battery.
    Reduces complexity needed for generating final CSV report.
    Currently, only 2 types of results are generated by supported batteries.
    In future, there can be more result types, so let's be prepared.
    """
    P_VALUE = 0
    NUM_FAILURES = 1
    UNKNOWN = 255
