import os
import sys
from tkinter import PhotoImage


class ResourceLoader:
    def __init__(self, base_path=None):
        """
        Initialize the ResourceLoader.

        Args:
            base_path: Directory path to load images from. If None, defaults
                       to 'assets/images' inside PyInstaller temp or source folder.
        """

        if base_path is None:
            if hasattr(sys, "_MEIPASS"):
                base_path = os.path.join(sys._MEIPASS, "assets", "images")
            else:
                base_path = os.path.join(os.path.dirname(__file__), "assets", "images")
        self.base_path = os.path.abspath(base_path)

    # --------------------------
    # Resource Loading Methods
    # --------------------------

    def get_resource_path(self, file_name: str):
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
        return PhotoImage(file=path) if os.path.exists(path) else None
