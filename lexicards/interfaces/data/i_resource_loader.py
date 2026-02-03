from abc import ABC, abstractmethod


class IResourceLoader(ABC):
    """Interface for resource loading mechanisms."""

    @abstractmethod
    def get_resource_path(self, file_name: str) -> str:
        """Return the absolute path for a given resource file."""
        pass

    @abstractmethod
    def load_image(self, file_name: str):
        """Load and return an image resource."""
        pass
