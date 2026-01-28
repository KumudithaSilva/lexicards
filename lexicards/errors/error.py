class LexiCardError(Exception):
    """Base class for all LexiCard-specific exceptions."""

    pass


class DataFileNotFoundError(LexiCardError):
    """Raised when the required data file cannot be found."""

    pass


class DataCorruptionError(LexiCardError):
    """Raised when a data file is found but is corrupted or unreadable."""

    pass
