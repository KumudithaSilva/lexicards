from abc import ABC, abstractmethod
from tkinter import Tk


class LexiUiBuilderAbstract(ABC):

    def __init__(self, root: Tk, images: dict= None):
        self._root = root
        self._images = images or {}
        self._ui = None

    @abstractmethod
    def create_new_ui(self):
        pass

    @abstractmethod
    def build_window(self):
        pass

    @abstractmethod
    def build_canvas(self):
        pass

    @abstractmethod
    def build_text_elements(self):
        pass

    @abstractmethod
    def build_buttons(self):
        pass


    def get_result(self):
        return self._ui
