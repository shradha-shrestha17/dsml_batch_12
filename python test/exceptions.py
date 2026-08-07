class InvalidRatingError(Exception):
    """Raised when rating is not between 1 and 5"""
    pass


class InvalidDistanceError(Exception):
    """Raised when distance is negative"""
    pass