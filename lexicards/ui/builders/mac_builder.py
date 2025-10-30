from tkinter import Button
from lexicards.ui.builders.desktop_builder import DesktopLexiUiBuilder
from lexicards.ui.lexi_ui import LexiUi


class MacLexiUiBuilder(DesktopLexiUiBuilder):
    def __init__(self, root, images=None, known_callback=None, unknown_callback=None, audio_callback=None):
        super().__init__(root, images, known_callback, unknown_callback)
        self._audio_callback = audio_callback

    def build_window(self):
        self._root.title("LexiCards Mac")
        self._root.config(padx=50, pady=50, bg=LexiUi.BACKGROUND_COLOR)
        self._root.resizable(False, False)

    def build_canvas(self):
        canvas = super().build_canvas()
        canvas.grid(row=0, column=0, columnspan=3)
        self._ui.set_canvas(canvas)
        return canvas

    def build_buttons(self):
        # reuse desktop buttons
        unknown_button, known_button = super().build_buttons()

        # create audio button in the middle
        audio_button = Button(
            image=self._images["audio_image"],
            highlightthickness=0,
            relief="flat",
            bg=LexiUi.BACKGROUND_COLOR,
            command=self._audio_callback
        )
        audio_button.grid(row=1, column=1)

        # move existing buttons
        unknown_button.grid(row=1, column=0)
        known_button.grid(row=1, column=2)
        self._ui.set_unknown_button(unknown_button)
        self._ui.set_audio_buttons(audio_button)
        self._ui.set_known_button(known_button)
        return unknown_button, audio_button, known_button

