from abc import ABCMeta


class SingletonMeta(ABCMeta):
    """
    Metaclass for creating Singleton classes.

    Ensures that only one instance of a class exists.
    Subsequent calls to instantiate the class will return
    the same instance.
    """

    _instances = {}  # Dictionary to store instances of each class

    def __call__(cls, *args, **kwargs):
        """
        Called when a class with this metaclass is instantiated.

        Args:
            *args: Positional arguments for the class constructor.
            **kwargs: Keyword arguments for the class constructor.

        Returns:
            The singleton instance of the class.
        """
        if cls not in cls._instances:
            # Create a new instance and store it in _instances
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]
