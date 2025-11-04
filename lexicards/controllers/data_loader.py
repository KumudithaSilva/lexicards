import os.path
import sys

from PIL.ImageTk import PhotoImage

from lexicards.core.singleton_meta import SingletonMeta
from lexicards.interfaces.data.i_resource_loader import IResourceLoader


class ResourceLoader(IResourceLoader, metaclass=SingletonMeta):
    """
    Singleton class for loading application resources.

    Ensures that only one instance exists and that its configuration
    (base_path) is initialized only once.

    Attributes:
        base_path (str): Absolute path to the directory containing resources.
    """

    def __init__(self, base_path=None):
        """
        Initialize the ResourceLoader.

        Args:
            base_path: Directory path to load images from. If None, defaults
                       to 'assets/images' inside PyInstaller temp or source folder.
        """
        if not hasattr(self, "_initialized"):
            if base_path is None:
                if hasattr(sys, "_MEIPASS"):
                    base_path = os.path.join(sys._MEIPASS, "assets", "images")
                else:
                    base_path = os.path.join(
                        os.path.dirname(__file__), "..", "assets", "images"
                    )
            self.base_path = os.path.abspath(base_path)
            self._initialized = True

    def get_resource_path(self, file_name: str) -> str:
        """
        Get the absolute file path for a resource file.

        Args:
            file_name: Name of the resource file.

        Returns:
            Absolute path to the resource file.
        """
        return os.path.join(self.base_path, file_name)

    def load_image(self, file_name: str):
        """
        Load an image from the base path.

        Args:
            file_name: Name of the image file.

        Returns:
            PhotoImage: Tkinter PhotoImage object if file exists, else None.
        """

        path = self.get_resource_path(file_name)
        if not os.path.exists(path):
            raise FileNotFoundError(f"Resource not found: {path}")
        return PhotoImage(file=path)
