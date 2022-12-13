class SmallInputException(Exception):
    """Throw when input score less than 20"""


class LargeInputException(Exception):
    """Throw when input score is more than 21"""


class NegtaiveInputException(Exception):
    """Throw when input has negative number(s)"""


class InvalidStrikeException(Exception):
    """Throw when frame has invalid strike"""


class InvalidScoreException(Exception):
    """Throw when frame score is more than ten"""
